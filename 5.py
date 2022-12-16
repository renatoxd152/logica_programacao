#Faça um programa que leia dois números inteiros. Após isso, seu programa deve imprimir o resultado das seguintes operações: 1) o valor da divisão real do primeiro número lido pelo segundo (imprimir com duas casas decimais); 2) o valor da divisão inteira do primeiro pelo segundo (imprimir como número inteiro); 3) o valor do resto da divisão do primeiro pelo segundo (imprimir como número inteiro).
# ENTRADA:
a = int(input())
b = int(input())

# PROCESSAMENTO:
# ...
res = a / b
div_int = a//b
resto= a % b

# SAIDA:
print("{:.2f}".format(res))
print(div_int)
print(resto)
