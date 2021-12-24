# -*- coding: utf-8 -*-
"""
@author: Matheus L. Carrijo
"""
        ################################################################
        #                     Importando pacotes                       #
        ################################################################
        
import matplotlib.pyplot as plt #importing graph package
plt.figure(figsize=(11, 6), dpi=100) #set default figure size 
import numpy as np #importing numpy

        ################################################################
        #                       Definindo funções                      #
        ################################################################
        
# Set the Cobb-Douglas production function:
def produto_agregado(k_agregado, l_agregado = 1):
    return np.sqrt(k_agregado*l_agregado)

# Set the Cobb-Douglas production function per worker:
def produto_por_trabalhador(k_agregado, l_agregado = 1):
    return produto_agregado(k_agregado)/l_agregado

# Depreciation is a linear function of k per worker, i.e., k=K/L
def depreciacao(k_agregado, l_agregado = 1, taxa_depreciacao = 0.1):
    return taxa_depreciacao*(k_agregado/l_agregado)

def investimento(k_agregado, taxa_poupanca = 0.3):
    return taxa_poupanca*produto_por_trabalhador(k_agregado)

def consumo(k_agregado, taxa_poupanca = 0.3):
    return (1 - taxa_poupanca)*produto_por_trabalhador(k_agregado)

def k_variacao(k_agregado, taxa_poupanca = 0.3):
    return (taxa_poupanca*produto_por_trabalhador(k_agregado)
            - depreciacao(k_agregado))

        ################################################################
        #                   Programa principal                         #
        ################################################################
        
taxa_depreciacao, taxa_poupanca, l_agregado, k_t0 = 0.1, 0.3, 1, 4
       
print("Faremos uma exemplo em que a taxa de poupança é", end = " ")
print(f"{taxa_poupanca}%, a taxa de depreciação é", end = " ")
print(f"{taxa_depreciacao}%, e que a economia comece com uma", end = " ")
print("relação de 4 capital por trabalhador")

tolerancia = 0.001
norma = 10 # número apenas para entrar no While
while norma > tolerancia:
    k_t1 = (taxa_poupanca*produto_por_trabalhador(k_t0) + 
            k_t0*(1-taxa_depreciacao))
    norma = abs(k_t1 - k_t0)
    k_t0 = k_t1
    
        ################################################################
        #                    informando ao usuário                     #
        ################################################################
    
print(f"O produto de equilibrio é k* = {k_t1: .4}")

        ################################################################
        #                         Gráficos                             #
        ################################################################

k_grid = np.linspace(0, 2*k_t1, 1000)

plt.plot(k_grid, depreciacao(k_grid), color="blue", linewidth=3.0, 
         ls = "dashed")
plt.plot(k_grid, investimento(k_grid), color="green", linewidth=3.0)
plt.xlim(0, 2*k_t1) # entre -5 e 5 por exemplo
plt.ylim(0, 2*investimento(k_t1))
plt.legend([f'Depreciação, {taxa_depreciacao}k', 
            f'Investimento, {taxa_poupanca}f(k)'], fontsize = 14)
plt.ylabel("Investimento e Depreciação", fontsize = 15)
plt.xlabel("Capital por trabalhador, k", fontsize = 15)
plt.savefig(r'C:\Python\lemc\Imagens\Crescimento_Economico_graph.pdf')
plt.show()
 
