# status_import_service.py
# This service module manages the importation of status updates from CSV files into the game's Mastodon instance.
# It provides functions to parse, validate, and store status updates, ensuring they fit within the game's narrative structure.

import csv
from app.models import Status  # Assuming you have a Status model
from app.services import database_service  # Assuming you have a service to interact with the database

class StatusImportService:

    @staticmethod
    def import_statuses_from_csv(file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                StatusImportService._store_status(row)

    @staticmethod
    def _store_status(status_data):
        # Validate the status data if necessary
        if StatusImportService._validate_status(status_data):
            status = Status(
                created_at=status_data['created_at'],  # This will be the backdated timestamp
                updated_at=status_data['updated_at'],  # This can also be backdated, or set to the current time
                account_username=status_data['account_username'],
                text=status_data['text'],
                interaction_type=status_data['interaction_type'],
                in_reply_to_id=status_data['in_reply_to_id'],
                reblog_of_id=status_data['reblog_of_id'],
                media_attachment_ids=status_data['media_attachment_ids'],
                visibility=status_data['visibility']
            )
            database_service.add_and_commit(status)