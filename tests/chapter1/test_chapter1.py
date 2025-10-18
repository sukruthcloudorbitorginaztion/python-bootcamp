import os
import pytest
import shutil

from python_bootcamp_cloudorbit.chapter1 import mako_file_updator

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
INPUT_DIR = os.path.join(TEST_DIR, "input")
OUTPUT_DIR = os.path.join(TEST_DIR, "output")


@pytest.fixture(autouse=True)
def mock_args(monkeypatch):
    monkeypatch.setattr(
        "sys.argv",
        [
            "dummy",
            "--input_path",
            INPUT_DIR,
            "--output_path",
            OUTPUT_DIR,
            "--phone_number",
            "12345",
            "--event_name",
            "python_book_club",
        ],
    )
    yield
    shutil.rmtree(OUTPUT_DIR)


def test_chapter1():
    obj = mako_file_updator.MakoFileUpdator()
    obj.update()

    # validate the files
    ni_india_event_file_path = os.path.join(OUTPUT_DIR, "ni_india_event.txt")
    phonebook_file_path = os.path.join(OUTPUT_DIR, "phonebook.csv")

    with open(ni_india_event_file_path) as f:
        expected = (
            """Event name python_book_club\nPlease call to 12345 to register for the events\n"""
        )
        contents = f.read()
        assert expected == contents

    with open(phonebook_file_path) as f:
        expected = """Organization Location ,PhoneNumber\nNI Austin,1 800-433-3488\nNI Hungary,36 52 515 400\nNI India,12345\n"""
        contents = f.read()
        assert expected == contents
