from random import *
import random

def criaPopulacao(): 
    lista =[]
    string = ""
    for i in range(6):
        for i in range(7):
            aleatorio = choices([0,1]) 
            string=string+str(aleatorio[0]) 
        lista.append(string) 
        string = "" 
            
    return lista

def criaAvaliacao(valor):
    populacao = valor
    kgProduto=[7, 8, 4, 10, 4, 6, 4]
    benefProduto = [5, 8, 3, 2, 7, 9, 4]
    avaliacao =[]
    valorP = 0
    valorF = 0
    indice = 0
    geracao = 0

    for i in populacao:
        for x in range(7):
            if i[x] == '1':
                valorP +=kgProduto[x]
                valorF +=benefProduto[x]
        indice+=1    
        lista =[geracao, indice, i, valorF, valorP]
        avaliacao.append(lista)

        valorP = 0
        valorF = 0

    return avaliacao

def criaSelecao(valor):
    avaliacao = valor
    selecao=[]
    
    for x in range(2):
        t=0
        for i in avaliacao: t += i[3]

        i=0
        soma = (avaliacao[i][3] / t)
        r = random.random()
        while soma < r:
            i=(i+1)
            soma += avaliacao[i][3]/t
  
        selecao.append(avaliacao[i])
        avaliacao.pop(i)
        i=0
        
    return selecao

def criaCruzamento(valor):
    selecao = valor
    cruzamento =[]
    ponto = random.randint(0,6)

    pai1 = selecao[0][2]
    pai2 = selecao[1][2]

    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]

    cruzamento.append(filho1)
    cruzamento.append(filho2)

    avalia = criaAvaliacao(cruzamento)

    return avalia
 
def criaMutacao(valor):
    selecao = valor
    selecionado = 0
    lSelecionado =[]
    t=0
    for i in selecao: t += i[3]

    i=0
    soma = (selecao[i][3] / t)
    r = 0.1
    while soma < r:
        i=(i+1)
        soma += selecao[i][3]/t
    selecionado = selecao[i][2]
 
    posicao = random.randint(0,6)

    x = [selecionado[i:i+1] for i in range(0, len(selecionado), 1)]

    if x[posicao] == '0':
        x[posicao] = '1'
    else:
        x[posicao] = '0'
        
    selecionado = ''.join(x)
    lSelecionado.append(selecionado)
    avalia = criaAvaliacao(lSelecionado)
    
    return avalia

def novaPopulacao():
    t = 0
    populacao = criaPopulacao()
    avaliacao = criaAvaliacao(populacao)
    produtos = ['1','2','3','4','5','6','7']
    real=[]
    string = ''
    cont = 0
    
    for x in avaliacao:
        for y in x[2]:
            if y == '1':
                string = string+produtos[cont]
                cont += 1
            else:
                cont += 1
        real.append(string)
        string = ''
        cont=0
        
    print('Populacao',t,':', avaliacao)
    print('Forma real:', real, '\n')
    real.clear()
    
    for i in range(4):
        t+=1
        selecao = criaSelecao(avaliacao)
        cruzamento = criaCruzamento(selecao)
        for i in cruzamento:
            i[0] = t
            avaliacao.append(i)

        mutacao = criaMutacao(cruzamento)
        for i in mutacao:
            i[0] = t
        for i in avaliacao:
           if i[0] == mutacao[0][0] and i[1] == mutacao[0][1]:
               i[2]= mutacao[0][2]
               i[3]= mutacao[0][3]
               i[4]= mutacao[0][4]
        
        for x in avaliacao:
            for y in x[2]:
                if y == '1':
                    string = string+produtos[cont]
                    cont += 1
                else:
                    cont += 1
            real.append(string)
            string = ''
            cont=0
        print('Populacao',t,':', avaliacao)
        print('Forma real:', real, '\n')
        real.clear()
        
print(novaPopulacao())
