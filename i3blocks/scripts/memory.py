#! /usr/bin/env python3

import subprocess
import sys
import re

def err():
    print("ERR")
    sys.exit(33)

free_mem = subprocess.check_output(["sh", "-c", "free | grep Mem"]).decode("utf-8")
free_swap = subprocess.check_output(["sh", "-c", "free | grep Swap"]).decode("utf-8")

def extract_numbers(s):
    return [int(match) for match in re.findall("\\d+", s)]


free_mem_numbers = extract_numbers(free_mem)
free_swap_numbers = extract_numbers(free_swap)

KIBI_TO_GIBI = 1024 * 1024

mem_total = free_mem_numbers[0] / KIBI_TO_GIBI
mem_available = free_mem_numbers[-1] / KIBI_TO_GIBI
swap_total = free_swap_numbers[0] / KIBI_TO_GIBI
swap_available = free_swap_numbers[-1] / KIBI_TO_GIBI

mem_used = mem_total - mem_available
swap_used = swap_total - swap_available


print(f"MEM {mem_used:.1f}/{mem_total:.1f}GB SWA {swap_used:.1f}/{swap_total:.1f}GB")
if mem_used > 0.9 * mem_total:
    sys.exit(33)

