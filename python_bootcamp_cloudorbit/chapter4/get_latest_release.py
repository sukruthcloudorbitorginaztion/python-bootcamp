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

    # Fetch the page
    response = requests.get(url)
    response.raise_for_status()  # Raise exception if failed

    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        # Find the first release block
        release_div_download_widget = soup.find("div", class_="row download-list-widget")
        release_div = release_div_download_widget.find("ol", class_=["list-row-container", "menu"])
        if release_div:
            # Extract release title (e.g., "Python 3.13.9")
            version = release_div.find("span", class_="release-number").get_text(strip=True)
            
            # Extract the link
            link_tag = release_div.find("a")
            if link_tag and link_tag["href"]:
                download_link = f"https://www.python.org{link_tag['href']}"
            else:
                download_link = "Link not found"

            print(f"Latest release: {version}")
            print(f"Download link: {download_link}")
            return (version, download_link)
        else:
            print("No release information found on the page.")
    except:
        print("No release information found on the page.")



if __name__ == "__main__":
    get_latest_release("https://www.python.org/downloads/")