#Sabe-se que uma lata de tinta tem um custo C e é capaz de pintar uma área de M metros quadrados. Faça um programa que leia a largura L, a altura A de uma parede, o valor C de uma lata de tinta e o rendimento M desta lata. Após isso, imprima quantas latas de tintas são necessárias e o custo total (com duas casas decimais). Assuma que não é possível comprar lata de tinta fracionada.
import math
l = float(input())
a = float(input())
c = float(input())
m = float(input())

area = l * a
qtd_latas = area / m
qtd_latas = math.ceil(qtd_latas)

custo_total = qtd_latas * c

print(qtd_latas)
print("{:.2f}".format(custo_total))



