#!/usr/bin/python3
"""
Module for UTF-8 validation.
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing the data bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current UTF-8 character
    number_of_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        # Get the 8 least significant bits of the byte
        byte = byte & 0xFF

        if number_of_bytes == 0:
            # Count the number of leading 1s in the byte
            mask = 1 << 7
            while mask & byte:
                number_of_bytes += 1
                mask = mask >> 1

            # If the byte is a single-byte character (0xxxxxxx)
            if number_of_bytes == 0:
                continue

            # If the number of bytes is more than 4 or 1 (invalid cases)
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            # If this byte is not starting with 10xxxxxx, it's invalid
            if not (byte & mask1 and not (byte & mask2)):
                return False

        number_of_bytes -= 1

    # If there are leftover bytes to be processed, it's invalid
    return number_of_bytes == 0
