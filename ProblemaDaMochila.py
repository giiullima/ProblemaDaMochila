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

def avaliacao():
    populacao = criaPopulacao()
    kgProduto=[7, 8, 4, 10, 4, 6, 4]
    benefProduto = [5, 8, 3, 2, 7, 9, 4]
    peso = []
    fitness =[]
    valorP = 0
    valorF = 0
    print(populacao)
    
    for i in populacao:
        for x in range(7):
            if i[x] == '1':
               valorP +=kgProduto[x]
               valorF +=benefProduto[x]
               
        fitness.append(valorF)
        peso.append(valorP)
        valorP = 0
        valorF = 0

    return fitness

print(avaliacao())

