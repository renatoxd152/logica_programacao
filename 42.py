#Faça um programa que leia um número inteiro N e imprima a soma de todos os fatoriais entre 0 e N (inclusive N). Não utilize bibliotecas matemáticas.
n = int(input())
soma = 0
for c in range(1, n + 1):
    prod = 1
    for d in range(c, 0, -1):
        prod *= d
    soma += prod
soma = soma + 1
print(soma)
