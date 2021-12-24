# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 22:59:27 2021

@author: Matheus L. Carrijo
"""

        ################################################################
        #                     Importando pacotes                       #
        ################################################################
        
import numpy as np #importing numpy        
import matplotlib.pyplot as plt #importing graph package
plt.figure(figsize=(10, 6), dpi=1000) #set default figure size

        ################################################################
        #                       Definindo funções                      #
        ################################################################
        
def utilidade(x, y, alpha = 0.5):
    """
    Função de utilidade Cobb-Douglas dos agentes (ambos terão a mesma).
    """
    
    return (x**alpha)*(y**(1-alpha))

def demanda(p, dot, alpha = 0.5):
    """
    Resolve o problema do consumidor de forma analítica, estabelecendo a 
    demanda pelos bens x e y. Como as funções de utilidade são as mesmas para
    ambos os agentes, a demanda será igual para valores arbitrários da dotação
    inicial. O parâmetro 'dot' é uma lista em que a primeira entrada 
    corresponde à dotação inicial do bem x; e a segunda para o bem y. O 
    parâmetro preço é uma lista em que a primeira entrada corresponde ao preço
    do bem x e a segunda ao preço do bem y.
    """
    
    x = alpha*(p[0]*dot[0] + p[1]*dot[1]) / p[0]
    y = (1 - alpha)*(p[0]*dot[0] + p[1]*dot[1]) / p[1]
    
    return x, y
 
def demanda_liq(p, dot):
    """
    Calcula o excesso de demanda para os bens x e y, isto é, a diferença entre
    a demanda total e a dotação inicial dos agentes. O parâmetro p é uma lista
    com os preços de x e y, respect., enquanto que dot é uma lista com as
    dotações iniciais dos bens x e y, respect..
    """
    
    x, y = demanda(p, dot) 
    demanda_liq_x = x - dot[0]
    demanda_liq_y = y - dot[1]
    
    return demanda_liq_x, demanda_liq_y

def demanda_liq_agreg(p, dot_A, dot_B):
    """
    Calcula a demanda líquida agregada para os bens x e y. A demanda líquida 
    agregada nada mais é que a soma das demandas líquidas individuais.
    """
    
    demanda_liq_agreg_x = demanda_liq(p, dot_A)[0] + demanda_liq(p, dot_B)[0]
    demanda_liq_agreg_y = demanda_liq(p, dot_A)[1] + demanda_liq(p, dot_B)[1]
    
    return demanda_liq_agreg_x, demanda_liq_agreg_y

def equilibrio(dot_A, dot_B):
    """
    Calcula o equilíbrio geral para um mercado competitivo de dois bens e dois
    indivíduos. Seguindo o que diz a Lei de Walras, o preço do bem x pode ser 
    fixado em 1 (bem numerário) enquanto que achamos o preço do bem 2 que zera 
    o excesso de demanda agregado do bem 2.
    """    
    
    # Procurando o zero da demanda agregada excedente para o bem y
    # pelo método da bissecção: 
    
    global px
        
    px = 1
    tol = 1e-10
    p_alto = 1000
    p_baixo = 0
    
    # Analisando a fronteira:
    tentativa1 = demanda_liq_agreg([px, p_alto], dot_A, dot_B)[1]
    if abs(tentativa1) < tol:
        return p_alto 
    
    # atualiza preco pela média 
    preco = p_alto / 2
    excesso_demanda_agreg = demanda_liq_agreg([px, preco], dot_A, dot_B)[1]
    
    while abs(excesso_demanda_agreg) > tol: 
        
        if excesso_demanda_agreg > 0:
            
            p_baixo = preco
            
        else:
            
            p_alto = preco
        
        preco = (p_baixo + p_alto) / 2
        excesso_demanda_agreg = demanda_liq_agreg([px, preco], dot_A, dot_B)[1]
        
    return preco

def curva_contrato():
    """
    Calcula um subconjunto da curva de contrato variando as dotações.
    """
    
    precos_equilibrio = [] # Lista para adicionar os preços de equilíbrio 
                           # conforme variamos as dotações.
                           
    #y_aux = np.linspace(0, total_dot_y, 20) 
    y_aux = np.linspace(0, total_dot_y, 5) 
    # Não estou "varrendo" toda a caixa de Edgeworth para calcular as
    # demandas de equilíbrio. Passo apenas inteiramente por um eixo (eixo
    # x, por ex) e vario alguns pontos do eixo y. Por este motivo, a curva 
    # resultante é um subconjunto da curva de contrato.
    
    for j in y_aux:
        
        for i in x:
            
            precos_equilibrio.append(equilibrio([i, j], [total_dot_x - i, 
                                                         total_dot_y - j])) 
    
    x_estrela = []
    y_estrela = []
    
    for k in precos_equilibrio:
        
        for m in y_aux:
            
            for l in x:
            
                x_estrela.append(demanda([1, k], [l, m])[0])
                y_estrela.append(demanda([1, k], [l, m])[1])
    
    return [x_estrela, y_estrela]

        ################################################################
        #                    Programa principal                        #
        ################################################################
        
#dot_A = [100, 25] # dotação indivíduo A
#dot_B = [50, 150] # dotação indivíduo B

#dot_A = [23, 33] # dotação indivíduo A
#dot_B = [14, 32] # dotação indivíduo B

dot_A = [230, 100] # dotação indivíduo A
dot_B = [400, 90] # dotação indivíduo B

preco_equilibrio_y = equilibrio(dot_A, dot_B)
p_equilibrio = [px, preco_equilibrio_y]

#Calcula as demandas de equilíbrio para os indivíduos A e B, respect.:
demanda_eq_A = demanda(p_equilibrio, dot_A) 
demanda_eq_B = demanda(p_equilibrio, dot_B)

# Utilidade dos agentes em equilíbrio:
u_valor_A = utilidade(demanda_eq_A[0], demanda_eq_A[1])
u_valor_B = utilidade(demanda_eq_B[0], demanda_eq_B[1])


total_dot_x = dot_A[0] + dot_B[0] # pode-se considerar o tamanho do eixo 
                                  # horizontal da caixa de Edgeworth
total_dot_y = dot_A[1] + dot_B[1] # pode-se considerar o tamanho do eixo 
                                  # vertical da caixa de Edgeworth

x = np.linspace(0.0001, total_dot_x, 100) # grid da quantidade do bem x
y = np.linspace(0.0001, total_dot_y, 100) # grid da quantidade do bem y

contrato = curva_contrato()

        ################################################################
        #                  Informando ao usuário                       #
        ################################################################

print(f"\nCom dotações dos agentes A e B dadas por {dot_A} e", end = " ")
print(f"{dot_B} as alocações de equilíbrio para os indivíduos A", end = " ")
print(f"e e B são, respect., ({demanda_eq_A[0]:.2f},", end = " ")
print(f"{demanda_eq_A[1]:.2f}) e ({total_dot_x-demanda_eq_A[0]:.2f}", end = "")
print(f", {total_dot_y-demanda_eq_A[1]:.2f}).\n")
print("A curva de contrato na figura mostra as diferentes", end = " ")
print("alocações eficientes para variações nas dotações iniciais.\n")

        ################################################################
        #                         Gráfico                              #
        ################################################################

#plt.style.use('classic')
#plt.style.use('default')
plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["lines.linewidth"] = (2.5)

fig, ax = plt.subplots(tight_layout = True)  

# Cria o produto cartesiano das quantidades x_1 e x_2.
xc_1, xc_2 = np.meshgrid(x, y)

# Coloca label nos eixos originais
ax.set_xlabel('$x_A$', fontsize = 20)
ax.set_ylabel('$y_A$', fontsize = 20)

ax.axis([0, 1.02*total_dot_x, 0, 1.05*total_dot_y])

# Calcula a utilidade do consumidor A
uA = utilidade(xc_1, xc_2) # Calcula a matriz de utilidades do 
                           # consumidor A.

# Calcula a utilidade do consumidor B. Como queremos que o gráfico tenha origem
# em x = x0 e y = y0, fazemos o ajuste nos argumentos da função.
uB = utilidade(total_dot_x - xc_1, total_dot_y - xc_2) # Calcula a matriz de  
                                                       # utilidades do
                                                       # consumidor B.

# Criamos um novo eixo y (apenas para repetir os ticks e labels do eixo y 
#                         original)
ax2 = ax.twinx()

# Copiamos os limites do eixo y original
orig_ylim = ax.get_ylim()

# Replicamos os limites do eixo y original no novo eixo
ax2.set_ylim(orig_ylim)

# Definimos um label para o novo eixo y
ax2.set_ylabel('$y_B$', fontsize = 20)

# Invertemos o sentido do texto do eixo y original
ax2.invert_yaxis()

# Criamos um novo eixo x (apenas para repetir os ticks e labels do eixo x 
#                         original)
ax3 = ax.twiny()

# Copiamos os limites do eixo x original
orig_xlim = ax.get_xlim()

# Replicamos os limites do eixo x original no novo eixo
ax3.set_xlim(orig_xlim)

# Definimos um label para o novo eixo x
ax3.set_xlabel('$x_B$', fontsize = 20)

# Invertemos o sentido do texto do eixo x original
ax3.invert_xaxis()


CS1 = ax.contour(xc_1, xc_2, uA, levels = [u_valor_A - 70, u_valor_A, 
                                           u_valor_A + 50, u_valor_A + 100], 
                 linestyles = 'dashdot', colors = 'k', alpha = 1, 
                 extend = 'both')
CS2 = ax.contour(xc_1, xc_2, uB, levels = [u_valor_B - 100, u_valor_B - 50,
                                           u_valor_B, u_valor_B + 70], 
                 linestyles = 'dotted', colors = 'g', alpha = 1, 
                 extend = 'both')

# Curva de contrato:
ax.plot(contrato[0], contrato[1], 'blue', linewidth = 2, alpha = 0.6,
        label = 'Curva de contrato')

#Alocação de equilíbrio:
ax.scatter(demanda_eq_A[0], demanda_eq_A[1], s = 10*5**2, 
           label = "Alocação de equilíbrio", alpha = 1, c = "r")

# Dotação inicial:
ax.scatter(dot_A[0], dot_A[1], s = 10*5**2, label = "Dotação", alpha = 1,
           c = "black")
#ax.plot(dot_A[0], dot_A[1], 'black', marker = ".", markersize = 25,
#        label = "Dotação")
ax.legend(loc = "upper right", fancybox = True, shadow = True, fontsize = 13)

#plt.savefig(r'C:\Python\lemc\Imagens\Caixa_Edgeworth3.pdf')
plt.show()

