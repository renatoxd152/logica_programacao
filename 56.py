#Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros. Em seguida, seu programa deve imprimir os N valores na ordem que foram lidos.
n = int(input())
entrada = input()
entrada = entrada.split()
lista = []
for i in range(n):
    elem = int(entrada[i])
    espaco = ''
    print(elem,espaco, end = '')
    
    

