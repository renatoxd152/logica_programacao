'''Faça um programa que leia um número natural N e imprima o número harmônico de ordem N. Um número harmônico H é definido por:

H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N

Imprima o resultado com 4 casas decimais.'''
n = int(input())
den = 1
h = 0



while den <= n:
    h = h +  (1/ den)
    den = den + 1
print("{:.4f}".format(h))
    
   
    


   
