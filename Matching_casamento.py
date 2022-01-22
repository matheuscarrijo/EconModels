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
        #                       Definindo funções                      #
        ################################################################

def matching_com_solteiros(preferencia_H, preferencia_M):
    
    # preferencia_H são listas de listas, em que a i-ésima lista nos dá a 
    # preferência (ranking de mulheres) do homem i (o mesmo raciocínio vale 
    # para preferencia_M).
    
    # Garante que o número de homens deve ser igual ao de mulheres:
    assert len(preferencia_H) == len(preferencia_M)
    
    n = len(preferencia_H) # n = numero de mulheres e homens
    
    casais = [] # registra os casais formados. É uma lista de listas.
    h_solteiros = [h for h in range(n)] # Registra os homens solteiros. 
    m_solteiras = [m for m in range(n)] # Registra as mulheres solteiras. 
    # Lista para a situacao dos casais (mulher = coluna j; homem = linha i)
    # 0 = mulher j não recebeu proposta
    # 1 = mulher j recebeu proposta do homem j
    # 2 = mulher j aceitou a proposta do homem j
    estado = np.zeros((n, n), dtype = int) # Ajuda na formatação do gráfico

    # Cria a estrutura do gráfico que usaremos depois
    fig, ax = plt.subplots(nrows = 2, ncols = 5, sharex = False, 
                   sharey = True, tight_layout = True,
                   figsize = (13, 7), dpi = 800)
    
     ######## Enquanto houver homem solteiro, haverá novas propostas ########

    while h_solteiros: 
        
        
        for m in range(n): # quando m mudar, significa nova rodada (todos
                            # farão proposta pra mulher mais preferida, depois
                            # para a segunda mais preferida, e assim sucess.) 
            
            propostas = [] # Lista de listas. O elemento [h, m] significa que
                           # o homem h fez proposta para a mulher m. 
                           
            solteiros_indice = [] 
            solteiras_indice = []
    
            ##############  Mulheres que querem ficar solteiras: ############# 
            
            for k in m_solteiras:
                
                if preferencia_M[k][m] == -1:
                    
                    casais.append([-1, k])
                    solteiras_indice.append(k)
                    
            for j in solteiras_indice:
                
                m_solteiras.remove(j)
            
            ##################  rodada de propostas ######################### 
            
            for h in h_solteiros: # faz proposta ou escolhe ficar solteiro
                
                if (preferencia_H[h][m] != -1): # faz proposta
    
                    propostas.append([h, preferencia_H[h][m]])
                    
                    if estado[h][preferencia_H[h][m]] != 2:
                        estado[h][preferencia_H[h][m]] = 1
                
                else: # fica solteiro
                    
                    casais.append([h, -1])
                    solteiros_indice.append(h)
                    
            for j in solteiros_indice:
                
                h_solteiros.remove(j)
            
            ##################  Análise de propostas ######################### 
            
            for h, m2 in propostas: 
                
                # se a mulher está casada:
                if m2 in [casais[k][1] for k in range(len(casais))]:
                
                    # ----- achando o índice do parceiro da mulher m2 ----- #
                    
                    for i in range(len(casais)):
                        
                       if casais[i][1] == m2:
                           
                           indice_parceiro = i
                           
                    # ----------------------------------------------------- # 
                    
                    # se o homem fazendo a proposta é preferido ao atual 
                    # parceiro da mulher, então ela troca de parceiro:
                    if (preferencia_M[m2].index(casais[indice_parceiro][0]) > 
                        preferencia_M[m2].index(h)):
                        
                        estado[h][m2] = 2
                        estado[casais[indice_parceiro][0]][m2] = 0
                        
                        h_solteiros.append(casais[indice_parceiro][0])
                        
                        casais[indice_parceiro][0] = h
                        h_solteiros.remove(h)
                        h_solteiros.sort()
                    
                # Se a mulher está solteira, ela aceita a proposta:
                else:
                    
                    # Mas apenas se ela não prefere estar solteira a estar com 
                    # h
                    if (preferencia_M[m2].index(-1) > 
                        preferencia_M[m2].index(h)):
                        
                        casais.append([h, m2])
                        h_solteiros.remove(h)
                        h_solteiros.sort()
                        m_solteiras.remove(m2)
                        m_solteiras.sort()
                        
                        estado[h][m2] = 2
            
            # Removendo -1 da lista de solteiros caso tenha algum
            if -1 in h_solteiros:
                
                h_solteiros.remove(-1)
                
            # Removendo [-1, -1] da lista casais pois não significa nada
            if [-1, -1] in casais:
                
                casais.remove([-1,-1])
            
            
        ################################################################
        #      Gráfico: mostra casais formados a cada rodada           #
        ################################################################
        
            # Código RGB para as cores
            cores = {0: np.array([255, 255, 255]), # branco
                     1: np.array([100, 100, 255]), # azul (não usaremos)
                     2: np.array([255, 100, 100])} # vermelho 
            
            # Matriz que mapeia o estado nas cores correspondentes
            mapa = []
            
            for homem in estado:
                
                linha = []
                
                for situacao in homem:
                    
                    cor = cores[situacao]
                    linha.append(cor)
                    
                mapa.append(linha)
            
            #Labels para os homens e mulheres
            label_homens = ["H0", "H1", "H2", "H3", "H4", "H5", "H6", "H7", 
                            "H8", "H9"]
            label_mulheres = ["M0", "M1", "M2", "M3", "M4", "M5", "M6", "M7", 
                              "M8", "M9"]
            
            if m in range(5):
                
                ax[0][m].matshow(mapa)
                # Cria ticks para traçar as linhas do grid
                ax[0][m].set_xticks(np.arange(-.5, len(label_homens)), 
                                    minor = True)
                ax[0][m].set_yticks(np.arange(-.5, len(label_mulheres)), 
                                    minor = True)
                ax[0][m].grid(True, which = 'minor', color = 'k', ls = ':', 
                              linewidth = 1)
                # Define a posição dos ticks principais e altera labels
                ax[0][m].set_xticks(np.arange(len(label_homens)))
                ax[0][m].set_yticks(np.arange(len(label_mulheres)))
                ax[0][m].set_xticklabels(label_mulheres)
                ax[0][m].set_yticklabels(label_homens)
                ax[0][m].title.set_text(f"Rodada {m+1}")
              
            if m == 5:
                
                ax[1][0].matshow(mapa)
                # Cria ticks para traçar as linhas do grid
                ax[1][0].set_xticks(np.arange(-.5, len(label_homens)), 
                                    minor = True)
                ax[1][0].set_yticks(np.arange(-.5, len(label_mulheres)), 
                                    minor = True)
                ax[1][0].grid(True, which = 'minor', color = 'k', ls = ':', 
                              linewidth = 1)
                # Define a posição dos ticks principais e altera labels
                ax[1][0].set_xticks(np.arange(len(label_homens)))
                ax[1][0].set_yticks(np.arange(len(label_mulheres)))
                ax[1][0].set_xticklabels(label_mulheres)
                ax[1][0].set_yticklabels(label_homens)
                ax[1][0].title.set_text(f"Rodada {m+1}")
                
            if m == 6:
                
                ax[1][1].matshow(mapa)
                # Cria ticks para traçar as linhas do grid
                ax[1][1].set_xticks(np.arange(-.5, len(label_homens)), 
                                    minor = True)
                ax[1][1].set_yticks(np.arange(-.5, len(label_mulheres)), 
                                    minor = True)
                ax[1][1].grid(True, which = 'minor', color = 'k', ls = ':', 
                              linewidth = 1)
                # Define a posição dos ticks principais e altera labels
                ax[1][1].set_xticks(np.arange(len(label_homens)))
                ax[1][1].set_yticks(np.arange(len(label_mulheres)))
                ax[1][1].set_xticklabels(label_mulheres)
                ax[1][1].set_yticklabels(label_homens)
                ax[1][1].title.set_text(f"Rodada {m+1}")
                
            if m == 7:
                
                ax[1][2].matshow(mapa)
                # Cria ticks para traçar as linhas do grid
                ax[1][2].set_xticks(np.arange(-.5, len(label_homens)), 
                                    minor = True)
                ax[1][2].set_yticks(np.arange(-.5, len(label_mulheres)), 
                                    minor = True)
                ax[1][2].grid(True, which = 'minor', color = 'k', ls = ':', 
                              linewidth = 1)
                # Define a posição dos ticks principais e altera labels
                ax[1][2].set_xticks(np.arange(len(label_homens)))
                ax[1][2].set_yticks(np.arange(len(label_mulheres)))
                ax[1][2].set_xticklabels(label_mulheres)
                ax[1][2].set_yticklabels(label_homens)
                ax[1][2].title.set_text(f"Rodada {m+1}")
                
            if m == 8:
                
                ax[1][3].matshow(mapa)
                # Cria ticks para traçar as linhas do grid
                ax[1][3].set_xticks(np.arange(-.5, len(label_homens)), 
                                    minor = True)
                ax[1][3].set_yticks(np.arange(-.5, len(label_mulheres)), 
                                    minor = True)
                ax[1][3].grid(True, which = 'minor', color = 'k', ls = ':', 
                              linewidth = 1)
                # Define a posição dos ticks principais e altera labels
                ax[1][3].set_xticks(np.arange(len(label_homens)))
                ax[1][3].set_yticks(np.arange(len(label_mulheres)))
                ax[1][3].set_xticklabels(label_mulheres)
                ax[1][3].set_yticklabels(label_homens)
                ax[1][3].title.set_text(f"Rodada {m+1}")
                
            if m == 9:
                
                ax[1][4].matshow(mapa)
                # Cria ticks para traçar as linhas do grid
                ax[1][4].set_xticks(np.arange(-.5, len(label_homens)), 
                                    minor = True)
                ax[1][4].set_yticks(np.arange(-.5, len(label_mulheres)), 
                                    minor = True)
                ax[1][4].grid(True, which = 'minor', color = 'k', ls = ':', 
                              linewidth = 1)
                # Define a posição dos ticks principais e altera labels
                ax[1][4].set_xticks(np.arange(len(label_homens)))
                ax[1][4].set_yticks(np.arange(len(label_mulheres)))
                ax[1][4].set_xticklabels(label_mulheres)
                ax[1][4].set_yticklabels(label_homens)
                ax[1][4].title.set_text(f"Rodada {m+1}")
                
    return casais

        ################################################################
        #                    Programa principal                        #
        ################################################################

# Sem solteiros (note que se todos preferem estar com alguém a ficar solteiro
# então é o mesmo caso em que não há opção de ficar solteiro)

preferencia_H2 = \
    [[0, 4, 2, 8, 9, 3, 5, 1, 7, 6, -1], [2, 7, 0, 3, 4, 5, 1, 9, 8, 6, -1], 
     [7, 4, 0, 3, 1, 5, 8, 6, 2, 9, -1], [8, 5, 3, 6, 7, 4, 9, 1, 2, 0, -1], 
     [9, 3, 1, 2, 5, 4, 0, 8, 7, 6, -1], [1, 0, 3, 6, 4, 8, 2, 9, 7, 5, -1], 
     [6, 4, 8, 1, 2, 0, 3, 7, 9, 5, -1], [0, 4, 7, 5, 8, 2, 9, 1, 6, 3, -1], 
     [7, 2, 3, 6, 1, 0, 5, 8, 9, 4, -1], [0, 5, 9, 6, 4, 1, 3, 2, 8, 7, -1]]

preferencia_M2 = \
    [[1, 5, 9, 6, 8, 0, 3, 4, 2, 7, -1], [1, 0, 2, 5, 6, 3, 8, 4, 9, 7, -1], 
     [5, 1, 4, 6, 7, 2, 8, 0, 3, 9, -1], [5, 9, 2, 0, 8, 7, 6, 3, 1, 4, -1], 
     [9, 7, 5, 3, 0, 6, 2, 4, 8, 1, -1], [1, 0, 4, 8, 9, 3, 5, 6, 2, 7, -1], 
     [9, 6, 7, 5, 1, 0, 2, 4, 3, 8, -1], [6, 9, 1, 0, 8, 3, 7, 4, 2, 5, -1], 
     [8, 2, 7, 6, 5, 1, 0, 4, 9, 3, -1], [4, 7, 6, 0, 1, 9, 2, 8, 5, 3, -1]]

# Com solteiros:     
    
preferencia_H = \
    [[0, 4, 2, 8, -1, 9, 3, 5, 1, 7, 6], [2, -1, 7, 0, 3, 4, 5, 1, 9, 8, 6], 
     [7, 4, 0, 3, 1, 5, 8, 6, -1, 2, 9], [-1, 8, 5, 3, 6, 7, 4, 9, 1, 2, 0], 
     [9, 3, 1, 2, 5, -1, 4, 0, 8, 7, 6], [1, 0, -1, 3, 6, 4, 8, 2, 9, 7, 5], 
     [6, 4, 8, 1, 2, 0, 3, 7, 9, 5, -1], [0, 4, 7, 5, 8, 2, 9, 1, 6, 3, -1], 
     [7, 2, -1, 3, 6, 1, 0, 5, 8, 9, 4], [0, 5, 9, 6, 4, -1, 1, 3, 2, 8, 7]]

preferencia_M = \
    [[-1, 1, 5, 9, 6, 8, 0, 3, 4, 2, 7], [1, 0, -1, 2, 5, 6, 3, 8, 4, 9, 7], 
     [5, -1, 1, 4, 6, 7, 2, 8, 0, 3, 9], [5, 9, 2, 0, -1, 8, 7, 6, 3, 1, 4], 
     [9, 7, 5, 3, 0, 6, 2, 4, 8, 1, -1], [1, 0, 4, -1, 8, 9, 3, 5, 6, 2, 7], 
     [9, 6, 7, 5, 1, 0, 2, 4, 3, -1, 8], [6, 9, 1, 0, -1, 8, 3, 7, 4, 2, 5], 
     [8, 2, 7, 6, 5, 1, -1, 0, 4, 9, 3], [4, -1, 7, 6, 0, 1, 9, 2, 8, 5, 3]]
    
casais_com_solteiros = matching_com_solteiros(preferencia_H, preferencia_M)

#plt.savefig(r'C:\Python\lemc\Imagens\matching.pdf')
