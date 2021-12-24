# -*- coding: utf-8 -*-
"""
@author: Matheus L. Carrijo
"""

        ################################################################
        #                     Importando pacotes                       #
        ################################################################
        
import matplotlib.pyplot as plt #importing graph package
plt.figure(figsize=(11, 6), dpi=1000) #set default figure size 
import numpy as np

        ################################################################
        #                          Funções                             #
        ################################################################
    
def utilidade(c_estado_b, c_estado_g, prob_estado_b, prob_estado_g):
    
    return prob_estado_b*np.log(c_estado_b) + prob_estado_g*np.log(c_estado_g)

def restr_orcamentaria(c_estado_b, gamma, dot_estado_b, dot_estado_g):
    
    b = dot_estado_g + dot_estado_b*gamma/(1-gamma)
    
    return b - (gamma*c_estado_b)/(1-gamma)

def escolha(dot_estado_b, dot_estado_g, prob_estado_b, prob_estado_g, gamma):
    
    b = dot_estado_g + dot_estado_b*gamma/(1-gamma)
    c = prob_estado_g/prob_estado_b
    
    c_b_estrela = b*prob_estado_b*(1-gamma)/gamma
    c_g_estrela = c_b_estrela*c*(gamma/(1-gamma))      
    funcao_valor = utilidade(c_b_estrela, c_g_estrela, prob_estado_b, 
                             prob_estado_g)  
                                             
    return c_b_estrela, c_g_estrela, funcao_valor

def seguro_otimo(dot_estado_b, dot_estado_g, prob_estado_b, prob_estado_g, 
                 gamma):
    
    escolha_otima = escolha(dot_estado_b, dot_estado_g, prob_estado_b, 
                            prob_estado_g, gamma)
    
    return (dot_estado_g - escolha_otima[1]) / gamma

        ################################################################
        #                          Exemplo                             #
        ################################################################
    
dot_estado_b1, dot_estado_g1 = 250, 350
gamma_1 = 0.4
prob_estado_b1, prob_estado_g1 = 0.4, 0.60
        
exemplo_1 = escolha(dot_estado_b1, dot_estado_g1, prob_estado_b1, 
                    prob_estado_g1, gamma_1)

seguro_estrela = seguro_otimo(dot_estado_b1, dot_estado_g1, prob_estado_b1, 
                    prob_estado_g1, gamma_1)

        ################################################################
        #                   Informando ao usuário                      #
        ################################################################
        
print(f"\nCom dotação ({dot_estado_b1}, {dot_estado_g1});", end = " ") 
print("distribuição de probabilidade dada por", end = " ")       
print(f"({prob_estado_b1*100}%,{prob_estado_g1*100}%),", end = " ")
print(f"e premio {gamma_1*100}%, a distribuicao de consumo ótimo", end = " ")
print(f"será c_b = {exemplo_1[0]: .1f} e c_g = {exemplo_1[1]: .1f}.")
print(f"Ainda, a quantidade de seguro ótima é {seguro_estrela: .1f}.")

        ################################################################
        #                          Gráfico                             #
        ################################################################
    
c_estado_b1 = np.linspace(0.01, 1000, 1000)
c_estado_g1 = np.linspace(0.01, 1000, 1000)
orcamento = restr_orcamentaria(c_estado_b1, gamma_1, dot_estado_b1, 
                               dot_estado_g1) 
X, Y = np.meshgrid(c_estado_b1, c_estado_g1)

Z = plt.contour(X, Y, utilidade(X, Y, prob_estado_b1, prob_estado_g1), 
                levels = [exemplo_1[2]-10, exemplo_1[2], exemplo_1[2]+10], 
                linewidths = 2)
plt.plot(c_estado_b1, orcamento, color = "black", lw = 2, 
         label = "restrição orçamentária")
plt.clabel(Z, inline = 1, fontsize = 10)
plt.ylim(0, dot_estado_g1 + dot_estado_b1*gamma_1/(1-gamma_1))
plt.xlim(0, (1-gamma_1)*(dot_estado_g1 + dot_estado_b1*gamma_1/(1-gamma_1))
         /gamma_1)
plt.ylabel(r"Consumo no estado bom ($c_g$)", fontsize = 15)
plt.xlabel(r"Consumo no estado ruim ($c_b$)", fontsize = 15)
plt.scatter([exemplo_1[0]], [exemplo_1[1]], s = 7*4**2)
plt.annotate(f"$(c_b^*, c_g^*) = ({exemplo_1[0]: .0f}, {exemplo_1[1]: .0f})$", 
             (exemplo_1[0]+10, exemplo_1[1]+10), fontsize = 15)
plt.scatter([dot_estado_b1],[dot_estado_g1], s = 7*4**2, 
            label = f"dotação inicial = $({dot_estado_b1},{dot_estado_g1})$")
plt.annotate("A", (dot_estado_b1-15,dot_estado_g1-30), fontsize = 15)
plt.legend(fontsize = 14)
plt.savefig(r'C:\Python\lemc\Imagens\Escolha_sob_incerteza.pdf')
plt.show()
