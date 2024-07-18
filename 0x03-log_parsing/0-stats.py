#!/usr/bin/python3
import sys
import signal


def print_stats(total_size, status_codes):
    """Print the accumulated metrics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """Handle the keyboard interruption (CTRL + C)."""
    print_stats(total_size, status_codes)
    sys.exit(0)


# Initialize variables
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Setup signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Process each line from stdin
try:
    for line in sys.stdin:
        try:
            parts = line.split()
            if len(parts) < 7:
                continue

            # Extract the relevant parts of the log line
            file_size = int(parts[-1])
            status_code = int(parts[-2])

            # Update total file size
            total_size += file_size

            # Update status code counts if valid
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        except Exception:
            continue
finally:
    # Print final stats if there are remaining lines after the last batch of 10
    print_stats(total_size, status_codes)
