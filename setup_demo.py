#! /usr/bin/python3
import subprocess
from Aspidites import __version__
import math

major, minor, _ = map(int, __version__.split('.'))

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

    out = subprocess.check_output(['Aspidites', f'src/woma_demo{vstring}.wom', '-o', 'src/woma_demo.pyx', '-c'])
    print(out.decode('UTF-8'))


if __name__ == "__main__":
    main()
