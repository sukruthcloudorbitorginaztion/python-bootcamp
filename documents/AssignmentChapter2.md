# Phone Book Application - Assignment

## Overview
Build a command-line phone book application that stores contacts persistently using either JSON or XML format. This assignment introduces key programming concepts including abstract classes, file I/O, configuration management, and working with multiple data formats.

## Learning Objectives
By completing this assignment, you will learn:
- **Abstract Base Classes (ABC)**: Implement abstract methods to enforce a common interface
- **File I/O Operations**: Read from and write to files in different formats
- **XML Processing**: Parse and generate XML documents using ElementTree
- **JSON Processing**: Work with JSON data structures
- **Configuration Management**: Use ConfigParser to store and retrieve application settings
- **Code Extensibility**: Design classes that can be easily extended for new data formats
- **Object-Oriented Design**: Apply inheritance and polymorphism principles

## Problem Statement
Create a phone book application that allows users to:
1. Store contact information (phone number and name)
2. Retrieve contact names by phone number
3. Retrieve phone numbers by contact name
4. Delete contacts by phone number
5. Delete all contacts associated with a name

The application must support two storage formats:
- **JSON**: Store data as key-value pairs
- **XML**: Store data as structured elements

On first run, the application asks users to configure:
- Database type (json or xml)
- Database location (directory path)

These settings are saved in `config.ini` and used for subsequent runs.

## Implementation Requirements

### File Structure
```
chapter2/
├── data_manager.py      # DataManager classes (to be implemented)
├── phone_book.py        # PhoneBook main class (to be implemented)
└── config.ini          # Auto-generated configuration file
```

### 1. data_manager.py

Implement three classes:

#### **DataManager (Abstract Base Class)**
- `__init__(database_location, file_type)`: Initialize with storage location and file type
- `__del__()`: Write contents to file before shutdown
- `read_file_contents()`: Abstract method - read and parse file
- `write_to_file()`: Abstract method - write data to file
- `store_info(phone_number, name)`: Store a contact
- `retrieve_name_from_phone_number(phone_number)`: Get name by phone number
- `retrieve_phone_number_from_name(name)`: Get all phone numbers for a name
- `remove_contact_by_phone_number(phone_number)`: Remove contact by phone number
- `remove_contacts_by_name(contact_name)`: Remove all contacts with given name
- `database_file_path`: Property returning the full path to database file

#### **JsonDataManager**
Extends DataManager to handle JSON format:
- `read_file_contents()`: Load JSON file into dictionary
- `write_to_file()`: Save dictionary as formatted JSON

#### **XmlDataManager**
Extends DataManager to handle XML format:
- `read_file_contents()`: Parse XML into dictionary
- `write_to_file()`: Generate formatted XML from dictionary

**XML Structure:**
```xml
<?xml version="1.0" ?>
<root>
    <contact>
        <phonenumber>1234567890</phonenumber>
        <name>John Doe</name>
    </contact>
    <contact>
        <phonenumber>9876543210</phonenumber>
        <name>Jane Smith</name>
    </contact>
</root>
```

**JSON Structure:**
```json
{
    "1234567890": "John Doe",
    "9876543210": "Jane Smith"
}
```

### 2. phone_book.py

#### **PhoneBook Class**
- `__init__()`: Set up configuration and start the application
- `config_setup()`: Handle first-time setup or load existing configuration
- `run_sequence()`: Main application loop with menu system
- `base_dir`: Property returning directory where config.ini is stored
- `config_file_path`: Property returning full path to config.ini

## Sample Input and Output

### First Run (Configuration Setup)

```
Please specify the database type to be stored
Please enter your choice: xml or json : json
Please speficy your database location e.g C:\database : /home/user/phonebook_data

Please select the below operation
1: Store the phone number and contact name
2: Find the contact name from phone number
3: Find the phone numbers from contact name
4: Remove the contact by providing phone number
5: Remove the phone numbers by providing contact name
q: To quit
Please select the option: 1
Please provide phone number: 1234567890
Please provide contact name: John Doe

Please select the below operation
1: Store the phone number and contact name
2: Find the contact name from phone number
3: Find the phone numbers from contact name
4: Remove the contact by providing phone number
5: Remove the phone numbers by providing contact name
q: To quit
Please select the option: 1
Please provide phone number: 9876543210
Please provide contact name: Jane Smith

Please select the below operation
1: Store the phone number and contact name
2: Find the contact name from phone number
3: Find the phone numbers from contact name
4: Remove the contact by providing phone number
5: Remove the phone numbers by providing contact name
q: To quit
Please select the option: 2
Please provide phone number: 1234567890
Name found for 1234567890 is John Doe

Please select the below operation
1: Store the phone number and contact name
2: Find the contact name from phone number
3: Find the phone numbers from contact name
4: Remove the contact by providing phone number
5: Remove the phone numbers by providing contact name
q: To quit
Please select the option: q
```

### Subsequent Runs (Using Saved Configuration)

```
Please select the below operation
1: Store the phone number and contact name
2: Find the contact name from phone number
3: Find the phone numbers from contact name
4: Remove the contact by providing phone number
5: Remove the phone numbers by providing contact name
q: To quit
Please select the option: 3
Please provide contact name: Jane Smith
Phone numbers associated with Jane Smith are ['9876543210']

Please select the below operation
1: Store the phone number and contact name
2: Find the contact name from phone number
3: Find the phone numbers from contact name
4: Remove the contact by providing phone number
5: Remove the phone numbers by providing contact name
q: To quit
Please select the option: 1
Please provide phone number: 5555555555
Please provide contact name: Jane Smith

Please select the below operation
1: Store the phone number and contact name
2: Find the contact name from phone number
3: Find the phone numbers from contact name
4: Remove the contact by providing phone number
5: Remove the phone numbers by providing contact name
q: To quit
Please select the option: 3
Please provide contact name: Jane Smith
Phone numbers associated with Jane Smith are ['9876543210', '5555555555']

Please select the below operation
1: Store the phone number and contact name
2: Find the contact name from phone number
3: Find the phone numbers from contact name
4: Remove the contact by providing phone number
5: Remove the phone numbers by providing contact name
q: To quit
Please select the option: 4
Please provide phone number: 1234567890
Removed contact for 1234567890 is ('1234567890', 'John Doe')

Please select the below operation
1: Store the phone number and contact name
2: Find the contact name from phone number
3: Find the phone numbers from contact name
4: Remove the contact by providing phone number
5: Remove the phone numbers by providing contact name
q: To quit
Please select the option: 5
Please provide contact name: Jane Smith
Removed contacts for Jane Smith are [('9876543210', 'Jane Smith'), ('5555555555', 'Jane Smith')]

Please select the below operation
1: Store the phone number and contact name
2: Find the contact name from phone number
3: Find the phone numbers from contact name
4: Remove the contact by providing phone number
5: Remove the phone numbers by providing contact name
q: To quit
Please select the option: q
```

## Testing Your Implementation

Run the provided test cases to verify your implementation:

```bash
pytest test_chapter2.py
```

The tests will verify:
- Configuration file creation with correct format
- JSON database operations
- XML database operations
- Contact storage and retrieval
- Contact deletion by phone number and name

## Key Implementation Tips

1. **File Creation**: Create the database directory if it doesn't exist
2. **Empty Database**: Handle cases where the database file doesn't exist yet
3. **XML Formatting**: Use `minidom.toprettyxml()` for readable XML output
4. **JSON Formatting**: Use `json.dumps()` with `indent=4` for readable JSON
5. **Destructor**: The `__del__()` method ensures data is saved when the program exits
6. **Dictionary Structure**: Use phone number as key, name as value for internal storage
7. **Multiple Numbers**: One name can have multiple phone numbers
8. **Return Values**: Methods should return appropriate values (empty string, empty list, None, or tuples)

## Submission Checklist

- [ ] `data_manager.py` with all three classes implemented
- [ ] `phone_book.py` with PhoneBook class implemented
- [ ] All test cases pass
- [ ] Code follows Python naming conventions
- [ ] Proper docstrings for all methods
- [ ] Error handling for file operations
- [ ] Configuration persists across runs
