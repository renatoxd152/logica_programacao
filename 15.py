#Faça um programa que leia um número inteiro E de eleitores de um município, um número inteiro B que representa o número de votos brancos, um número N de votos nulos e um número V de votos válidos. O programa deve calcular e escrever o percentual que cada um representa em relação ao total de eleitores, além da porcentagem de ausentes. Formate sua saída conforme exemplos abaixo.
e = int(input())
b = int(input())
n = int(input())
v = int(input())

on = b + n + v 
num_aus = e - on

a = ((num_aus / e) * 100)
n = (n / e) * 100
b = (b / e) * 100
v = (v / e) * 100



print("Nulos: {:.2f}%".format(n))
print("Brancos: {:.2f}%".format(b))
print("Validos: {:.2f}%".format(v))
print("Ausentes: {:.2f}%".format(a))
