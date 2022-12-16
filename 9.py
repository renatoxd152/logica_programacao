#Faça um programa que leia três números reais A, B e C de uma equação do segundo grau, considerando: Ax^2 + Bx + C. Seu programa deve calcular e imprimir as as raízes da equação. Assuma que delta sempre será positivo.
a = float(input())
b = float(input())
c = float(input())

delta = b ** 2 - 4 * a * c
raiz = delta ** 0.5

x1 = ( -b + raiz ) / ( 2 * a )
x2 = ( -b - raiz ) / ( 2 * a )

if delta > 0 :
          print("{:.2f}".format(x1))
          print("{:.2f}".format(x2))
else:
    print("")
