#Em épocas de crise, comerciantes estão oferecendo descontos para aumentarem suas vendas. Faça um programa que leia o valor total da compra e um valor de desconto (de 0 a 100, representando a porcentagem de desconto). O programa de escrever o valor da compra com o desconto aplicado. Escreva a saída com duas casas decimais.
a = float(input())
b = float(input())

desc = (a * b) / 100
res = a - desc

print("{:.2f}".format(res))
