import importlib
import sys


if __name__ == '__main__':
    day = sys.argv[1]
    step = sys.argv[2]
    module = importlib.import_module(f'd{day}.s{step}')
    with open(f'd{day}/input.txt') as f:
        res = module.run(map(str.strip, f))
        print(res)
