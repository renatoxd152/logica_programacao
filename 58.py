'''
Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros. Em seguida leia um número inteiro X. 
Ao fim escreva a primeira posição na lista em que o valor X foi encontrado. Se X não estiver na lista, escrever -1.
'''
n = int(input())
entrada = input().split()
lista = []
for i in range(n):
    valor = int(entrada[i])
    lista.append(valor)
x = int(input())
indice = -1
for i in range(len(lista)):
    if lista[i] == x:
        indice = i
print(indice)



        
    
    
