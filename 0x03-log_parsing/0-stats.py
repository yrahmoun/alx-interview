#!/usr/bin/python3
"""module for task 0"""
import sys


def print_stats(file_size, status_codes):
    """Print stats"""
    print("File size: {}".format(file_size))
    codes_sorted = sorted(status_codes.keys())
    for code in codes_sorted:
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


codes_count = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
file_size_total = 0
count = 0

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            try:
                status_code = line.split()[-2]
                if status_code in codes_count.keys():
                    codes_count[status_code] += 1
                file_size = int(line.split()[-1])
                file_size_total += file_size
            except Exception:
                pass
            count += 1
            if count == 10:
                print_stats(file_size_total, codes_count)
                count = 0
    except KeyboardInterrupt:
        print_stats(file_size_total, codes_count)
        raise
    print_stats(file_size_total, codes_count)
