# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 18:54:59 2019

@author: Dell
"""

# Step function

import random as rd

def step(s,a,sp):
    
    
    if a == 'hit':
        p_draw = [rd.randint(1,10),rd.choices(['black','red'],[(2/3),(1/3)])]
        color = p_draw[1]
        if color == ['black']:
            sp[0] += p_draw[0]
        else:
            sp[0] -= p_draw[0]
            
        if (sp[0]>21) | (sp[0]<1) :
            r = -1
            terminal = True
        else:
            terminal = False
            r=0
        
        return s, sp, r, terminal
    else:       
        while sp[1] < 17:
            d_draw = [rd.randint(1,10),rd.choices(['black','red'],[(2/3),(1/3)])]
            color = d_draw[1]
            if color == ['black']:
                sp[1] += d_draw[0]
            else:
                sp[1] -= d_draw[0]
        
        
        if sp[1] > 21 or sp[1] < 1:
            r = +1
        elif sp[0] == sp[1]:
            r = 0
        elif sp[0] > sp[1]:
            r = +1
        elif sp[1] > sp[0]:
            r = -1
                
        terminal = True
        return s, sp, r, terminal
    


