#! /usr/bin/env python3

import subprocess



import os
import subprocess
import sys
import re

INTERFACE = "/var/run/wpa_supplicant/wlp4s0"

if not os.path.exists(INTERFACE):
    print("WIF DOWN")
    sys.exit(33)

def err():
    print("ERR")
    sys.exit(33)

wpa_cli = subprocess.check_output(["wpa_cli", "-g", INTERFACE, "status"]).decode("utf-8")


match = re.search("^ssid=(.*)", wpa_cli, flags=re.MULTILINE)
if match:
    ssid = match.group(1)

    match = re.search("^freq=(\d*)$", wpa_cli, flags=re.MULTILINE)
    if not match:
        err()
    frequency = int(match.group(1))
    
    
    print(f"WIF {ssid} ({frequency // 1000}.{frequency // 100 % 10}GHz)")
else:
    print("WIF DIS")
    sys.exit(33)
