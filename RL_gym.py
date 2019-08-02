# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 19:57:20 2019

@author: gbcfr
"""

import numpy as np

nan = np.nan # representa ações impossíveis
T = np.array([ # shape=[s, a, s']
        [[0.7, 0.3, 0.0], [1.0, 0.0, 0.0], [0.8, 0.2, 0.0]],
        [[0.0, 1.0, 0.0], [nan, nan, nan], [0.0, 0.0, 1.0]],
        [[nan, nan, nan], [0.8, 0.1, 0.1], [nan, nan, nan]]
        ])
R = np.array([ # shape=[s, a, s']
        [[10., 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]],
        [[0.0, 0.0, 0.0], [nan, nan, nan], [0.0, 0.0, -50.]],
        [[nan, nan, nan], [40., 0.0, 0.0], [nan, nan, nan]]
        ])        

possible_actions = [[0, 1, 2], [0, 2], [1]]

Q = np.full((3, 3), -np.inf) # -inf para ações impossiveis
for state, actions in enumerate(possible_actions):
    Q[state, actions] = 0.0 # Valor inicial = 0.0 para todas as ações possíveis
    
discount_rate = 0.95
n_iterations = 100

for iteration in range(n_iterations):
    Q_prev = Q.copy()
    for s in range(3):
        for a in possible_actions:
            Q[s,a] = np.sum([
                    T[s, a, sp] * (R[s, a, sp] + discount_rate * np.max(Q_prev[sp]))
                    for sp in range(3)
                    ])