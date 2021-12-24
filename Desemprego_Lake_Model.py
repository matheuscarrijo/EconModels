# -*- coding: utf-8 -*-
"""
@author: Matheus L. Carrijo
"""

        ################################################################
        #                     Importando pacotes                       #
        ################################################################
        
import matplotlib.pyplot as plt #importing graph package
plt.figure(figsize=(9, 6), dpi=1000) #set default figure size 
import numpy as np

        ################################################################
        #                          Funções                             #
        ################################################################
    
def nivel_estacionario(empregados = 250_000, desempregados = 50_000, 
                       Alpha = .027, Lambda = .391):
    
    #Definindo as variáveis com o valor dos parâmetros
        
    forca_trabalho = empregados + desempregados
    
    A = np.array([[1 - Lambda, Alpha    ],
                  [Lambda     , 1 - Alpha]])
    x_inicial = np.array([[desempregados/forca_trabalho], 
                          [empregados/forca_trabalho]])
    
    tempo = []
    eixo_taxa_desemprego = [x_inicial[0][0]]
    eixo_taxa_emprego = [x_inicial[1][0]]
    t = 0
    tol = 1e-04
    dif = tol + 1
    
    # Calculando o nível estacionário
    
    while dif > tol:
        
        x = A @ x_inicial
        tempo.append(t)
        eixo_taxa_desemprego.append(x[0][0])
        eixo_taxa_emprego.append(x[1][0])
        dif = np.max(np.abs(x - x_inicial))
        x_inicial = x
        t += 1
    tempo.append(t)
    
    # Informando ao usuário
    
    print(f"\nPara uma economia com {empregados} empregados,", end = " ")
    print(f"{desempregados} desempregados, uma taxa de obtenção de", end = " ")
    print(f"emprego de {100*Lambda: .2f}%, e uma taxa de demissão", end = " ")
    print(f"de {100*Alpha: .2f}%, a taxa de desemprego no nível", end = " ")
    print(f"estacionário é dada por {100*x[0][0]: .2f}% \n")
    
    return x, tempo, eixo_taxa_desemprego, eixo_taxa_emprego

    
def individual_path(Lambda = 0.3, Alpha = .027, desempregado = True):
    """
    
    Parameters
    ----------
    Lambda : float, optional
        Taxa de obtenção de emprego. The default is 0.3.
    Alpha : float, optional
        Taxa de demissão. The default is .027.
    desempregado : bool, optional
        informa se os indivíduos estão desempregados. The default is True.

    Returns
    -------
    tempo : list
        lista em que a i-ésima entrada corresponde ao tempo que o i-esimo
        trabalhador demorou pra encontrar emprego (caso esteja desempregado) 
        ou que demorou pra ficar desempregado (caso esteja empregado).

    """
    
    if desempregado:
        
        tempo = []
        
        j = 1
        while j <= 1000: # amostra de 1000 individuos
            
            encontrou_emprego = False
            t = 0
            while not encontrou_emprego:
            # enquanto a pessoa j não encontrar emprego, ela continua 
            # procurando 
            
                r = np.random.rand()
                
                if r <= Lambda: # desempregado encontra emprego

                    encontrou_emprego = True
                    
                t += 1
                
            tempo.append(t) 
            j += 1
           
    else:    
        
        tempo = [] 
        
        j = 1
        while j <= 1000: # amostra de 1000 individuos
            
            ficou_desempregado = False 
            t = 0
            while not ficou_desempregado: # fica no emprego até ser demitido
            
                r = np.random.rand()    
            
                if r <= Alpha: # empregado ficou desempregado
    
                    ficou_desempregado = True
                    t += 1
                
                t += 1
                
            tempo.append(t) 
            j += 1
       
    return tempo


        ################################################################
        #                Uma economia com:                             #
        #                - empregados = 250_000                        #
        #                - desempregados = 50_000                      # 
        #                - Alpha = .027                                #
        #                - Lambda = .391                               #
        ################################################################

exemplo_padrao = nivel_estacionario()

        ################################################################
        #                         Gráfico                              #
        ################################################################

plt.rcParams["figure.figsize"] = (10, 6)
plt.rcParams["lines.linewidth"] = (2.5)

fig, ax = plt.subplots(nrows = 2, ncols = 1, sharex  = True)

# plot desemprego:
    
ax[0].plot(exemplo_padrao[1], exemplo_padrao[2], color = "blue", lw = 1.5)
ax[0].set_xlim(0, exemplo_padrao[1][-1])
ax[0].set_ylabel("Taxa de desemprego", fontsize = 14)
#ax[0].legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower center',
#             ncol=2, mode="expand", borderaxespad=0.)
ax[0].set_title(r'$(\alpha, \lambda) = (2.7\%, 39.1\%)$', fontsize = 14)

# plot emprego: 
    
ax[1].plot(exemplo_padrao[1], exemplo_padrao[3], color = "green", lw = 1.5)
ax[1].set_xlabel("Tempo", fontsize = 14)
ax[1].set_ylabel("Taxa de emprego", fontsize = 14)
#fig.savefig(r'C:\Python\lemc\Imagens\LakeModel0.pdf')
plt.show()


        ################################################################
        #         Variando parâmetros (estática comparativa)           #
        ################################################################

# Variando Lambda   
 
estatica1 = nivel_estacionario(450_000, 50_000, .04, .3)
estatica2 = nivel_estacionario(450_000, 50_000, .04, .6)

# Variando Alpha    

estatica3 = nivel_estacionario(450_000, 50_000, .03, .4)
estatica4 = nivel_estacionario(450_000, 50_000, .06, .4)

        ################################################################
        #                         Gráfico                              #
        ################################################################
        
fig, ax = plt.subplots(nrows = 2, ncols = 1, sharex  = True)

t_max = max(estatica1[1][-1], estatica2[1][-1], estatica3[1][-1], 
            estatica4[1][-1]) # limite eixo x

# plot desemprego:
    
ax[0].plot(estatica1[1], estatica1[2], color = "blue", lw = 1, 
           label = r'$(\alpha, \lambda) = (4\%, 30\%)$')
ax[0].plot(estatica2[1], estatica2[2], color = "green", lw = 1,
           label = r'$(\alpha, \lambda) = (4\%, 60\%)$')
ax[0].plot(estatica3[1], estatica3[2], color = "red", lw = 1,
           label = r'$(\alpha, \lambda) = (3\%, 40\%)$')
ax[0].plot(estatica4[1], estatica4[2], color = "black", lw = 1,
           label = r'$(\alpha, \lambda) = (6\%, 40\%)$')
ax[0].set_xlim(0, t_max)
ax[0].set_ylabel("Taxa de desemprego", fontsize = 14)
ax[0].legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower center',
             ncol=2, mode="expand", borderaxespad=0., fontsize = 14)

# plot emprego: 
    
ax[1].plot(estatica1[1], estatica1[3], color = "blue", lw = 1)
ax[1].plot(estatica2[1], estatica2[3], color = "green", lw = 1)
ax[1].plot(estatica3[1], estatica3[3], color = "red", lw = 1)
ax[1].plot(estatica4[1], estatica4[3], color = "black", lw = 1)
ax[1].set_xlim(0, t_max)
ax[1].set_xlabel("Tempo", fontsize = 14)
ax[1].set_ylabel("Taxa de emprego", fontsize = 14)
#fig.savefig(r'C:\Python\lemc\Imagens\LakeModel.pdf')
plt.show()

        ################################################################
        #              Trajetória de indivíduos com:                   #
        #                 - Lambda = .391                              # 
        #                 - Alpha = .027                               #
        ################################################################

exemplo_padrao2 = individual_path()

aux = max(exemplo_padrao2)
hist, valores = np.histogram(exemplo_padrao2, bins = np.arange(0, aux))
plt.plot(valores[:-1], hist, color="blue", linewidth=1)
plt.ylabel("Trabalhadores", fontsize = 14)
plt.xlabel("Tempo até encontrar emprego", fontsize = 14)
#plt.title('Histograma', fontsize = 13)
#plt.savefig(r'C:\Python\lemc\Imagens\histograma_desemprego.pdf')
plt.show()

        ################################################################
        #             Estática comparativa para desemprego             #
        ################################################################

exemplo_padrao3 = individual_path(Lambda = 0.2)
exemplo_padrao4 = individual_path(Lambda = 0.4)
exemplo_padrao5 = individual_path(Lambda = 0.65)
exemplo_padrao6 = individual_path(Lambda = 0.9)

aux = max(max(exemplo_padrao2), max(exemplo_padrao3),
          max(exemplo_padrao4), max(exemplo_padrao5))

hist2, valores2 = np.histogram(exemplo_padrao3, bins = np.arange(0, aux))
hist3, valores3 = np.histogram(exemplo_padrao4, bins = np.arange(0, aux))
hist4, valores4 = np.histogram(exemplo_padrao5, bins = np.arange(0, aux))
hist5, valores5 = np.histogram(exemplo_padrao6, bins = np.arange(0, aux))

        ################################################################
        #                         Gráfico                              #
        ################################################################
    
plt.plot(valores2[:-1], hist2, color="black", linewidth=1)
plt.plot(valores3[:-1], hist3, color="green", linewidth=1)
plt.plot(valores4[:-1], hist4, color="red", linewidth=1)
plt.plot(valores5[:-1], hist5, color="orange", linewidth=1)
plt.legend([r'$\lambda = 10\%$', r'$\lambda = 40\%$', r'$\lambda = 70\%$',
            r'$\lambda = 90\%$'], fontsize = 14)
plt.ylabel("Trabalhadores", fontsize = 14)
plt.xlabel("Tempo até encontrar emprego", fontsize = 14)
#plt.title('Histogramas', fontsize = 13)
#plt.savefig(r'C:\Python\lemc\Imagens\histograma_estatica_comparativa_desemprego.pdf')
plt.show()

################ Comentários da reunião dia 12/11 ##################

# 1) Fazer estática comparativa deste modelo OK

# 2) Simular uma trajetória de tamanho 100 de um indivíduo e uma trajetória de 
# tamanho endógeno, isto é, até conseguir emprego. 
#   - quanto tempo demorou até encontrar um emprego?
#   - pega outro indivíduo e faz novamente isso
#   - fazer para 1000 indivíduos e construir um histograma 
#   - Como o histograma se comporta quando mudamos o Lambda e Alpha?

"""
r = np.random.rand()
path = [0]

if r <= Lambda:
    # desempregado ficou empregado
    path.append(1)
else:
   # desempregado continua desempregado
   path.append(0)
   
if r <= Alpha:
    # empregado continua desempregado
    path.append(0)
else:
   # empregado continua empregado
   path.append(1)
"""