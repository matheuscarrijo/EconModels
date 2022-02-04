# -*- coding: utf-8 -*-
"""
@author: Matheus Lopes Carrijo
"""

        ################################################################
        #                     Importando pacotes                       #
        ################################################################
        
import numpy as np
import matplotlib.pyplot as plt

        ################################################################
        #                     Definindo funções                        #
        ################################################################

utilidade = lambda consumo, lazer: (consumo**(alpha))*(lazer**(1-alpha))    
producao = lambda trabalho: trabalho**(0.5)
producao_com_lazer = lambda lazer: (1-lazer)**(0.5)
reta_orcamentaria = lambda lazer: (salario_equilibrio + 
                                   lucro_estrela(salario_equilibrio) - 
                                   salario_equilibrio*lazer)    
lucro = lambda salario, trabalho: producao(trabalho) - salario*trabalho

# Funções que surgem do problema da firma:
lucro_estrela = lambda salario: 1/(4*salario)
demanda_trab = lambda salario: 1/(4*(salario**2))
oferta_bem_x = lambda salario: 1/(2*salario)

# Funções que surgem do problema do consumidor:
demanda_bem_x = lambda salario: alpha*(4*(salario**2) + 1)/(4*salario)
demanda_lazer = lambda salario: (1-alpha)*(1 + 1/(4*(salario**2)))
oferta_trab = lambda salario: 1 - demanda_lazer(salario)

# Excesso de demanda:
excesso_demanda_trab = lambda salario: demanda_trab(salario) - \
                                       oferta_trab(salario) 
    
def equilibrio(w_alto = 100, w_baixo = 0):
    
    tol = 1e-10
    
    # Analisando fronteiras
    if abs(excesso_demanda_trab(w_alto)) < tol:
        
        return w_alto
    
    if abs(excesso_demanda_trab(w_alto)) < tol:
        
        return w_baixo
    
    w_aux = (w_alto + w_baixo)/2 # atualiza preco pela média
    
    # Algoritmo da bissecção para encontrar o zero da função 
    # excesso_demanda_trab
    while abs(excesso_demanda_trab(w_aux)) > tol:
        
        if excesso_demanda_trab(w_aux) > 0:
            
            w_baixo = w_aux
            
        if excesso_demanda_trab(w_aux) < 0:
            
            w_alto = w_aux
            
        w_aux = (w_alto + w_baixo)/2
        
    return w_aux


        ################################################################
        #                    Programa principal                        #
        ################################################################
    
alpha = 0.7 # único parâmetro necessário 

salario_equilibrio = equilibrio()
q_equilibrio_bem_x = demanda_bem_x(salario_equilibrio)
q_equilibrio_trab = demanda_trab(salario_equilibrio)
q_equilibrio_lazer = 1 - q_equilibrio_trab

        ################################################################
        #                         Gráfico                              #
        ################################################################

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["lines.linewidth"] = (2.5)

fig, ax = plt.subplots(tight_layout = True)  

# Grid para quantidades de consumo do bem x e lazer
bem_x = np.linspace(0, 1, 100)
lazer = np.linspace(0, 1, 100)

# Cria o produto cartesiano das quantidades x_1 e x_2.
l, x = np.meshgrid(lazer, bem_x)

# Coloca label nos eixos originais
ax.set_xlabel('$Lazer$', fontsize = 20)
ax.set_ylabel('Consumo', fontsize = 20)

#ax.axis([0, 1.02, 0, 1.05])
ax.axis([0, 1, 0, 1])

# Criamos um novo eixo x (apenas para repetir os ticks e labels do eixo x 
#                         original)
ax3 = ax.twiny()

# Copiamos os limites do eixo x original
orig_xlim = ax.get_xlim()

# Replicamos os limites do eixo x original no novo eixo
ax3.set_xlim(orig_xlim)

# Definimos um label para o novo eixo x
ax3.set_xlabel('$Trabalho$', fontsize = 20)

# Invertemos o sentido do texto do eixo x original
ax3.invert_xaxis()

uA = utilidade(x, l)
u = utilidade(q_equilibrio_bem_x, q_equilibrio_lazer)
CS1 = ax.contour(l, x, uA, levels = [u], colors = 'black', alpha = 1, 
                 extend = 'both', label = "Curva de indiferença")

fmt = {}
strs = ['utilidade']
for l, s in zip(CS1.levels, strs):
    fmt[l] = s
plt.clabel(CS1, inline = 1, fmt = fmt, fontsize = 14)

# Reta orçamentária:
ax.plot(lazer, reta_orcamentaria(lazer), 'blue', linewidth = 2, alpha = 1,
        label = 'Restrição orçamentária', ls = 'dotted')

# Função de produção:
    
lazer = np.linspace(0, 1, 100)
ax.plot(lazer, producao_com_lazer(lazer), 'green', linewidth = 2, 
        alpha = 1, label = 'Curva de produção')

#Alocação de equilíbrio:
ax.scatter(q_equilibrio_lazer, q_equilibrio_bem_x, s = 8*5**2, alpha = 1, 
           c = "r", 
           label = f"Alocação de equilíbrio: ({q_equilibrio_lazer:.2}, {q_equilibrio_bem_x:.2})")

ax.legend(loc = "lower left", fancybox = True, shadow = True, fontsize = 14)

#plt.savefig(r'C:\Python\lemc\Imagens\Equilibrio-geral.pdf')
plt.show()

