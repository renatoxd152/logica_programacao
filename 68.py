'''
Faça um programa que leia uma string S e imprima imprima 1 se ela é palíndromo e 0 caso contrário. Uma string é palíndromo se quando lido da esquerda para a direita é igual ao ser lido da direita para a esquerda. 
Exemplos: "arara", "amor e roma". Observações importantes: 1) Seu programa deve desconsiderar caracteres de espaço; 
2) Seu programa NÃO deve criar uma string auxiliar, ou seja, ele deve dizer se a string é palíndromo apenas acessando/consultando seus caracteres.
'''
frase = str(input().strip().upper())
palavra = frase.split()
junto = ''.join(palavra)
tamanho = len(junto)-1
inverso = ''

for i in range(tamanho, -1, -1):
    inverso = inverso + junto[i]
    
if junto == inverso:
    print(1)
else:
    print(0)

