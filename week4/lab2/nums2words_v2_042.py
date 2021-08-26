#!/usr/bin/env python3

import sys

nums = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
}

def main():
    for num in sys.stdin:
        line = ""
        numbers = num.strip().split()
        for c in numbers:
            if c in nums:
                line = line + nums[c] + " "
            else:
                line = line + "unknown" + " "
        print(line[:-1])

if __name__ == '__main__':
    main()
