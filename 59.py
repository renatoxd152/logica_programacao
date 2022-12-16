#Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros. Em seguida leia um número inteiro X. Ao fim escreva o número de vezes que o número X foi lido do usuário.
n = int(input())
entrada = input()
entrada = entrada.split()


x = int(input())
cont = 0 
for i in range(n):
    elem = int(entrada[i])
    if elem == x:
        cont = cont + 1
print(cont)


    


