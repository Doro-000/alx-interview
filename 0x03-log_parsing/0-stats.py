#!/usr/bin/python3
"""
log parsing
"""

import sys
import re

regex = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')  # nopep8


def log_parse() -> None:
    """
    parses a log file
    """
    line_count: int = 0
    log: dict = {}
    log["file_size"] = 0
    log["code_frequency"] = {
        str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500]}
    try:
        for line in sys.stdin:
            match = regex.fullmatch(line.strip())
            if (match):
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # File size
                log["file_size"] += file_size

                # status code
                log["code_frequency"][code] += 1

                if (line_count % 10 == 0):
                    output(log)
    except KeyboardInterrupt:
        output(log)


def output(log: dict) -> None:
    """
    helper function to display stats
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    log_parse()
