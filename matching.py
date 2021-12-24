# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 01:13:44 2021

@author: mathe
"""

# Tipos de homens e mulheres:
H = [0, 1, 2]
M = [3, 4, 5]

"""As linhas de 0 a 2 na lista abaixo diz respeito aos homens; de 3 a 5, às
mulheres. As colunas são as preferências em ordem decrescente."""
preferencias = [[3, 5, 4], [5, 4, 3], [5, 3, 4],
                [2, 1, 0], [0, 2, 1], [1, 2, 0]]

"""Conjunto dos casais formados a cada rodada. Dimensão: 3x2 (numero de casais
X tipos de pessoas"""
casais = []
N = 3 #cardinalidade dos conjuntos M e H
""" A função propostas recebe um valor de um homem, h, e o número da
rodada, n, e retorna a proposta, que será sempre aquela mulher na n-ésima 
posição das preferências dos homens"""
def propostas(h, n):
    assert h in range (0,3)
    assert n < 4 and n > 0
    return preferencias[h][n]

def aceitacao(h, n):
    assert h in range (0,3)
    #assert m in range (3,6)
    assert n < 4 and n > 0
    casada = False
    m_pretendida = propostas(h, n)
    for i in range(len(casais)):
        if m_pretendida == casais[i][2]:
            casada = True
    if casada:
        

def main():
    
           
            