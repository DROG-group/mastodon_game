"""
status_import_service.py

This module provides services related to importing status updates from CSV files into the game's Mastodon instance.
It contains utility functions to parse, validate, and store status updates, ensuring they fit within the game's 
narrative structure. The module also includes utilities to extract status content from generated completions, 
clean up status IDs for consistency, and ensure user existence.

Classes:
    StatusImportService: A class with static methods providing services for importing and storing status updates.

Dependencies:
    csv: Module to read from and write to comma-separated value (CSV) files.
    re: Module providing support to work with Regular Expressions.
    app.models: Module containing the game's data models.
    app.services: Module containing service utilities for database interactions.
    app.services.user_service: Module providing user-related services.
"""

import csv
import re
from app.models import Status, User
from app.services import database_service
from app.services.user_service import get_user_by_username, create_user

class StatusImportService:
    """
    A service class providing static methods to handle status import operations.
    """

    @staticmethod
    def extract_csv_content(content):
        """
        Extracts the content between the last occurrence of <CSVBegin: and :CSV end> bookends.

        Args:
            content (str): The content string containing embedded CSV data.

        Returns:
            str: The extracted CSV content, or an empty string if the bookends are not found.
        """
        pattern = r"<CSVBegin:(.*?):CSV end>"
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            return match.group(1).strip()
        
        return ""

    @staticmethod
    def clean_csv_ids(rows):
        """
        Cleans the generated CSV data to ensure the IDs are consistent and unique.

        Args:
            rows (list): A list of dictionaries containing status data.

        Returns:
            None: The function modifies the `rows` argument in place.
        """
        if not rows:
            return

        start_id = 1
        if 'id' in rows[-1]:
            start_id = int(rows[-1]['id']) + 1

        id_mapping = {}

        for row in rows:
            old_id = row['id']
            row['id'] = str(start_id)
            id_mapping[old_id] = str(start_id)
            start_id += 1

        for row in rows:
            if row['in_reply_to_id'] in id_mapping:
                row['in_reply_to_id'] = id_mapping[row['in_reply_to_id']]
            if row['reblog_of_id'] in id_mapping:
                row['reblog_of_id'] = id_mapping[row['reblog_of_id']]

    @staticmethod
    def import_statuses_from_csv(file_path):
        """
        Imports status updates from a provided CSV file.

        The function extracts the CSV content, cleans up status IDs, ensures users exist in the system, and stores 
        the status updates in the database.

        Args:
            file_path (str): The path to the CSV file containing status updates.

        Returns:
            None
        """
        with open(file_path, 'r') as file:
            content = file.read()
            csv_content = StatusImportService.extract_csv_content(content)
            reader = csv.DictReader(csv_content.splitlines())
            rows = list(reader)

        # Clean IDs and ensure users exist
        StatusImportService.clean_csv_ids(rows)
        for row in rows:
            username = row['account_username']
            if not get_user_by_username(username):
                create_user(username)
            StatusImportService._store_status(row)

    @staticmethod
    def _store_status(status_data):
        """
        Stores a status update in the database.

        Args:
            status_data (dict): A dictionary containing status data.

        Returns:
            None
        """
        status = Status(
            created_at=status_data['created_at'],
            updated_at=status_data['updated_at'],
            account_username=status_data['account_username'],
            text=status_data['text'],
            interaction_type=status_data['interaction_type'],
            in_reply_to_id=status_data['in_reply_to_id'],
            reblog_of_id=status_data['reblog_of_id'],
            media_attachment_ids=status_data['media_attachment_ids'],
            visibility=status_data['visibility']
        )
        database_service.add_and_commit(status)
