#Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros, inserindo-os em uma lista de tamanho N. Em seguida, seu programa deve imprimir o maior valor informado e a posição dele na lista. Se o maior valor foi informado mais de uma vez, imprimir a posição do primeiro.
n = int(input())
entrada = input().split()
lista = []
for i in range(n):
    valor = int(entrada[i])
    lista.append(valor)
maior = 0
indice_maior = 0
for i in range(len(lista)):
    if i == 0:
        maior = lista[i]
    elif lista[i] > maior:
        maior = lista[i]
        indice_maior = i 
print(maior)
print(indice_maior)
