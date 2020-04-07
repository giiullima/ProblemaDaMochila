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

#print(criaPopulacao())

def criaAvaliacao(valor):
    populacao = valor
    kgProduto=[7, 8, 4, 10, 4, 6, 4]
    benefProduto = [5, 8, 3, 2, 7, 9, 4]
    avaliacao =[]
    valorP = 0
    valorF = 0
    item = 0
    
    #print(populacao)
    
    for i in populacao:
        for x in range(7):
            if i[x] == '1':
               valorP +=kgProduto[x]
               valorF +=benefProduto[x]
        item+=1    
        lista =[item, i, valorF, valorP]
        avaliacao.append(lista)
        
        valorP = 0
        valorF = 0

    return avaliacao

#print(criaAvaliacao())

def CriaSelecao():
    avaliacao = criaAvaliacao(criaPopulacao())
    selecao=[]
    
    for x in range(2):
        t=0
        for i in avaliacao: t += i[2]

        i=0
        soma = (avaliacao[i][2] / t)
        r = random.random()
       
        while soma < r:
            i=(i+1)
            soma += avaliacao[i][2]/t
 
        selecao.append(avaliacao[i])
        avaliacao.pop(i)
        i=0
    return selecao
print(CriaSelecao())

def criaCruzamento():
    selecao = CriaSelecao()
    cruzamento = []
    ponto = random.randint(0,6)

    pai1 = selecao[0][1]
    pai2 = selecao[1][1]

    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]

    cruzamento.append(filho1)
    cruzamento.append(filho2)

    return cruzamento

print(criaCruzamento())

def criaMutacao():
    selecionado = '1101100'
    posicao = random.randint(0,6)

    x = [selecionado [i:i+1] for i in range (0, len(selecionado), 1)]
    if x[posicao] == '0':
        x[posicao] = '1'
    else:
        x[posicao] = '0'

    selecionado = ''.join(x)
    
    return selecionado

print(criaMutacao()) 
    

