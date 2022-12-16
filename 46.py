#Faça um programa que leia um número inteiro positivo N e imprima a soma dos dígitos desse número. Por exemplo, se a entrada for 358, a saída será 16 (3 + 5 + 8). Obs: Não é permitido transformar os números em strings, ou seja, resolva o problema apenas utilizando operações matemáticas válidas.
n = int(input())
s = 0
while n:
    s += n % 10
    n = n // 10
print(s)
