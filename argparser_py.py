# new_ resuserrection
#!/usr/bin/env python3.8

import sys 
from sys import stdin
import math
import argparse

# creacion de las variables  este tiempo en las cuales son bastante  diferentes en las cuales se llama al inicio del arg parser
# " this is teminit pasrser
def one(x):
    parter =  argparse.ArgumentParser()
    parter.add_argument(dest='argument1', help="thist is the first argument")
    parter.add_argument(dest='argument2', help="not found argument") 
    test_fuck = parter.parse_args()
    print(test_fuck.argument1)
    print(test_fuck.argument2)

if __name__ == '__main__':
    one(sys.argv[1])