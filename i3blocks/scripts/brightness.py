#! /usr/bin/env python3

import subprocess
import sys

light = subprocess.check_output(["light", "-r"]).decode("utf-8")

brightness = int(light)

brightness_level = round(brightness / 16)

print(f"BRI {brightness_level}/16")


