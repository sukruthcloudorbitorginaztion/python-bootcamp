"""
data store
----------
Store the phone book
"""
import json
import os
import xml.etree.ElementTree as ETree
from abc import ABC, abstractmethod
from xml.dom import minidom

DATABASE_FILE_PREFIX = "database"


class DataManager(ABC):
    """
    DataManager class has abstract methods to be implemented for managing data(read, write)
    """

    def __init__(self, database_location, file_type):
        """
        Initializes the values for DataManager

        Args:
            database_location (string): database directory where the database file is located
            type (string): type e.g xml, json
        """
        pass

    def __del__(self):
        """
        Write the contents to file before shutting down
        """
        pass

    @abstractmethod
    def read_file_contents(self):
        """
        Read file contents
        """
        pass

    @abstractmethod
    def write_to_file(self):
        """
        Write the file contents back to file
        """
        pass

    def store_info(self, phone_number, name):
        """
        Store the infromation to base

        Args:
            phone_number (string): phone number
            name (string): contact name
        """
        pass

    def retrieve_name_from_phone_number(self, phone_number):
        """
        Retrieve the name from phone number

        Args:
            phone_number (string ): phone number

        Returns:
            string: contact name
        """
        pass

    def retrieve_phone_number_from_name(self, name):
        """
        Retrieve the phone numbers from name

        Args:
            name (string ): contact name

        Returns:
            string array: list of phone numbers
        """
        pass

    def remove_contact_by_phone_number(self, phone_number):
        """Removes the contact info by its phone number

        Args:
            phone_number (string): phone number of the contact
        """
        pass

    def remove_contacts_by_name(self, contact_name):
        """Removes the contacts info by its contact name

        Args:
            contact_name (string): phone number of the contact
        """
        pass

    @property
    def database_file_path(self):
        """
        Returns the database file path

        Returns:
            string: database file path
        """
        pass


class JsonDataManager(DataManager):
    """
    JsonDataManager
    """
    pass



class XmlDataManager(DataManager):
    """
    JsonDataManager
    """
    pass