#!/usr/bin/python3
"""
Log parsing script
"""
import sys
import re


ip_r = r'(\d{1,3}\.){3}\d{1,3}'
date_r = r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{6}'
method_r = r'"GET /projects/260 HTTP/1\.1"'
status_code_r = r' \d{3} '
file_size_r = r'\d{1,4}\n'
regex = r'{} - \[{}\] {}{}{}'.format(ip_r, date_r,
                                     method_r, status_code_r,
                                     file_size_r)


def log(codes_list, total_size):
    """ Logs output """
    codes_list.sort()
    print("File size: {}".format(total_size), flush=True)
    for code in set(codes_list):
        print("{}: {}".format(code, codes_list.count(code)), flush=True)


if __name__ == "__main__":
    codes_list = []
    total_size = 0
    count = 0
    try:
        for line in sys.stdin:
            count += 1
            searched_line = re.search(regex, line)
            if searched_line:
                try:
                    status_code = int(re.search(status_code_r, line).group())
                    file_size = int(re.search(file_size_r, line).group())
                    codes_list.append(status_code)
                    total_size += file_size
                except Exception:
                    pass
                if count != 0 and count % 10 == 0:
                    log(codes_list, total_size)
            else:
                pass
    except (KeyboardInterrupt, EOFError):
        log(codes_list, total_size)
