'''
Na matemática, um número primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

Faça um programa que leia um número inteiro positivo N e imprima 1 se ele for primo e 0 caso contrário.
'''

n = int(input())
cont = 0
total = 0
for c in range(1, n+1):
    if n % c == 0:
        total = total + 1
if total == 2:
    print(1)
else:
    print(0)
           
        
    
    
        

