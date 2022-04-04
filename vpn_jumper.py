#!/usr/bin/env python3

import os
from time import sleep
import random

codeList = ["TR", "US", "DE", "NL", "CH", "CA-W", "GB"]

try:
  os.system("windscribe connect")
  while True:
    codeChoice = random.choice(codeList)
    sleep(random.randrange(12,30))
    print("#Changing the IP Address...")
    os.system("windscribe connect " + codeChoice)

except:
  os.system("windscribe disconnect")
  print("Error occured")
