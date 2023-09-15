"""
world_service.py

This module provides services related to the generation and management of the game's world narrative, including 
creating and updating statuses (toots) using the OpenAI API.

The primary functionality is to iteratively generate toots and world descriptions, ensuring that the narrative
context is maintained between iterations.

Functions:
    generate_toots_iteratively(): Generate toots and the world description iteratively using the OpenAI API.

Dependencies:
    openai: Python client for the OpenAI API.
    yaml: Module to load and parse YAML formatted data.
    time: Module to handle time-related tasks.
    app.prompts: Module that provides access to predefined prompts from YAML files.
"""

import openai
import yaml
import time
from app.prompts import world_system  # Import the system context directly

def generate_toots_iteratively():
    """
    Generate toots iteratively using the OpenAI API.
    Also, generate the world description the first time this function is invoked.

    This function will:
    1. Use the imported `world_system` as the system context.
    2. Use the OpenAI API to generate narrative content based on the system context.
    3. Extract the world description if it's the first iteration.
    4. Extract CSV content from the generated narrative for further processing or storage.
    5. Repeat this process for a duration of one hour.
    """
    
    # Use the imported `world_system` as the system context
    system_context = world_system
    
    # Check if this is the first invocation
    first_time = True  # This can be determined using other logic like checking a database or a flag
    
    end_time = time.time() + 3600  # One hour from now
    
    while time.time() < end_time:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                    "role": "system",
                    "content": system_context,
                },
            ],
        )
        generated_content = response.choices[0].message['content']
        
        # If it's the first time, extract the world description
        if first_time:
            world_description_yaml = extract_yaml_content(generated_content)
            world_description = yaml.safe_load(world_description_yaml)
            
            # Store or process the world description as needed
            # For example: store_world_description(world_description)
            
            # Update the system context to include the first-time generated memory for subsequent iterations
            system_context += world_description_yaml
            first_time = False
        
        # Extract CSV from the generated content
        csv_content = extract_csv_content(generated_content)
        
        # Store the CSV content or process as needed
        # For example: store_csv(csv_content)
        
        # Sleep for a while before the next iteration if needed
        time.sleep(10)

def extract_yaml_content(content):
    """
    Extracts the YAML content from a given string based on defined bookends or markers.

    Args:
        content (str): The content string containing embedded YAML data.

    Returns:
        str: The extracted YAML content, or an empty string if the bookends are not found.
    """
    # Define bookends or markers to detect YAML content
    start_tag = "<YAMLBegin:"
    end_tag = ":YAMLEnd>"
    
    # Extract content between the bookends
    start_pos = content.find(start_tag)
    end_pos = content.find(end_tag)
    
    if start_pos != -1 and end_pos != -1:
        return content[start_pos + len(start_tag):end_pos].strip()
    
    return ""

def extract_csv_content(content):
    """
    Extracts the CSV content from a given string based on defined bookends or markers.

    Args:
        content (str): The content string containing embedded CSV data.

    Returns:
        str: The extracted CSV content, or an empty string if the bookends are not found.
    """
    # Define bookends or markers to detect CSV content
    start_tag = "<CSVBegin:"
    end_tag = ":CSVEnd>"
    
    # Extract content between the bookends
    start_pos = content.find(start_tag)
    end_pos = content.find(end_tag)
    
    if start_pos != -1 and end_pos != -1:
        return content[start_pos + len(start_tag):end_pos].strip()
    
    return ""
