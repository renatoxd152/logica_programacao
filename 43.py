#Faça um programa que leia dois números inteiros positivos A e B e faça o cálculo de multiplicação de A e B usando apenas a operação de soma. Imprima o resultado ao final.
a = int(input())
b = int(input())
cont = 0
mult = 0
while cont < b:
    cont = cont + 1
    mult = mult + a
print(mult)
