# -*- coding: utf-8 -*-
"""
@author: Matheus L. Carrijo
"""

import matplotlib.pyplot as plt

        ################################################################
        #                     Definindo funções                        #
        ################################################################
        
def utilidade_agente1(escolha_social):
    
    # Note que na função de utilidade do agente 1 só existe uma única
    # tecnologia possível, então não precisamos nem especificá-la.
    
    assert escolha_social == 0 or escolha_social == 1 or escolha_social == 2 
    
    # Se a escolha social é demandar tudo do agente 1: 
    if escolha_social == 0:
        
        return 100 
    
    # Se a escolha social é demandar produto dos dois agentes: 
    elif escolha_social == 1:
        
        return 50 
    
    else:
        
        return 0
    
def utilidade_agente2(escolha_social, tecnologia):
    
    # Para cada escolha social 0, 1 ou 2, temos duas tecnologias possíveis:
    # Tecnologia 0 é a pior tecnologia; tecnologia 1 é a melhor tecnologia.
    
    assert escolha_social == 0 or escolha_social == 1 or escolha_social == 2 
    assert tecnologia == 0 or tecnologia == 1 
    
    # Se a escolha social é demandar tudo do agente 1: 
    if escolha_social == 0:
        
        return 0 # a utilidade do agente 2, quando a escolha social é demandar 
                 # tudo do agente 1, é sempre nula.   
    
    # Se a escolha social é demandar de ambos os agentes: 
    elif escolha_social == 1:
        
        return 50 # a utilidade do agente 2, quando a escolha social é demandar 
                  # de ambos os agentes, é sempre 50.
    
    # Se a escolha social é demandar tudo do agente 2
    else:
        
        # e se o agente 2 tem a melhor tecnologia a2
        if tecnologia == 1:
            
            return 100 # ...seu payoff é 100
        
        else: # Caso contrário, se o agente 2 tem a pior tecnologia
            
            return 25 # ...seu payoff é 25

def escolha_social_implementavel(SCF):
    
    """
    Queremos verificar se uma determinada escolha social é implementável no 
    sentido de que os agentes terão inventivos para reverelar seus verdadeiros 
    tipos (no caso específico tratado aqui, apenas o agente 2 poderia fazer 
    isto, já que apenas ele quem tem informação "privada").
    """
    
    escolha_social_implementavel = [] 
    tipos_ag2 = [0, 1]
    
    for escolha in SCF:
        
        escolha_implementavel_bool = True 
        
        for tipo in tipos_ag2:
                
            # utilidade do agente 2 se ele verdadeiramente revelar seu tipo:
            util_ag2_verdadeiro = utilidade_agente2(escolha[tipo], tipo)
        
        ########## utilidade do agente 2 se ele mentir seu tipo: ############
        
            if tipo == 0:
            
                util_ag2_falso = utilidade_agente2(escolha[1], tipo)
            
            else:
            
                util_ag2_falso = utilidade_agente2(escolha[0], tipo)
                
        ####################################################################
            
            if util_ag2_falso > util_ag2_verdadeiro:
                
                escolha_implementavel_bool = False
        
        if escolha_implementavel_bool == True:
            
            escolha_social_implementavel.append(escolha)
    
    return escolha_social_implementavel


        ################################################################
        #                    Programa principal                        #
        ################################################################
        
# Função de escolha social: primeira entrada de cada linha indica a escolha 
# social com o agente 2 escolhendo a pior tecnologia e segunda entrada indica a 
# escolha social com o agente 2 escolhendo a melhor tecnologia. Por padrão, o 
# agente 1 somente escolhe um tipo de tecnologia.

SCF = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]

# Queremos analisar se cada escolha social é implementável no sentido de que os
# agentes irão revelar seus verdadeiros tipos. 
escolha_social = escolha_social_implementavel(SCF)

        ################################################################
        #      Tabela das funções de escolha social implementáveis     #
        ################################################################
        
def tabela_latex():
    
    global tabela
    
    # Cria a tabela usando a sintaxe do latex (o processo não aceita uma string
    # com multiplas linhas; o que eu faço aqui é quebrar a string simples 
    # usando \ no final da linha, apenas pra facilitar a visualização)
        
    texto = ''
    for i in range(len(escolha_social)):
        for j in range(len(escolha_social[i])):
            texto += f'\Large${escolha_social[i][j]}$ &'
        texto = texto[:-1] + '\\\\ \hline '
            
    tabela = f"\\begin{{adjustwidth}}{{2.25in}}{{2.25in}}\
        \\begin{{adjustbox}}{{width=40mm,nofloat=table,center}}\
        \\begin{{tabular}}{{ | c | c | }}\
        \hline\
        \multicolumn{{2}}{{| c |}}{{Funções de escolha social implementáveis}} \\\\ \
        \hline \
        $f(a_{1}, b_{2})$ & $f(a_{1}, a_{2})$ \\\\ \
        \hline  \
        {texto} \
        \\end{{tabular}} \
        \\end{{adjustbox}} \
        \\end{{adjustwidth}}"                                            
    
    # Define o estilo cosmético da figura.
    plt.style.use('_classic_test_patch')

    # Plot da tabela:
    # Habilita o uso do código em tex
    plt.rc("text", usetex = True)
    
    # Habilita alguns pacotes do latex
    plt.rc("text.latex", preamble=r'\setlength{\arrayrulewidth}{0.15mm}\setlength{\tabcolsep}{18pt}\renewcommand{\arraystretch}{1.5}\usepackage{multirow,array,float,'
           'changepage,adjustbox,caption}')
    
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
    
# Teste:        
tabela_latex()


    
    