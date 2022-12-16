'''
Faça um programa que leia as dimensões N e M de uma matriz A, representando o número de linhas e colunas respectivamente. Após isso, leia N x M valores em apenas uma linha, colocando-os na matriz A. 
Por fim, o programa deve imprimir a soma de cada coluna da matriz.
'''
d = input().split()
entrada = input().split()
lista = []
linha = []
matriz = []

for i in range (len(entrada)):
    elem = int(entrada[i])
    lista.append(elem)

n_linhas = int(d[0])
n_colunas = int(d[1])
    
i = 0    
for x in range(n_linhas):
    linha = []
    for y in range(n_colunas):
        linha.append(lista[i])
        i = i + 1
    matriz.append(linha)

   
for c in range(n_colunas):
    soma = 0
    for l in range(n_linhas):
        soma += matriz[l][c]
    print(soma)


    

