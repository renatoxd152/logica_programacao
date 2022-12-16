#Faça um programa que leia dois números inteiros positivos A e B, onde A é a base e B é o expoente de uma potência. Após isso, calcule e imprima o valor de A elevado a B. Não utilize bibliotecas matemáticas. No caso de python, não é permitido usar o operador **. Faça sua solução utilizando laço de repetição.
a = int(input())
b = int(input())
pot = 1
cont = 0


while cont < b:
    cont = cont + 1
    pot = pot * a
print(pot)
    
