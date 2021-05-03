# Check out: https://realpython.com/intro-to-python-threading/.

import os
import sys
import threading
import time


def wait(waitTime=0):
    print("Starting...\n")
    time.sleep(waitTime)
    print("Finished.")
    return 0

def main():

    while True:

        waitTime = input("Enter a time in seconds (s), press Q/q to quit: ")

        if waitTime == 'q' or waitTime == 'Q':
            return 0

        x = threading.Thread(target=wait, args=[int(waitTime)], daemon=True)
        x.start()

        # wait for thread to finish.
        # x.join()

    return 0


if __name__ == "__main__":

    sys.exit(main())