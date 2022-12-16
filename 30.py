#Faça um programa que leia uma sequência de números inteiros do usuário até que ele digite o valor zero. Quando o valor zero for digitado, o programa deve imprimir o resultado em três linhas: 1ª linha) Soma dos valores pares da sequência; 2ª linha) Soma dos valores ímpares da sequência; 3ª linha) soma de todos os valores da sequência.
n = 1
par = 0
impar = 0
soma = 0

while n != 0:
    n = int(input())
    if n % 2 == 0:
        par = par + n
        
    else:
        impar = impar + n
    soma = soma + n       
print(par)
print(impar)
print(soma)   
