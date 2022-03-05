# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:11:32 2022

@author: hmdebern
"""

# https://codeworld19.blogspot.com/2020/08/time-delta-in-python-hacker-rank.html

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    return str(int(abs((t1-t2).total_seconds())))
    
    
t1='Sun 10 May 2015 13:54:36 -0700'
t2='Sun 10 May 2015 13:54:36 -0000'

print(time_delta(t1, t2) )
    
# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input())

#     for t_itr in range(t):
#         t1 = input()

#         t2 = input()

#         delta = time_delta(t1, t2)

#         fptr.write(delta + '\n')

#     fptr.close()
    
    