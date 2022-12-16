#Faça um programa que leia os coeficientes a, b e c de uma equação do segundo grau ax² + bx + c. Após isso, calcule e imprima a soma das raízes da equação. Se as raízes não forem reais, imprima nan (use print(math.nan))
import math
a = float(input())
b = float(input())
c = float(input())

delta = (b**2) - 4 * a * c
raiz = delta ** 0.5

x1 = (- b + raiz) / (2 * a)
x2 = (- b - raiz) / (2 * a)

soma = x1 + x2

if delta > 0 :
    print("{:.2f}".format(soma))
elif delta == 0 :
    raiz = (- b ) / (2 * a)
    print("{:.2f}".format(raiz))
else:
    print(math.nan)

    
    
