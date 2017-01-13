#!/usr/bin/env python3.4
import subprocess
import time
import sys

print("""
      [+] "on" to turn the lights on
      [+] "off" to turn them off!
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
