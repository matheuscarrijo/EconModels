# -*- coding: utf-8 -*-
"""
@author: Matheus L. Carrijo
"""

        ################################################################
        #                     Importando pacotes                       #
        ################################################################
        
import matplotlib.pyplot as plt #importing graph package
plt.figure(figsize=(11, 6), dpi=100) #set default figure size 
import numpy as np 

        ################################################################
        #                       Definindo funções                      #
        ################################################################
        
def investimento(taxa_juros):
    """
    Dada a taxa de juros, calcula o nível de investimento. Deve ser 
    negativamente relacionada com a taxa de juros. Por simplicidade, 
    consideramos o caso linear.
    """
    
    if a < 0 and b > 0:
        return a*taxa_juros + b
    
def demanda_monetaria(taxa_juros, produto):
    """
    Modelamos a demanda monetária tentando incorporar linearmente os motivos 
    precaução, especulação, e transação, respectivamente pelas variáveis 
    e, c, d.
    """
    
    return c*produto + d*taxa_juros + e 

def consumo(produto):
    """
    Consideraremos o consumo como uma função linear da renda disponível, de
    modo que o coeficiente de inclinação é a propensão marginal a consumir e 
    a constante é o consumo autônomo.
    """
    
    return (propensao_marginal_a_consumir * (produto - aliquota_imposto) 
            + consumo_autonomo)

def produto_IS(taxa_juros):
    """
    Construímos a curva IS através da equação Y = C + I + G, em que C é a
    função consumo (que depende da renda disponível), I é o investimento, 
    dependente da taxa de juros, e G são os gastos do governo. Como o consumo
    depende do nível de renda, esta equação é manipulada até que tenhamos uma
    expressão do produto em relação à taxa de juros
    """
    
    I = investimento(taxa_juros)
    
    return ((consumo_autonomo + I + gastos_governo) / 
            (1 - propensao_marginal_a_consumir
            * (1 - aliquota_imposto)))


def produto_LM(taxa_juros):
    """
    Construímos a curva LM através da equação 
    oferta_monetaria = demanda_monetaria = c*produto + d*taxa_juros + e, 
    em que a oferta é exógena e a demanda calculada pela função. Então, a
    expressão pode ser manipulada até que tenhamos uma função de Y em função 
    da taxa de juros.
    """
    
    return ((oferta_monetaria/nivel_precos - e) / c - taxa_juros * (d / c))

def excesso_ISLM(taxa_juros):
    """
    Função para calcular o equilíbrio fazendo excesso_ISLM = 0, isto é, 
    o par (r*, Y*) ótimo que nos dá a intersecção entre as curvas IS e LM.
    """
    
    return produto_IS(taxa_juros) - produto_LM(taxa_juros)

        ################################################################
        #                   Programa principal                         #
        ################################################################
    
a, b, propensao_marginal_a_consumir, consumo_autonomo = -20, 5, 0.3, 100
gastos_governo, aliquota_imposto, c, d, e = 50, .2, 10, -300, 50
nivel_precos, oferta_monetaria = 10, 100

print("\nFaremos uma exemplo em que a função investimento é", end = " ")
print(f"dada por {a}r + {b};", end = " ")
print("a função demanda monetária, por", end = " ")
print(f"{c}Y + {d}i + {e};", end = " ")
print("a função consumo, por", end = " ")
print(f"{propensao_marginal_a_consumir}Y + {consumo_autonomo};", end = " ")
print(f"e a política fiscal por G = {gastos_governo} e", end = " ")
print(f"T = {aliquota_imposto}Y.", end = " ")
print("Ainda, a oferta monetária real é dada por M/P =", end = " ")
print(f"{oferta_monetaria/nivel_precos}.")


# Calculo do equilibrio 

taxa_juros_grid = np.linspace(0, 1000, 100000)

Excesso_abs = []

for i in taxa_juros_grid:
    
    Excesso_abs.append(abs(excesso_ISLM(i)))
       
indice_min = Excesso_abs.index(min(Excesso_abs))
juros_equilibrio = taxa_juros_grid[indice_min]
produto_equilibrio = produto_IS(juros_equilibrio)

print("\nPortanto, a taxa de juros e produto de equilíbrio são,", end = "") 
print(f" respect., {juros_equilibrio: .2f} e {produto_equilibrio: .2f}")

        ################################################################
        #                         Gráfico                              #
        ################################################################
        
valores_produto = []

for i in taxa_juros_grid:
    
    valores_produto.append(abs(produto_IS(i)))
    
y = taxa_juros_grid[np.argmin(valores_produto)]

# O código acima foi para saber a taxa de juros (no grid) que torna a curva IS
# nula. Isto será útil para determinar a escala do gráfico no eixo y (vertical)

# Gráficos: 
    
plt.plot(produto_IS(taxa_juros_grid), taxa_juros_grid, color="blue", 
         linewidth=3.0, ls = "dotted")
plt.plot(produto_LM(taxa_juros_grid), taxa_juros_grid, color="green", 
         linewidth=3.0, ls = "dashed")
plt.ylim(0, y) 
plt.xlim(min(produto_LM(taxa_juros_grid)), 
         max(produto_IS(taxa_juros_grid)))
plt.legend(['Curva IS', 'Curva LM'], fontsize = 15, loc = "upper center")
# plt.title("Modelo IS-LM", fontsize = 20)
plt.ylabel("Taxa de juros", fontsize = 15)
plt.xlabel("Produto, Y", fontsize = 15)
plt.savefig(r'C:\Python\lemc\Imagens\IS_LM.pdf')
plt.show()
    