#! /usr/bin/env python3

from datetime import datetime

now = datetime.now()
seconds = (now - now.replace(hour=0, minute=0, second=0, microsecond=0)).total_seconds()

decimal_seconds = seconds * (100000 / (60*60*24))

print(f"DEC {decimal_seconds // 10000:.0f}:{decimal_seconds // 100 % 100:02.0f}:{decimal_seconds % 100:02.0f}")



