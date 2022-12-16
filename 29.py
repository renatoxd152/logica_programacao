#Faça um programa que leia dois números inteiros X e Y e imprima todos os números de X até Y, seguidos nos números de Y até X. Se X for maior que Y, imprima INVALIDO.
n = int(input())
m = int(input())
soma = 0
while n <= m :
    soma=soma+n
    n=n+1
print(soma)
    
    

