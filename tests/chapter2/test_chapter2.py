import os
import shutil
from  python_bootcamp_cloudorbit.chapter2.phone_book import (
    CONFIG_FILE_NAME,
    PhoneBook,
    KEY_DATABASE_TYPE,
    KEY_DATABASE_LOCATION,
)
from tests.chapter2.tud_test_base import set_keyboard_input, get_display_output
import pytest

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE_PATH = os.path.abspath(
    os.path.join(TEST_DIR, "..", "..", "python_bootcamp_cloudorbit", "chapter2", CONFIG_FILE_NAME)
)
OUTPUT_DIR = os.path.join(TEST_DIR, "output")


@pytest.fixture(autouse=True)
def mock_args():
    if os.path.exists(CONFIG_FILE_PATH):
        os.remove(CONFIG_FILE_PATH)
    yield
    if os.path.exists(CONFIG_FILE_PATH):
        os.remove(CONFIG_FILE_PATH)
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)


def test_chapter2_config_file_json():
    set_keyboard_input(["json", OUTPUT_DIR, "q"])
    obj = PhoneBook()
    expected = f"[DEFAULT]\n{KEY_DATABASE_TYPE} = json\n{KEY_DATABASE_LOCATION} = {OUTPUT_DIR}\n\n"
    with open(CONFIG_FILE_PATH, "r") as fp:
        output = fp.read()
    assert expected == output


def test_chapter2_config_file_xml():
    set_keyboard_input(["xml", OUTPUT_DIR, "q"])
    obj = PhoneBook()
    expected = f"[DEFAULT]\n{KEY_DATABASE_TYPE} = xml\n{KEY_DATABASE_LOCATION} = {OUTPUT_DIR}\n\n"
    with open(CONFIG_FILE_PATH, "r") as fp:
        output = fp.read()
    assert expected == output


@pytest.mark.parametrize(
    "config, expected_file_contents",
    [
        (
            "xml",
            '<?xml version="1.0" ?>\n<root>\n    <contact>\n        <phonenumber>10</phonenumber>\n        <name>name1</name>\n    </contact>\n</root>\n',
        ),
        ("json", '{\n    "10": "name1"\n}'),
    ],
)
def test_chapter2_xml_testing(config, expected_file_contents):
    set_keyboard_input(
        [
            config,
            OUTPUT_DIR,
            "1",
            "10",
            "name1",
            "1",
            "100",
            "name2",
            "1",
            "1000",
            "name3",
            "2",
            "1000",
            "1",
            "1001",
            "name2",
            "3",
            "name2",
            "4",
            "1000",
            "5",
            "name2",
            "" "q",
        ]
    )

    expected_list = [
        "Name found for 1000 is name3",
        "Phone numbers associated with name2 are ['100', '1001']",
        "Removed contact for 1000 is ('1000', 'name3')",
        "Removed contacts for name2 are [('100', 'name2'), ('1001', 'name2')]",
    ]

    def phone_book_call():
        obj = PhoneBook()

    phone_book_call()
    std_out_list = get_display_output()

    # verifcation output
    for message in expected_list:
        assert message in std_out_list

    with open(os.path.join(OUTPUT_DIR, f"database.{config}")) as fp:
        file_output = fp.read()
    assert expected_file_contents == file_output