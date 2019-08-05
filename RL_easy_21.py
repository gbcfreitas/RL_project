# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:24:31 2019

@author: gbcfr
"""

import numpy as np
import random as rd
from step import step

terminal = np.full((1),False)

    
# Question 2
# Applying Monte-Carlo control
# No discounting

# Initialization        

pi = np.full((21,10),'hit')
pi[17:]='stick'

n0 = 100
ns = np.full((21,10),0)
nsa = np.full((21,10,2),0)
alpha = 0

Q = np.full((21,10,2),0)
V = np.full((21,10),0)
G = 0
r = 0

# Start



episodes = 1000

for i in range(episodes):

    sum_p = rd.randint(1,10)
    sum_d = rd.randint(1,10)
    s = [sum_p,sum_d]
    sp = [sum_p,sum_d]
    terminal = False
    G = 0
    
    while terminal == False:
        a = pi[s[0]-1,s[1]-1]
        ns[s[0]-1,s[1]-1] += 1
        s, sp, r, terminal = step(s,a,sp)

        if a == 'hit':
            nsa[s[0]-1,s[1]-1,0]+=1
            G += r
            alpha = 1/nsa[s[0]-1,s[1]-1,0]
            Q[s[0]-1,s[1]-1,0] += alpha*(G - Q[s[0]-1,s[1]-1,0])
        else:
            nsa[s[0]-1,s[1]-1,1]+=1
            G += r
            alpha = 1/nsa[s[0]-1,s[1]-1,1]
            Q[s[0]-1,s[1]-1,1] += alpha*(G - Q[s[0]-1,s[1]-1,1])
        
        s = sp[:]


    for i, a in np.ndenumerate(pi):
   
        epsilon = n0/(n0+ns[i[0],i[1]])
        if max(Q[i[0],i[1],0],Q[i[0],i[1],1])==Q[i[0],i[1],0]:
            a = 'hit'
        else:
            a = 'stick'
        
        pi_new = rd.choices(population=[rd.choice(['hit','stick']),a],weights=[epsilon, (1-epsilon)]) 
        pi[i] = pi_new[0]








