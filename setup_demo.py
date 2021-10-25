#! /usr/bin/python3
import os
import math
import Aspidites

major, minor, _ = map(int, Aspidites.__version__.split('.'))

if major == 0:
    major_pad = 1
else:
    major_pad = (int(math.log(major, 10)) + 2)

if minor == 0:
    minor_pad = 1
else:
    minor_pad = (int(math.log(major, 10)) + 2)

vstring = '_' + str(major).rjust(major_pad, '0') + str(minor).rjust(minor_pad, '0') + '00'


def main():
    c = f'Aspidites src/woma_demo{vstring}.wom -o src/woma_demo.pyx -c'
    with os.popen(c) as p:
        chunk = p.read(8)
        while chunk:
            print(chunk, sep='', end='')
            chunk = p.read(8)


if __name__ == "__main__":
    main()
