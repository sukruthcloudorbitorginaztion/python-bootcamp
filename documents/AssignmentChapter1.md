
# **Chapter1 Assignment: Mako Template File Updater**

## **Objective**

Implement a Python module `MakoFileUpdater` that reads Mako template files, replaces placeholders with values provided via command-line arguments, and outputs the rendered files to a specified directory.

This will help you practice **Mako templates, file I/O, command-line argument parsing, and basic class design** in Python.

---

## **Required Skills**

By completing this assignment, you will practice:

1. **Mako Templates** – Dynamically updating placeholders with values.
2. **Python Dependencies** – Adding and using third-party packages (like `mako`) in `pyproject.toml`.
3. **Command-line Arguments** – Using `argparse` to read input parameters.
4. **File Operations** – Reading, writing, and processing multiple files.
5. **Object-Oriented Programming** – Using classes, constructors (`__init__`), and methods.

---

## **Problem Statement**

Your module must:

1. **Accept command-line arguments**:

| Argument         | Description                                              |
| ---------------- | -------------------------------------------------------- |
| `--input_path`   | Path to the directory containing `.mako` template files  |
| `--output_path`  | Path to the directory where rendered files will be saved |
| `--phone_number` | Value to replace `INDIA_PHONE_NUMBER` in templates       |
| `--event_name`   | Value to replace `EVENT_NAME` in templates               |

2. **Process `.mako` files** in the input directory:

   * Ignore any non-Mako files
   * Replace placeholders in `.mako` files with the values from command-line arguments
   * Save the rendered files in the output directory **without the `.mako` extension**

3. **Handle directories**:

   * If the output directory does not exist, create it automatically

4. **Testing**:

   * Your implementation will be validated using a provided `pytest` file; you do not need to write tests.

---

## **Sample Input**

**Input Directory Structure:**

```
input/
├── cloud_orbit_event.mako
├── phonebook.mako
├── readme.txt   # Non-Mako file, should be ignored
```

**Content of `cloud_orbit_event.mako`:**

```
Event name ${EVENT_NAME}
Please call to ${INDIA_PHONE_NUMBER} to register for the events
```

**Content of `phonebook.mako`:**

```
Organization Location ,PhoneNumber
NI Austin,1 800-433-3488
NI Hungary,36 52 515 400
NI India,${INDIA_PHONE_NUMBER}
```

**Command-line execution:**

```bash
python MakoFileUpdator.py \
    --input_path input \
    --output_path output \
    --phone_number 12345 \
    --event_name python_book_club
```

---

## **Expected Output**

**Output Directory Structure:**

```
output/
├── cloud_orbit_event.txt
├── phonebook.txt
```

**Content of `cloud_orbit_event.txt`:**

```
Event name python_book_club
Please call to 12345 to register for the events
```

**Content of `phonebook.txt`:**

```
Organization Location ,PhoneNumber
NI Austin,1 800-433-3488
NI Hungary,36 52 515 400
NI India,12345
```

> Note: `readme.txt` from the input directory is ignored because it is not a `.mako` file.

---

## **Hints & Tips**

1. Use `os.listdir()` to iterate through files in the input directory.
2. Use the `mako.template.Template` class to render templates with placeholders.
3. Remove the `.mako` extension for output filenames using `str.split()` or `os.path.splitext()`.
4. Use `argparse.ArgumentParser()` to handle command-line arguments.
5. Check if the output directory exists using `os.path.exists()`; create it with `os.mkdir()` if it doesn’t exist.

---

## **Deliverables**

* `MakoFileUpdator.py` → completed Python module
* `.mako` template files for testing (students can create sample templates)

---
