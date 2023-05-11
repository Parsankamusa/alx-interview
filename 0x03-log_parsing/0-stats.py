#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """
import sys

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for i, line in enumerate(sys.stdin):      
        parts = line.strip().split()
        if len(parts) != 7:
            continue
       
        status_code = int(parts[5])
        file_size = int(parts[6])
        # Update the counters
        total_file_size += file_size
        status_code_counts[status_code] += 1
        if i > 0 and i % 10 == 0:
            print(f'Total file size: {total_file_size}')
            for code in sorted(status_code_counts.keys()):
                count = status_code_counts[code]
                if count > 0:
                    print(f'{code}: {count}')
            print('')
except KeyboardInterrupt:
    print(f'Total file size: {total_file_size}')
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        if count > 0:
            print(f'{code}: {count}')

