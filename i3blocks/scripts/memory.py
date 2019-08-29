#! /usr/bin/env python3

import subprocess
import sys
import re

def err():
    print("ERR")
    sys.exit(33)

mem_total = subprocess.check_output(["sh", "-c", "cat /proc/meminfo | grep 'MemTotal'"]).decode("utf-8")
mem_free = subprocess.check_output(["sh", "-c", "cat /proc/meminfo | grep 'MemFree'"]).decode("utf-8")


def extract_number(s):
    match = re.search("\\d+", s)
    if match:
        return int(match.group(0))
    else:
        err()

# Original data is in kB here, I think this means they are working with the 
# metric system here
mem_total = extract_number(mem_total) / 1000000
mem_free = extract_number(mem_free) / 1000000
mem_used = mem_total - mem_free

print(f"MEM {mem_used:.1f}GB/{mem_total:.1f}GB")
if mem_used > 0.9 * mem_total:
    sys.exit(33)

