'''
Faça um programa que leia duas strings A e B, e imprima 1 se A e B são anagramas e 0, caso contrário. Anagrama é a transposição de letras de palavra ou frase para formar outra palavra ou frase diferente. 
Por exemplo: "algoritmo" e “logaritmo” são anagramas. Seu programa deve desconsiderar caracteres de espaço.
'''
string1 = list(input().replace(" ", ""))
string2 = list(input().replace(" ", ""))

if len(string1) != len(string2):
    aux = 0
y = {}
for x in string1:
    if x in y:
        y[x] += 1 
    else:
        y[x] = 1 
    
for x in string2:
    if x in y:
        y[x] -= 1 
    else:
        y[x] = 1 
    
for i in y:
    if y[i] != 0:
        aux = 0
    else:
        aux = 1
print(aux)
        


