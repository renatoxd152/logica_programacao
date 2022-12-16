#Faça um programa que leia dois números inteiros e imprima o máximo divisor comum (MDC) entre eles. Dica: pesquise sobre o algoritmo de euclides.

x1 = int(input())
x2 = int(input())
anterior = x1
atual = x2

resto = atual % anterior
while resto != 0:
    resto = anterior % atual
    anterior = atual
    atual = resto
    
print(anterior)
