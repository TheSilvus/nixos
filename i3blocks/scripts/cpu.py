#! /usr/bin/env python3

import subprocess
import sys

mpstat = subprocess.check_output(["mpstat", "1", "1"]).decode("utf-8")

cpu_line = mpstat.strip().split("\n")[-1]

idle = float(cpu_line.split(" ")[-1])
usage = 100 - idle

print(f"CPU {usage:.2f}%")
if usage > 90:
    sys.exit(33)
