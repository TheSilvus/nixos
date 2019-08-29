#! /usr/bin/env python3

import subprocess
import sys
import re

def err():
    print("ERR")
    sys.exit(33)

amixer = subprocess.check_output(["sh", "-c", "amixer | head -n 7"]).decode("utf-8")


def extract_number(s):
    match = re.search("\\d+", s)
    if match:
        return int(match.group(0))
    else:
        err()

match = re.search("\\[(\\d{1,3})\\%]", amixer)
if match:
    percentage = int(match.group(1))
else:
    err()

if "[on]" in amixer:
    muted = False
elif "[off]" in amixer:
    muted = True
else:
    err()


if not muted:
    print(f"VOL {percentage}%")
else:
    print(f"VOL MUT")
