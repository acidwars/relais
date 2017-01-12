#!/usr/bin/env python3.4
import subprocess
import time
import sys

print("""
      [+] 1 for turning the light on
      [+] 0 for turning it off!
      """)
if sys.argv[1] == "1":
    subprocess.call(["./relais", "on"], shell=False)

elif sys.argv[1] == "0":
    subprocess.call(["./relais", "off"], shell=False)

else:
    try:
        while True:
            answer = str(input(">> "))
            if answer == "1":
                subprocess.call(["./relais", "on"], shell=False)
            elif answer == "0":
                subprocess.call(["./relais", "off"], shell=False)
            else:
                print("Not allowed!")

    except KeyboardInterrupt:
        print("Interrupted")
