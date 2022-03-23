# função para pegar a posição inicial para o argumento 
# texto = o texto para pegar o argumrnto selecionado
# argumento = argumento para ser pesquisado
# inicioBloco = argumento inicial do bloco (não obrigatorio)
# inicioBloco = argumento inicial do bloco (não obrigatorio)
def posicaoInicial(texto, argumento, inicioBloco=None, finalBloco=None):
    return texto.index(argumento, inicioBloco, finalBloco)

# função para pegar a posição final para o argumento 
# texto = o texto para pegar o argumrnto selecionado
# argumento = argumento para ser pesquisado
# inicioBloco = argumento inicial do bloco (obrigatorio)
# inicioBloco = argumento inicial do bloco (obrigatorio)
def posicaoFinal(texto, argumento, inicioBloco=None, finalBloco=None):
    return texto.index(argumento, inicioBloco, finalBloco) + len(argumento)

# função para pegar o texto completo entre duas posição 
# texto = o texto para pegar o argumrnto selecionado
# argumentoInicial = argumento inicial para pesquisa
# argumentoFinal = argumento final para pesquisa
# inicioBloco = argumento inicial do bloco (obrigatorio)
# inicioBloco = argumento inicial do bloco (obrigatorio)
def textoCompleta(texto, argumentoInicial, argunmentoFinal, inicioBloco, finalBloco):
    return texto[posicaoInicial(texto, argumentoInicial, inicioBloco, finalBloco): 
    posicaoFinal(texto, argunmentoFinal, inicioBloco, finalBloco)]

# função para pegar o argumeto texto completo entre duas posição 
# texto = o texto para pegar o argumrnto selecionado
# argumentoInicial = argumento inicial para pesquisa
# argumentoFinal = argumento final para pesquisa
def valorTexto(texto, argumentoInicial, argunmentoFinal):
    return texto[posicaoFinal(texto, argumentoInicial): 
    posicaoInicial(texto, argunmentoFinal)]

# função para alterar o texto antigo para o novo  
# texto = o texto para pegar o argumrnto selecionado
# argumentoInicial = argumento inicial para pesquisa
# argumentoFinal = argumento final para pesquisa
# novoValor = novo texto para subtituir o antigo
def trocarTexto(texto, argumentoInicial, argunmentoFinal, novoValor,):
    inicioBloco = posicaoInicial(texto, '<proxy>')
    finalBloco = posicaoFinal(texto, '</authPassword>')
    argumento = textoCompleta(texto, argumentoInicial, argunmentoFinal, inicioBloco, finalBloco)

    if argumento is not None:
        valor = valorTexto(argumento, argumentoInicial, argunmentoFinal)
        argumentoNovo = argumento.replace(valor, novoValor)
        return texto.replace(argumento, argumentoNovo)
        
# função para validar o texto pego na interface 
def validarStr(texto):
    return len(texto) >= 3
