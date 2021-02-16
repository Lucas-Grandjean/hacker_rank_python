#!/bin/python3

import math
import os
import random
import re
import sys

def is_weird(number):
    if(number % 2 == 1):
        return 'Weird'
    elif(number >= 2 and number <= 5):
        return 'Not Weird'
    elif(number >= 6 and number <= 20):
        return 'Weird'
    elif(number > 20):
        return 'Not Weird'

if __name__ == '__main__':
    n = int(input().strip())
    print(is_weird(n))
        