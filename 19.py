#Um motorista de Uber estipula o preço de uma determinada viagem dada a quantidade de quilômetros percorrida. Para viagens de até X km, é cobrado um valor R$ V1 por km. Acima de Y km, é cobrado o valor R$ V2. Faça um programa que leia X, V1, V2 e a quantidade de quilômetros A da viagem e imprima o valor total com duas casas decimais.
x =  float(input())
v1 = float(input())
v2 = float(input())
a = float(input())

if a < x :
    valor = a * v1
    print("{:.2f}".format(valor))
elif a > x:
    valor = a * v2
    print("{:.2f}".format(valor))
