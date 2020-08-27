#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    i = 1
    
    #This is the for-loop method
    for i in range(1,11):
        result = n * i
        print(str(n) + ' x ' + str(i) + ' = ' + str(result))
        i+=1
        
    #This is the while loop method
    #while i <= 10:
    #    result = n * i
    #    print(str(n) + ' x ' + str(i) + ' = ' + str(result))
    #    i += 1
