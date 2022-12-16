#Faça um programa que leia um número inteiro e positivo N. Após isso leia N números inteiros. Ao fim, imprima 1 se a sequência de números lidos estão ordenados em forma crescente e -1 se estão ordenados de forma decrescente. Se não estão ordenados, imprima 0. Considere que uma sequência de tamanho N é crescente quando X1 <= X2 <= ... <= XN e decrescente quando X1 >= X2 >= ... >= XN. No caso desse exercício, se todos os valores lidos forem iguais, considere como um segmento crescente.
decrescente = 0
crescente = 0

quantidade = int(input())

for i in range(0, quantidade):

    ultimo_numero = int(input())

    if i == 0:
        primeiro_numero = ultimo_numero
    else:
        if primeiro_numero >= ultimo_numero:
            decrescente += 1

        if primeiro_numero <= ultimo_numero:
            crescente += 1

        primeiro_numero = ultimo_numero

if quantidade == (crescente+1):
    print(1)
elif quantidade == (decrescente+1):
    print(-1)
else:
    print(0)
    




    


