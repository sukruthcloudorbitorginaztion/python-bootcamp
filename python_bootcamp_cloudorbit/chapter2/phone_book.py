"""
PhoneBook
---------
stores the phone number, name in the database(json file, xml file)
"""
import configparser
import os

from python_bootcamp_cloudorbit.chapter2.data_manager import JsonDataManager, XmlDataManager

CONFIG_FILE_NAME = "config.ini"
KEY_DATABASE_TYPE = "database_type"
KEY_DATABASE_LOCATION = "database_location"


DATABASE_TYPE_MAP = {"xml": XmlDataManager, "json": JsonDataManager}


class PhoneBook:
    """
    PhoneBook class1
    """

    def __init__(self):
        """
        Initialize the member variable
        """
        self._database_type, self._database_location = self.config_setup()
        self.config_setup()
        self.run_sequence()

    @property
    def base_dir(self):
        """
        Prpopertey to return base directory where config.ini file to be stored

        Returns:
            string: path of config.ini file to be stored
        """
        return os.path.dirname(os.path.realpath(__file__))

    @property
    def config_file_path(self):
        """
        Property to return config file path

        Returns:
            string: path of config.ini file path
        """
        return os.path.join(self.base_dir, CONFIG_FILE_NAME)

    def config_setup(self):
        """
        If you are executing the applicaiton for the first time then it will collect information
        such as database type(xml, json) and database location from the user,
        stores this info to the config.ini(next to Chapater2.py).

        Next time onwards, database type, database location is retrived from the config.ini

        Returns:
            tuple: database_type, database_location
        """
        config = configparser.ConfigParser()

        if not os.path.exists(self.config_file_path):
            print("Please specify the database type to be stored")
            keys = [key for key in DATABASE_TYPE_MAP.keys()]
            data_base_types = " or ".join(keys)
            database_type = input(f"Please enter your choice: {data_base_types} : ")
            database_location = input("Please speficy your database location e.g C:\\database : ")
            config["DEFAULT"] = {
                KEY_DATABASE_TYPE: database_type,
                KEY_DATABASE_LOCATION: database_location,
            }
            with open(self.config_file_path, "w") as config_file:
                config.write(config_file)

            return database_type, database_location
        else:
            config.read(self.config_file_path)
            return config["DEFAULT"][KEY_DATABASE_TYPE], config["DEFAULT"][KEY_DATABASE_LOCATION]

    def run_sequence(self):
        """
        Run the sequence till the operation is quit
        """
        cls_data_manager = DATABASE_TYPE_MAP[self._database_type]
        obj_data_manager = cls_data_manager(self._database_location, self._database_type)

        quit = False
        while not quit:
            print("Please select the below operation")
            print("1: Store the phone number and contact name")
            print("2: Find the contact name from phone number")
            print("3: Find the phone numbers from contact name")
            print("4: Remove the contact by providing phone number")
            print("5: Remove the phone numbers by providing contact name")
            print("q: To quit")
            response = input("Please select the option: ")
            if response == "1":
                phone_number = input("Please provide phone number: ")
                contact_name = input("Please provide contact name: ")
                obj_data_manager.store_info(phone_number, contact_name)
            elif response == "2":
                phone_number = input("Please provide phone number: ")
                print(
                    f"Name found for {phone_number} is "
                    + str(obj_data_manager.retrieve_name_from_phone_number(phone_number))
                )
            elif response == "3":
                contact_name = input("Please provide contact name: ")
                print(
                    f"Phone numbers associated with {contact_name} are "
                    + str(obj_data_manager.retrieve_phone_number_from_name(contact_name))
                )
            elif response == "4":
                phone_number = input("Please provide phone number: ")
                print(
                    f"Removed contact for {phone_number} is "
                    + str(obj_data_manager.remove_contact_by_phone_number(phone_number))
                )
            elif response == "5":
                contact_name = input("Please provide contact name: ")
                print(
                    f"Removed contacts for {contact_name} are "
                    + str(obj_data_manager.remove_contacts_by_name(contact_name))
                )
            else:
                quit = True


if __name__ == "__main__":
    PhoneBook()
