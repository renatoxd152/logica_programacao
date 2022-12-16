'''
Faça um programa que leia um conjunto de valores que correspondem as idades de pessoas de uma comunidade. Quando o valor fornecido for um número negativo, significa que não existem mais idades para serem lidas. Após a leitura, seu programa deve informar:

A média das idades das pessoas (com duas casas decimais)
A quantidade de pessoas maiores de idade
A porcentagem de pessoas idosas (considere quem uma pessoa idosa tem mais de 75 anos) (com duas casas decimais)
'''
n = -1
x = 0
media = 0
soma = 0
cont = 0
idade = 0
idoso = 0
while x > n:
    x = int(input())
    if x > 0:
        soma = soma + x
        cont = cont + 1
        if x > 18:
            idade = idade + 1
        if x > 75:
            idoso = idoso + 1
if cont > 0:     
    porc = (idoso / cont)*100        
    media = soma / cont
else:
    porc = 0

print("{:.2f}".format(media))
print(idade)
print("{:.2f}%".format(porc))
    
