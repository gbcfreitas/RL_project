# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:24:31 2019

@author: gbcfr
"""

from random import randint
from random import choice
import numpy as np



# Defining the step function

def step(s,a):
    
    if a == 'hit':
        p_draw = [randint(1,10),choice(['black','red'])]
        if p_draw[1]=='black':
            s[0] += p_draw[0]
        else:
            s[0] -+ p_draw[0]
    else:# a = 'stick'
        while s[1] < 17:
            d_draw = [randint(1,10),choice(['black','red'])]
            if d_draw[1]=='black':
                s[1] += d_draw[0]
            else:
                s[1] -= d_draw[0]
        else:
            return
    
    return s,a

#Start

sum_p = randint(1,10)
sum_d = randint(1,10)

# policy pi and action-value function q

pi = np.full((10,21),'hit')
pi[:,17:]='stick'
q = np.full((10,21),0)
# Current state
s = [sum_p,sum_d]
a = pi[sum_d-1,sum_p-1]

step(s,a)
while a == 'hit':
    step(s,a)
       
if s[0] > 21 or s[0] < 1:
    r = -1
elif s[1] > 21 or s[1] < 1:
    r = +1
elif s[0] == s[1]:
    r = 0
elif s[0] > s[1]:
    r = +1
elif s[1] > s[0]:
    r = -1

q(s,a)= r+=  
  #  return r





