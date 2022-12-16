#Faça um programa que leia um número inteiro positivo N. Após isso o programa deve ler N números inteiros e ao final da leitura imprimir o maior, menor e a soma dos números lidos.
n = int(input())
cont = 0
maior = 0
soma = 0

while cont < n :
    x = int(input())
    cont = cont + 1
    soma = soma + x
    
    if cont == 1:
        maior = menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x

print(maior)
print(menor)
print(soma)
        
    
    

