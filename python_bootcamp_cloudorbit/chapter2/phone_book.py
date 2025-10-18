"""
PhoneBook
---------
stores the phone number, name in the database(json file, xml file)
"""
import configparser
import os

from python_bootcamp_cloudorbit.chapter2.data_manager import JsonDataManager, XmlDataManager

CONFIG_FILE_NAME = "config.ini"


DATABASE_TYPE_MAP = {"xml": XmlDataManager, "json": JsonDataManager}


class PhoneBook:
    """
    PhoneBook class1
    """

    def __init__(self):
        """
        Initialize the member variable
        """
        pass



if __name__ == "__main__":
    PhoneBook()
