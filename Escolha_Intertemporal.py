# -*- coding: utf-8 -*-
"""
@author: Matheus L. Carrijo
"""

        ################################################################
        #                     Importando pacotes                       #
        ################################################################
        
import matplotlib.pyplot as plt #importing graph package
plt.figure(figsize=(10, 6), dpi=1000) #set default figure size 
import numpy as np

        ################################################################
        #                          Funções                             #
        ################################################################
        
def u(c, a):
    if a > 0 and a != 1:
        return (c**(1-a) - 1) / (1 - a)
    else:
        if a == 1:
            return np.log(c)

def U(c1, c2, a, b):
    return u(c1, a) + u(c2, b)

def budget(c1, m1, m2, r):
    if m1 > 0 and m2 > 0 and r > 0 and r < 1:    
        return (1+r)*m1 + m2 - (1+r)*c1
    
def inverse_budget(c2, m1, m2, r):
    if m1 > 0 and m2 > 0 and r > 0 and r < 1:    
        return (m2-c2)/(1+r) + m1

def choice(a, b, r, m1, m2):
    if (a > 0 and a != 1 and b > 0 and b != 1 and m1 > 0 and m2 > 0 and r > 0 
        and r < 1):
        c1_estrela = (m1+m2/(1+r)) / (1+(1+r)**((1-a)/a))
        c2_estrela = (m1 - c1_estrela)*(1+r) + m2 
        funcao_valor = U(c1_estrela, c2_estrela, a, b)

    return c1_estrela, c2_estrela, funcao_valor

        ################################################################
        #                          Exemplo                             #
        ################################################################
        
a, b, r, m1, m2 = 0.5, 0.5, 0.5, 50, 750
exemplo1 = choice(a, b, r, m1, m2)

        ################################################################
        #                   Informando ao usuário                      #
        ################################################################
        
print(f"\nCom uma taxa de juros de {100*r}%, renda em t1 de {m1}", end = " ")        
print(f"e renda {m2} em t2, a distribuição de consumo no tempo que", end = " ")
print("maximiza a utilidade do agente é dada por", end = " ")
print(f'(c1, c2) = ({exemplo1[0]}, {exemplo1[1]}), com nível de', end = " ")
print(f"utilidade dado por U = {exemplo1[2]}")
        
        ################################################################
        #                          Gráfico                             #
        ################################################################

eixo_x, eixo_y = np.linspace(0, 1000, 1000), np.linspace(0, 1000, 1000)
budget1 = budget(eixo_x, m1, m2, r)
X, Y = np.meshgrid(eixo_x, eixo_y)

Z = plt.contour(X, Y, U(X, Y, a, b), 
                levels = [exemplo1[2]-10, exemplo1[2], exemplo1[2]+10], 
                linewidths = 2)
plt.plot(eixo_x, budget1, color = "black", lw = 2, 
         label = "restrição orçamentária")
plt.clabel(Z, inline = 1, fontsize = 10)
plt.ylim(0, (1+r)*m1 + m2)
plt.xlim(0, m1 + m2/(1+r))
plt.ylabel(r"Consumo em $t_2$", fontsize = 14)
plt.xlabel(r"Consumo em $t_1$", fontsize = 14)
plt.scatter([exemplo1[0]], [exemplo1[1]], s = 7*4**2)
plt.annotate(f"$(c_1^*, c_2^*) = ({exemplo1[0]: .0f}, {exemplo1[1]: .0f})$", 
             (exemplo1[0]+10, exemplo1[1]+10), fontsize = 14)
plt.scatter([m1],[m2], s = 7*4**2, 
            label = f"dotação inicial $(m_1, m_2) = ({m1},{m2})$")
plt.annotate("A", (m1-5,m2-55), fontsize = 14)
plt.legend(fontsize = 11.5)
#plt.savefig(r'C:\Python\lemc\Imagens\Escolha_Intertemporal_exemplo.pdf')
plt.show()

        ################################################################
        #                   Estática Comparativa                       #
        #                (alterando a taxa de juros)                   #
        ################################################################

# Outros exemplos        
a2, b2, r2, m1_2, m2_2 = 0.5, 0.5, 0.1, 50, 750
a3, b3, r3, m1_3, m2_3 = 0.5, 0.5, 0.9, 50, 750
exemplo2 = choice(a2, b2, r2, m1_2, m2_2)
exemplo3 = choice(a3, b3, r3, m1_3, m2_3)

# Saída para o usuário
print(f"\nDiminuindo a taxa de juros para {100*r2}%, temos", end = " ")
print("que a nova distribuição de consumo no tempo que maximiza a", end = " ")
print("utilidade do agente é dada por", end = " ")
print(f'(c1*, c2*) = ({exemplo2[0]}, {exemplo2[1]}), com nível de', end = " ")
print(f"utilidade dado por U = {exemplo2[2]}. Se aumentarmos a", end = " ")
print(f"taxa de juros para {100*r3}%, a distribuição de consumo no", end = " ")
print("tempo é dada por (c1*, c2*) =", end = " ")
print(f"({exemplo3[0]}, {exemplo3[1]}), com nível de utilidade", end = " ")
print(f"U = {exemplo3[2]}. Podemos conferir estes resultados graficamente.")

# configuração exemplo1
budget1 = budget(eixo_x, m1, m2, r)

# configuração exemplo2
budget2 = budget(eixo_x, m1_2, m2_2, r2)

# configuração exemplo3
budget3 = budget(eixo_x, m1_3, m2_3, r3)

        ################################################################
        #                          Gráfico                             #
        ################################################################

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["lines.linewidth"] = (2.5)

# plotando exemplo1 (mesmo que anterior)
Z1 = plt.contour(X, Y, U(X, Y, a, b), levels = [exemplo3[2], exemplo1[2], 
                                                exemplo2[2]], linewidths = 2)
plt.plot(eixo_x, budget1, color = "black", ls = "dashed", lw = 2, 
         label = f"restrição orçamentária com $r = {100*r}\%$")

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["lines.linewidth"] = (2.5)

# plotando exemplo2
plt.plot(eixo_x, budget2, color = "blue", lw = 2, 
         label = f"restrição orçamentária com $r = {100*r2}\%$")

# plotando exemplo3
plt.plot(eixo_x, budget3, color = "red", lw = 2, 
         label = f"restrição orçamentária com $r = {100*r3}\%$")

# Marcando pontos na tangência da reta orçamentária com as curvas de utilidade
plt.scatter([exemplo1[0]], [exemplo1[1]], s = 4*4**2)
plt.scatter([exemplo2[0]], [exemplo2[1]], s = 4*4**2)
plt.scatter([exemplo3[0]], [exemplo3[1]], s = 4*4**2)
plt.scatter([m1],[m2], s = 7*4**2, 
            label = f"dotação inicial $(m_1, m_2) = ({m1},{m2})$")

plt.annotate("A", (m1-5,m2-55), fontsize = 14)

# configuração geral plot 
plt.legend(loc = 'lower left', bbox_to_anchor=(0.1, 0.1),
           fancybox = True, shadow = True, fontsize = 11.5)
plt.ylim(0, (1+r)*m1 + m2)
plt.xlim(0, m1_3 + m2_3/(1+r3))
plt.ylabel(r"Consumo em $t_2$", fontsize = 14)
plt.xlabel(r"Consumo em $t_1$", fontsize = 14)
#plt.savefig(r'C:\Python\lemc\Imagens\Escolha_Intertemporal_estatica_comparativa.pdf')
plt.show()
