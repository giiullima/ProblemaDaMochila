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
    avaliacao.sort(reverse=True, key=lambda x: x[1])
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


    

