#Faça um programa que leia um número inteiro N que indica a quantidade de números em um conjunto. Em seguida, leia os N números inteiros que compõem esse conjunto. Por fim, o programa deve imprimir dois números, que representam os dois maiores valores encontrados no conjunto, ordenados de forma decrescente.
n =  int(input())
i = 0
maior1 = 0
maior2 = 0
while i < n:
    x = int(input())
    i = i + 1
    if((maior1==0)and(maior2==0)):
        maior1 = x
        maior2 = x
    if maior1 <= x:
        maior2 = maior1
        maior1 = x
print(maior1)
print(maior2)
        
        

