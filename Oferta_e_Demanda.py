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
        
def demanda(p, a = -2, b = 7): 
    # Setting demand function (slope coefficient must be negative!)
    
    assert a < 0 and b > 0
    
    global a2, b2 # estabelece as variáveis como globais, isto é, elas são
                  # reconhecidas em todo o programa, não só dentro das funções
    a2, b2 = a, b
    
    return a*p + b

def oferta(p, c = 4, d = 1):
    # Setting supply function (slope coefficient must be posive!)
    # d in (0,b) é suficiente pra equilibrio
    
    assert c > 0 and d > 0 and b2 > d 
    
    global c2, d2
    c2, d2 = c, d
    
    return c*p + d
    
def excesso_demanda(p):
   # Setting excess demand function. It must be clear that equlibrium requires
   # excesso_demanda(p) = 0, for some especific p
   
   return demanda(p) - oferta(p)

        ################################################################
        #                    Programa principal                        #
        ################################################################

p_grid = np.linspace(-1000, 1000, 1000) 
q_grid = np.linspace(-1000, 1000, 1000)

E_abs = []
for i in p_grid:
    E_abs.append(abs(excesso_demanda(i)))
       
indice_min = E_abs.index(min(E_abs))
p_equilibrio = p_grid[indice_min]
q_equilibrio = oferta(p_equilibrio)

print(f"\nFaremos o cálculo para a função demanda D = {a2}p + {b2}", end = " ")
print(f"e oferta S = {c2}p + {d2}\n")
print("O preço e a quantidade de equilíbrio são", end = "") 
print(f", respectivamente,{p_equilibrio: .2f} e {q_equilibrio: .2f}")

        ################################################################
        #                         Gráfico                              #
        ################################################################
        
q1, q2, q3 = demanda(p_grid), oferta(p_grid), excesso_demanda(p_grid)
plt.plot(q1, p_grid, color="blue", linewidth=3.0 , ls = "dashed")
plt.plot(q2, p_grid, color="green", linewidth=3.0)
plt.plot(q3, p_grid, color="red", linewidth=3.0, ls = "dotted")
plt.xlim(d2, b2) 
plt.ylim(-d2/c2, (-b2) / a2)
plt.legend([f'Curva de Demanda: D = {a2}p + {b2}', 
            f'Curva de Oferta: S = {c2}p + {d2}', 
            'Curva do excesso de demanda: E = D - S'], fontsize = 13)
plt.ylabel("Preço", fontsize = 15)
plt.xlabel("Quantidade", fontsize = 15)
plt.savefig(r'C:\Python\lemc\Imagens\Ofeta_Demanda_Graph.pdf')
plt.show()
     
