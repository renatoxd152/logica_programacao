#Sejam A, B e C os três lados de um triângulo. Faça um programa que leia o valor de três lados de um triângulo A, B e C. Seu algoritmo deve informar se o triangulo é: Escaleno (todos os lados diferentes); Isósceles (possui dois lados iguais); e Equilátero (todos os lados iguais); Não forma triângulo (quando a soma de dois lados é menor que o terceiro lado).
a = int(input())
b = int(input())
c = int(input())

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print("EQUILATERO")
    elif a != b != c != a:
        print("ESCALENO")
    else:
        print("ISOSCELES")
else:
    print("INVALIDO")


    
