# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 13:39:49 2021

@author: Usuario
"""
import numpy as np

alfa = .1
beta = .4
gama = .3

d1 = 5
d2 = 8
d3 = 0

vetor_constante = [[d1],
                   [d2],
                   [d3]]

vetor_array = np.array(vetor_constante)

print(vetor_array)

print(vetor_constante)

matriz = [[(1 - alfa),  0,          0],
          [0,           (1 - beta), 0],
          [0,           0,          (1 - gama)]]

matriz_array = np.array(matriz)

print(matriz_array)

print(matriz)

matriz_inversa = np.linalg.inv(matriz_array)


print('matriz\n', matriz_inversa)

vetor_solucao = np.dot(matriz_inversa, vetor_array)

print(vetor_solucao)







