'''
Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros. A cada valor lido, o programa deve inserir em uma lista A se o valor for par e em uma lista B se o valor for ímpar.
Ao fim, escreva as duas listas resultantes, na primeira linha a lista A e na segunda a lista B.
'''
n = int(input())
entrada = input().split()
lista = []
par = []
impar = []

for i in range(n):
    elem = int(entrada[i])
    lista.append(elem)
    
for i in lista:
    if i % 2 == 0:
        par.append(i) 
    else:
        impar.append(i)

for x in range(len(par)):
    espaco = ''
    novo_par = par[x]
    print(novo_par,espaco,end = '')
print()
for y in range(len(impar)):
    espaco = ''
    novo_impar = impar[y]
    print(novo_impar,espaco,end = '')
    
    
    

