#Faça um programa que leia um número inteiro S que representa uma quantidade de segundos. Seu programma deve imprimir quatro valores inteiros, que representem a quantidade de segundos S em dias, horas, minutos e segundos. Por exemplo, 188365 segundos representam 2 dias, 4 horas, 19 minutos e 25 segundos. Dica: lembre-se dos operadores resto e divisão inteira.
s = int(input())

dia = s // 86400

resto = s % 86400

h = resto // 3600

resto = resto % 3600

minutos = resto // 60

resto = resto % 60



print(dia,h,minutos,resto)
