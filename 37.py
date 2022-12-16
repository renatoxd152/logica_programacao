#Faça um programa que leia um número inteiro positivo N. Após isso o programa deve ler N números inteiros e ao final da leitura imprimir o maior deles.
n = int(input())
cont = 0
maior = 0
while cont < n :
    cont = cont + 1
    x = int(input())
    if x > maior:
        maior = x
print (maior)
   
    

