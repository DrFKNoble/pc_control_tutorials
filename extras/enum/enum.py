import os
import sys

from enum import Enum

class TEMP(Enum):
    HOT = 1
    TEMPERATE = 2
    COLD = 3


def main():
        
    feeling = TEMP.HOT

    if feeling == TEMP.HOT:
        print("I'm feeling hot")

    return 0


if __name__ == "__main__":

    sys.exit(main())