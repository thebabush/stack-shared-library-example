#!/usr/bin/env python3

from __future__ import print_function

import ctypes
import os


def find(name):
    for root, dirs, files in os.walk('.'):
        if name in files:
            return os.path.join(root, name)


def main():
    soname = find('libhello.so')
    if soname is None:
        print("ERROR: Couldn't find libhello.so in .stack-work/")
        exit(0)

    so = ctypes.CDLL(soname)
    so.hello()


if __name__ == '__main__':
    main()
