0x04. UTF-8 Validation
Algorithm
Python

## Description

This project involves writing a method in Python that determines if a given dataset represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding used for electronic communication. The task is to ensure the provided data conforms to the UTF-8 encoding scheme.

## Concepts Covered

- **Bitwise Operations in Python**: Understanding how to manipulate bits using operations like AND (`&`), OR (`|`), XOR (`^`), NOT (`~`), and bit shifts (`<<`, `>>`).
- **UTF-8 Encoding Scheme**: Familiarity with how characters are encoded into 1 to 4 bytes.
- **Data Representation**: Working with data at the byte level and handling the least significant bits of integers.
- **List Manipulation in Python**: Iterating through lists, accessing list elements, and using list comprehensions.
- **Boolean Logic**: Applying logical operations to make decisions in the program.

## Requirements

- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- Code should follow the PEP 8 style (version 1.7.x).
- All files must be executable.

## Files

- `0-validate_utf8.py`: Contains the `validUTF8` function that checks if a dataset is a valid UTF-8 encoding.

## Usage

The `validUTF8` function takes a list of integers and returns `True` if the data represents a valid UTF-8 encoding, otherwise `False`.

### Function Prototype

```python
def validUTF8(data):
