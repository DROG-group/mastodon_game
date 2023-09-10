# This module sets up and configures logging for the application. 
# It ensures that logs are consistently formatted 
# and can be written to various outputs like files, databases, or external services.

import logging

def setup_logging(level=logging.INFO):
    logging.basicConfig(level=level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)
