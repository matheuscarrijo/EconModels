# -*- coding: utf-8 -*-

"""
@author: Matheus L. Carrijo

Objetivo do programa: implementar computacionalmente o modelo que descreve a 
competição de oligopólio com apenas duas empresas idênticas (duopólio) e com
apenas um período, chamado Modelo de Cournot. Cada empresa toma a decisão
de quanto produzir baseada na expectativa de produção da outra empresa, de 
maneira a maximizar o lucro. O equilíbrio de previsões é a situação em que cada 
empresa vê sua crença sobre a outra confirmada. Por simplicidade, também 
considero custos nulos. Depois, o modelo é ampliado para o caso com n empresas
"""

        ################################################################
        #                     Importando pacotes                       #
        ################################################################
        
import matplotlib.pyplot as plt #importing graph package
plt.figure(figsize=(10, 6), dpi=1000) #set default figure size
import numpy as np #importing numpy

        ################################################################
        #                       Definindo funções                      #
        ################################################################

def demanda_inversa(Y, a = 1000, b = 1): #preço em função da quantidade
    """
    Definindo a demanda inversa, que depende da produção total da economia e 
    dos parâmetros 'a' e 'b'. O parâmetro Y é uma lista em que a entrada i 
    representa a produção da empresa i.
    """
    
    assert a > 0 and b > 0, "Os parâmetros da demanda devem ser positivos"

    global c, d
    c, d = a, b 
    
    return a - b*(sum(Y))

def receita(y, Y):
    """
    Receita = preço*quantidade. No caso do oligopólio, o preço é dado pela 
    demanda inversa e a quantidade determinada pela firma.
    """
    
    return y*demanda_inversa(Y)

def curva_reacao():
    """
    Serve para o caso em que numero_firmas = 2. A função resolve o problema de
    maximização da firma arbitrária (1 ou 2) em função da produção que ela 
    espera da outra firma, ou seja, a função gera a curva de melhor resposta.
    O equiilibrio de Cournot será a intersecção entre ambas as curvas.
    """
    
    demanda_inversa([0,1]) # Chamo a função apenas para definir o parâmetro 'c' 
    
    # Resolvendo o problema para uma empresa arbitrária (empresa 1 ou 2): 
         
    receita_valores = [] 
    y_argmax = []
    y, y_e = np.linspace(0, c, c+1), np.linspace(0, c, c+1)
    
    for j in y_e:
        
        for i in y:
            
            receita_valores.append(receita(i, [i,j]))
        
        indice_max = np.argmax(receita_valores) # Guarda o índice da maior 
                                                # receita
        y_argmax.append(y[indice_max]) # Adiciona a uma lista o nível de  
                                       # produção y que maximiza o lucro                              
        receita_valores = [] # "zera" a lista de receita para o algoritmo 
                             # resolver novamente o problema de maximizacao de  
                             # lucro para outro nível de produção esperado
                          
    return y_e, y_argmax

def equilibrio_cournot(numero_firmas = 2):
    """
    Esta função serve para o caso geral em que numero_firmas = n. A solução é
    implementada algebricamente. As firmas são idênticas e o custo é nulo. O
    cálculo é realizado para o caso especial de demanda inversa linear.
    """
    
    coeficientes = np.array([[2 if j==i else 1 for i in range(numero_firmas)] 
                    for j in range(numero_firmas)])
    inversa_coeficientes = np.linalg.inv(coeficientes)
    
    constantes = np.array([c/d for i in range(numero_firmas)]) 

    vetor_producao = np.dot(inversa_coeficientes, constantes)
    
    return vetor_producao

        ################################################################
        #                   Programa principal                         #
        #                  (chamando as funções)                       #
        ################################################################
        
curva_de_reacao = curva_reacao()

equilibrio_cournot1 = equilibrio_cournot() # Para n=2 firmas

quantidade_equilibrio = sum(equilibrio_cournot1)
    
preco_equilibrio = demanda_inversa(equilibrio_cournot1)


     ########### Analisando o efeito do aumento de firmas #############

preco2 = [] 
quantidade2 = []
n_firmas = 100

for i in range(1, n_firmas + 1): # para cada numero de firmas, calcular as 
                                 # a quantidade e preço de equilíbrio da 
                                 # economia.
    
    equilibrio_cournot2 = equilibrio_cournot(i)
    quantidade2.append(sum(equilibrio_cournot2))
    preco2.append(demanda_inversa(equilibrio_cournot2))

        ################################################################
        #                    informando ao usuário                     #
        ################################################################

print("O preço e a quantidade de equilíbrio são dados respectivamente por:")
print(f"{quantidade_equilibrio: .2f} e {preco_equilibrio: .2f}")

        ################################################################
        #                         Gráficos                             #
        ################################################################

# Gráfico para o exemplo de 2 firmas (curvas de reacao):

fig1, ax1 = plt.subplots()        
ax1.plot(curva_de_reacao[1], curva_de_reacao[0], color="blue", linewidth=2.0, 
         ls = "dotted", label = "Curva de reação da empresa 1") 
ax1.plot(curva_de_reacao[0], curva_de_reacao[1], color="green", linewidth=2.0,
         ls = "dashed", label = "Curva de reação da empresa 2")
ax1.set_xlabel(r"Produção da empresa 1 ($y_1$)", fontsize = 15)
ax1.set_ylabel(r"Produção da empresa 2 ($y_2$)", fontsize = 15)
plt.scatter(equilibrio_cournot1[0], equilibrio_cournot1[1], s = 7*4**2, 
            label = "Equilíbrio de Cournot", color = "black")
plt.annotate(f"$(y_1^*, y_2^*) = ({c/3*d: .2f}, {c/3*d: .2f})$", 
             ((c/3*d)+15,(c/3*d)+30), fontsize = 13)
ax1.legend(fontsize = 12)
#fig1.savefig(r'C:\Python\lemc\Imagens\oligopolio_equilibrio_de_cournot.pdf')
plt.show() 

# Gráfico para a análise da entrada de firmas:

fig2, ax2 = plt.subplots()
ax2.plot(np.linspace(1, n_firmas, n_firmas), quantidade2, color="k", 
         linewidth=2.0, ls = "dashed", label = "Quantidade") 
ax2.plot(np.linspace(1, n_firmas+1, n_firmas), preco2, color="r", 
         linewidth=2.0, label = "Preço")
ax2.set_xlabel(r"Número de firmas", fontsize = 15)
ax2.legend(fontsize = 13) 
#fig2.savefig(r'C:\Python\lemc\Imagens\oligopolio_efeito_numero_firmas.pdf')
plt.show()

#Anotações:

# cursto marginal constante (serve para não constante?) pode ser implementado