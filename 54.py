'''
Faça um programa que leia um número inteiro não negativo N e imprima "S" se ele é palíndromo e "N" caso contrário. Um número é palíndromo quando lido da esquerda para a direita é igual ao ser lido da direita para a esquerda. Exemplos: 37173, 1221.

Obs: Faça seu programa utilizando apenas números inteiros. Não é permitido converter o número para string.
'''
numero = int(input())
aux = numero
numero_invertido = 0
while numero > 0:
    digito = numero % 10
    numero_invertido *= 10
    numero_invertido += digito
    numero //= 10

if aux == numero_invertido:
    print("S")
else:
    print("N")
