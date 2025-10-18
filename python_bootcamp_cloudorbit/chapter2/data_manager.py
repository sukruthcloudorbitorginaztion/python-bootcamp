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
        self.database_location = database_location
        self.file_type = file_type
        self.file_contents = self.read_file_contents()

    def __del__(self):
        """
        Write the contents to file before shutting down
        """
        self.write_to_file()

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
        self.file_contents[phone_number] = name

    def retrieve_name_from_phone_number(self, phone_number):
        """
        Retrieve the name from phone number

        Args:
            phone_number (string ): phone number

        Returns:
            string: contact name
        """
        if phone_number in self.file_contents:
            return self.file_contents[phone_number]
        return ""

    def retrieve_phone_number_from_name(self, name):
        """
        Retrieve the phone numbers from name

        Args:
            name (string ): contact name

        Returns:
            string array: list of phone numbers
        """
        return [
            phone_number
            for phone_number, contact_name in self.file_contents.items()
            if name == contact_name
        ]

    def remove_contact_by_phone_number(self, phone_number):
        """Removes the contact info by its phone number

        Args:
            phone_number (string): phone number of the contact
        """
        res = self.file_contents.pop(phone_number, None)
        if res:
            return (phone_number, res)

    def remove_contacts_by_name(self, contact_name):
        """Removes the contacts info by its contact name

        Args:
            contact_name (string): phone number of the contact
        """
        return [
            self.remove_contact_by_phone_number(phone_number)
            for phone_number in self.retrieve_phone_number_from_name(contact_name)
        ]

    @property
    def database_file_path(self):
        """
        Returns the database file path

        Returns:
            string: database file path
        """
        return os.path.join(self.database_location, f"{DATABASE_FILE_PREFIX}.{self.file_type}")


class JsonDataManager(DataManager):
    """
    JsonDataManager
    """

    def read_file_contents(self):
        """
        Read file contents, convert to dictionary
        """
        if os.path.exists(self.database_file_path):
            with open(self.database_file_path, "r") as json_file:
                return json.loads(json_file.read())
        else:
            return {}

    def write_to_file(self):
        """
        Write the file contents back to file
        """
        json_data = json.dumps(self.file_contents, indent=4)
        if not os.path.exists(self.database_location):
            os.mkdir(self.database_location)
        with open(self.database_file_path, "w") as outfile:
            outfile.write(json_data)


class XmlDataManager(DataManager):
    """
    JsonDataManager
    """

    def read_file_contents(self):
        """
        Read file contents, convert to dictionary
        """
        file_contents = {}
        if os.path.exists(self.database_file_path):
            tree = ETree.parse(self.database_file_path)
            root = tree.getroot()
            for contact in root.iter("contact"):
                phone_number = contact.find("phonenumber").text
                name = contact.find("name").text
                file_contents[phone_number] = name
        return file_contents

    def write_to_file(self):
        """
        Write the file contents back to file
        """
        if not os.path.exists(self.database_location):
            os.mkdir(self.database_location)

        if len(self.file_contents) == 0:
            if os.path.exists(self.database_file_path):
                os.remove(self.database_file_path)
            return
        root_element = ETree.Element("root")
        for phone_number, name in self.file_contents.items():
            contact_element = ETree.Element("contact")
            phone_number_element = ETree.Element("phonenumber")
            phone_number_element.text = phone_number
            name_element = ETree.Element("name")
            name_element.text = name
            contact_element.append(phone_number_element)
            contact_element.append(name_element)
            root_element.append(contact_element)

        xmlstr = minidom.parseString(ETree.tostring(root_element)).toprettyxml(indent="    ")
        with open(self.database_file_path, "wb") as xml_file:
            xml_file.write(xmlstr.encode("utf-8"))
