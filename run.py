#!/usr/bin/env python

import importlib
import sys


if __name__ == '__main__':
    day = sys.argv[1]
    part = sys.argv[2]
    module = importlib.import_module(f'd{day}.p{part}')
    with open(f'd{day}/input.txt') as f:
        res = module.run(map(str.strip, f))
        print(res)
