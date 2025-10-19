"""
get latest directory from the http url
"""

from dataclasses import dataclass, field
from datetime import datetime

import requests
from bs4 import BeautifulSoup

def get_latest_release(url):
    """Get the latest directory and date time created in the url path

    Args:
        url_path_of_repo (string): e.g

    Raises:
        Exception: [description]: e.g
        https://www.python.org/downloads/"

    Returns:
        [tuple(dir, date_time)]: return the tuple(directory_name and directory created date)
    """
    pass



if __name__ == "__main__":
    get_latest_release("https://www.python.org/downloads/")