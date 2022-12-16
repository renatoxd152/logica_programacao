#Faça um algoritmo que leia 3 valores inteiros A, B e C. Coloque-os em ordem crescente (ou seja, ao final A deve armazenar o menor valor, C o maior e B o valor do meio). Utilize o modelo abaixo apresentado no final do exercício, modificando apenas o processamento
a = int(input())
b = int(input())
c = int(input())

if a >= b and a > c and b >= c:
    print(c)
    print(b)
    print(a)
    
elif a >= b and a >= c and c >= b:
    print(b)
    print(c)
    print(a)

elif b >= a and b >= c and a >= c:
    print(c)
    print(a)
    print(b)
elif b >= a and b >= c and c >= a:
    print(a)
    print(c)
    print(b)
elif c >= a and c >= b and  a >= b :
    print(b)
    print(a)
    print(c)
elif c >= a and c >= b and  b >= a :
    print(a)
    print(b)
    print(c)
    

