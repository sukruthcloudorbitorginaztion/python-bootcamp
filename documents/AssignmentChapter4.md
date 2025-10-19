
# Assignment: Fetch Latest Release from a Website

## Objective

The objective of this assignment is to **write a Python function that fetches and parses the latest release information from a website**, such as the Python downloads page.

Students will learn to:

* Send HTTP requests and handle responses
* Parse HTML content using **BeautifulSoup**
* Extract specific elements based on HTML structure
* Handle edge cases like missing elements or HTTP errors

---

## Required Skills

To successfully complete this assignment, you should be familiar with:

* Python **functions** and **return values**
* **HTTP requests** using the `requests` module
* Parsing HTML using **BeautifulSoup**
* Handling **exceptions** in Python
* Understanding basic HTML structure (tags, classes, and attributes)

---

## Problem Statement

Websites like [python.org](https://www.python.org/downloads/) often list the latest releases of their software in a structured HTML format.

Your task is to write a function called **`get_latest_release(url)`** that:

1. Accepts a **URL** of a downloads page.
2. Sends a **GET request** to fetch the HTML content.
3. Parses the HTML and extracts:

   * The **latest release version** (e.g., `"Python 3.13.9"`)
   * The **download link** for that release
4. Returns a **tuple** `(version, download_link)`.
5. Handles cases where no release information is found by returning `None` and printing a message.
6. Raises an exception for HTTP request errors.

---

## Sample Input and Output

### Example 1

```python
url = "https://www.python.org/downloads/"
version, link = get_latest_release(url)

print(version)  # Output: Python 3.13.9
print(link)     # Output: https://www.python.org/downloads/release/python-3139/
```

### Example 2 (No release information)

```python
url = "https://www.example.com/no-releases"
result = get_latest_release(url)
print(result)   # Output: None
# Printed message: "No release information found on the page."
```

---

## Hints & Tips

* Use **`requests.get()`** to fetch the page and **`response.raise_for_status()`** to handle HTTP errors.
* Use **BeautifulSoup** with the `"html.parser"` to parse the HTML.
* Check the website’s HTML structure in a browser’s **DevTools** to locate the correct `div` or `ol` containing release information.
* When selecting elements with **multiple classes**, pass a **list** to `class_` or use **CSS selectors**:

  ```python
  soup.select_one("div.list-row-container.menu")
  ```
* Use `.get_text(strip=True)` to extract clean text from tags.
* Handle edge cases:

  * Missing release block → return `None`
  * Missing download link → provide a placeholder or error message
  * HTTP errors → raise exception

---

## Deliverables

1. **Python Function**

   * File: `get_latest_release.py`
   * Function: `get_latest_release(url)`
   * Requirements:

     * Correctly extracts latest release version and download link
     * Handles missing release information
     * Raises exceptions for HTTP errors
     * Includes docstrings for clarity



---
