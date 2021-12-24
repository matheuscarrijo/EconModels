# -*- coding: utf-8 -*-

"""
@author: Matheus L. Carrijo
"""
        ################################################################
        #                     Importando pacotes                       #
        ################################################################
        
import numpy as np
import random as rd # Precisaremos desta pacote para o computador escolher
                    # jogar o jogo Stag Hunt 
import matplotlib.pyplot as plt
        ################################################################
        #                       Definindo funções                      #
        ################################################################

def payoff(jogo):
    """
    
    
    Parameters
    ----------
    jogo : Lista.
        A primeira entrada é a jogada do primeiro jogador e a segunda entrada
        é a jogada do segundo jogador. Para um jogo ser válido, ele deve estar
        dentro da matriz de jogos possíveis. 

    Returns
    -------
    Lista
        Retorna uma lista em que a primeira entrada representa o payoff do 
        primeiro jogador e a segunda entrada o payoff do segundo jogador.

    """
    
    if jogo in matriz:
        
        if jogo == ['s', 's']:
            return [5, 5]
        if jogo == ['s', 'h']:
            return [0, 3]
        if jogo == ['h', 's']:
            return [3, 0]
        if jogo == ['h', 'h']:
            return [3, 3]
        
    else:
        
        return -1
    
def rodada():
    """
    

    Returns
    -------
    jogo : Lista.
        Retorna uma lista contendo o jogo feito pela escolha das estratégias
        pelos dois jogadores.

    """
    
    jogada_A, jogada_B = rd.choice(estrategia), rd.choice(estrategia)
    jogo = [jogada_A, jogada_B]
    
    return jogo

 
def nash_equilibrium_analitico(jogo):
    """
    

    Parameters
    ----------
    jogo : Lista.
        Recebe uma lista do jogo definido pelas ações dos jogadores. 

    Returns
    -------
    bool
        Calcula o equilíbrio de forma analítica do jogo, isto é, sabemos de 
        antemão que o equilíbrio consiste nos jogos em que ambos os jogadores 
        escolhem ao mesmo tempo caçar lebre ou veado.

    """
    
    if jogo in matriz:
        
        payoffs = payoff(jogo)
        
        if payoffs == [5, 5] or payoffs == [3,3]:
            
            equilibrio = True
            
        else:
            
            equilibrio = False
            
        return equilibrio
    
    else:
        
        return -1


def nash_equilibrium(jogo):
    """
    

    Parameters
    ----------
    jogo : Lista
        Recebe uma lista do jogo determinado pelas ações (escolha das 
        estratégias) dos jogadores.

    Returns
    -------
    Bool
        Assim como na função anterior, calcula o equilíbrio de Nash. Aqui, 
        porém, fazemos um algorítmo em que o cálculo do equilíbrio baseia-se 
        na análise da mudança de estratégia unilateral de cada jogador: se 
        houver uma melhora no payoff dos jogadores, então não há equilibrio; 
        caso contrário, há.
        
    """
            
    if jogo in matriz: 
        
        payoffs = payoff(jogo)
        equilibrio = True
        
        if jogo[0] == 'h':
            
            jogo[0] = 's'
            payoff_aux = payoff(jogo)
            
            if payoff_aux[0] > payoffs[0]:
                
                equilibrio = False
            
            jogo[0] = 'h'
        
        if jogo[0] == 's':
            
            jogo[0] = 'h'
            payoff_aux = payoff(jogo)
            
            if payoff_aux[0] > payoffs[0]:
                
                equilibrio = False
        
            jogo[0] = 's' 
        
        if jogo[1] == 'h':
            
            jogo[1] = 's'
            payoff_aux = payoff(jogo)
            
            if payoff_aux[1] > payoffs[1]:
                
                equilibrio = False
                
            jogo[1] = 'h'
        
        if jogo[1] == 's':
            
            jogo[1] = 'h'
            payoff_aux = payoff(jogo)
            
            if payoff_aux[1] > payoffs[1]:
                
                equilibrio = False
            
            jogo[1] = 's'
                
        return equilibrio
    
    else:
        
        return -1
    
def tabela_latex():
    
    global tabela
    
    matriz0 = np.array([[[5,5], [0,3], [3,0], [3,3]]])
    matriz = matriz0.flatten() # Transforma a matriz de payoffs em uma lista
    
    # Cria a tabela usando a sintaxe do latex:
    # (o processo não aceita uma string com multiplas linhas; o que eu faço 
    # aqui é quebrar a string simples usando \ no final da linha, apenas pra 
    # facilitar a nossa visualização)
    
    tabela = f"\\begin{{table}}[H]\\centering\\begin{{tabular}}{{c c | c | c |}} \
        & \\multicolumn{{1}}{{c}}{{}} & \\multicolumn{{2}}{{c}}{{Jogador 2}}\\\\ \
        & \\multicolumn{{1}}{{c}}{{}} & \\multicolumn{{1}}{{c}}{{$s$}}  & \\multicolumn{{1}}{{c}}{{$h$}} \\\\ \
        \\cline{{3-4}} \\multirow{{2}}*{{Jogador 1}}  & $s$ & ({matriz[0]},{matriz[1]}) & ({matriz[2]},{matriz[3]}) \\\\ \
        \\cline{{3-4}} & $h$ & ({matriz[4]},{matriz[5]}) & ({matriz[6]},{matriz[7]}) \\\\ \
        \\cline{{3-4}} \
    \\end{{tabular}}\\end{{table}}"                                            
    
    # Define o estilo cosmético da figura.
    plt.style.use('_classic_test_patch')

    # Plot da tabela:
    # Habilita o uso do código em tex
    plt.rc("text", usetex = True)
    
    # Habilita alguns pacotes do latex
    plt.rc("text.latex", preamble=r'\usepackage{multirow,array,float}')
    
    # Inicializa a figura p/ plot
    plt.figure(figsize=(1,1), dpi = 500)
    
    # Cria eixos p/ plot
    ax = plt.subplot2grid((1,1),(0,0))
    
    # Desativa o frame criado pelo passo anterior
    ax.axis("off")
    
    # Passa o conteúdo da variável ``tex_table´´ como texto ao gráfico
    ax.text(0.5, 0.5, tabela, ha = "center", va = "center")
    # Mostra a figura
    
    #plt.savefig('Inserir nome.pdf')
    plt.show()
    
    # Desabilita o uso do código em tex
    plt.rc("text", usetex = False)
  
        ################################################################
        #                           Jogando                            #
        ################################################################
        
estrategia = ['s', 'h'] # as possíveis ações dos jogadores são caçar veado 
                        # (jogar "s") ou caçar lebre (jogar "h").
matriz = [['s', 's'], ['s', 'h'],
          ['h', 's'], ['h', 'h']] # jogos possíveis determiandos pela matriz.

equilibrio = False # Para entrar no loop abaixo
i = 1 # contagem do número de jogos

while not equilibrio: #Jogos serão feitos até que se alcance um equilibrio 

    jogo = rodada() #Um jogo é uma lista com as jogadas dos dois jogadores
    equilibrio = nash_equilibrium(jogo) #Confere se o jogo constitui equilibrio
    payoffs = payoff(jogo) #Calcula o Payoff do jogo
    
    print("\nJogaremos até encontrarmos um jogo com Equilíbrio de Nash.")
    
    if jogo == ['s', 'h']:
            
        print(f"\nJogo {i}: O jogador A falhou em tentar caçar", end = " ")
        print("o veado sozinho; o jogador B conseguiu caçar", end = " ")
        print("a lebre sozinho. Como o jogador A poderia", end = " ")
        print("melhorar sua situação mudando sua estratégia e", end = " ")
        print("caçar uma lebre sozinho, este jogo não", end = " ")
        print("constitui um Equilíbrio de Nash.")
            
    if jogo == ['h', 's']:
            
        print(f"\nJogo {i}: O jogador B falhou em tentar caçar", end = " ")
        print("o veado sozinho; o jogador A conseguiu caçar", end = " ")
        print("a lebre sozinho. Como o jogador B poderia", end = " ")
        print("melhorar sua situação mudando sua estratégia e", end = " ")
        print("caçar uma lebre sozinho, este jogo não", end = " ")
        print("constitui um Equilíbrio de Nash.")
        
    if jogo == ['h', 'h']:
            
        print(f"\nJogo {i}: Ambos os jogadores escolheram", end = " ")
        print("caçar lebres e conseguiram. Como nenhum jogador", end = " ")
        print("tem a ganhar mudando sua estratégia unilateralme", end = "")
        print("nte para caçar um veado, então este jogo constit", end = "")
        print("ui um Equilíbrio de Nash. Note, no entanto, que ambo", end = "")
        print("s melhorariam sua situação se combinassem de caçar um veado.")
            
    if jogo == ['s', 's']:
            
        print(f"\nJogo {i}: Ambos os jogadores escolheram", end = " ")
        print("caçar veados e conseguiram. Como nenhum jogador", end = " ")
        print("tem a ganhar mudando sua estratégia unilateralme", end = "")
        print("nte para caçar uma lebre, então este jogo constit", end = "")
        print("ui um Equilíbrio de Nash. Note que este é o melhor", end = " ")
        print("resultado que os jogadores poderiam ter.")
            
    i += 1

i -= 1

        ################################################################
        #                    Invocando a tabela                        #
        ################################################################

tabela_latex()