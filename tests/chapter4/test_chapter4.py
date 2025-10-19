import pytest
from python_bootcamp_cloudorbit.chapter4.get_latest_release import get_latest_release


@pytest.fixture(scope="function")
def python_downloads_html():
    """Simulated HTML page for python.org/downloads/"""
    return """
    <div class="row download-list-widget">
        <ol class="list-row-container menu">
            <li>
                <span class="release-number">Python 3.13.9</span>
                <a href="/downloads/release/python-3139/">Download</a>
            </li>
        </ol>
    </div>
    """


def test_get_latest_release(requests_mock, python_downloads_html):
    """Test successful parsing of version and link from HTML."""
    url = "https://www.python.org/downloads/"

    # Mock the HTTP GET request
    requests_mock.get(url, text=python_downloads_html)

    expected_result = (
        "Python 3.13.9",
        "https://www.python.org/downloads/release/python-3139/",
    )

    result = get_latest_release(url)
    assert result == expected_result


def test_get_latest_release_no_release_found(requests_mock):
    """Test when no release section is found in HTML."""
    url = "https://www.python.org/downloads/"
    requests_mock.get(url, text="<html><body>No releases</body></html>")

    result = get_latest_release(url)
    assert result is None


def test_get_latest_release_http_error(requests_mock):
    """Test that HTTP errors raise exceptions."""
    url = "https://www.python.org/downloads/"
    requests_mock.get(url, status_code=404)

    with pytest.raises(Exception):
        get_latest_release(url)
