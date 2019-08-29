#! /usr/bin/env python3

import os
import subprocess
import sys
import re

def err():
    print("ERR")
    sys.exit(33)

acpi = subprocess.check_output("acpi").decode("utf-8")

match = re.search("(\\d{1,3})%", acpi)
if match:
    percentage = int(match.group(1))
else:
    err()


if "Discharging" in acpi:
    state = "DIS"
elif percentage == 100:
    state = "FUL"
elif "Charging" in acpi:
    state = "CHA"
else:
    err()

match = re.search("(\d\d:\d\d:\d\d)", acpi)
if match:
    time = match.group(1)
else:
    time = None

if time:
    print(f"BAT {percentage}% {state} {time}")
else:
    print(f"BAT {percentage}% {state}")

if percentage < 20:
    sys.exit(33)
