#!/usr/bin/python3
""" Log parsing
"""

import sys

def print_statistics(total_file_size, status_counts):
    print(f"Total file size: File size: {total_file_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_file_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            elements = line.split()
            
            if len(elements) < 7 or not elements[6].isdigit():
                # Skip the line if the format is incorrect or the file size is not an integer
                continue
            
            status_code = int(elements[5])
            file_size = int(elements[6])
            total_file_size += file_size

            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_counts)

    except KeyboardInterrupt:
        # Catch keyboard interruption (CTRL + C) and print the statistics before exiting
        print_statistics(total_file_size, status_counts)

if __name__ == "__main__":
    main()

