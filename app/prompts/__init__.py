"""
app/prompts/__init__.py

This module provides a centralized location for loading and parsing prompt content 
from the corresponding YAML files in the `app/prompts` package and its subdirectories.

The content from the YAML files is exposed as package-level variables, allowing easy 
import and access to the prompts throughout the application.

Attributes:
    All the parsed content from the YAML files will be available as package-level variables.
    The variable names will correspond to the base filenames of the YAML files.

Usage:
    from app.prompts import some_yaml_filename_without_extension

"""

import yaml
import os
import glob

# Directory path for the app/prompts/ directory
base_path = "app/prompts/"

# Search for all .yaml and .yml files recursively in the directory
yaml_files = glob.glob(base_path + '**/*.yaml', recursive=True) + \
             glob.glob(base_path + '**/*.yml', recursive=True)

# Load and parse each found YAML file and expose its content as a package-level variable
for yaml_file in yaml_files:
    with open(yaml_file, 'r') as file:
        content = yaml.safe_load(file)
        
        # Extract the base filename without extension and set it as the variable name
        variable_name = os.path.splitext(os.path.basename(yaml_file))[0]
        
        # Use globals() to set the variable at the module level
        globals()[variable_name] = content