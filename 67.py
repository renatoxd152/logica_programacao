#Faça um programa que leia uma string S e um caractere C. Ao fim escreva o número de vezes que o caractere C aparece na string S.
string = input()
caractere = input()
cont = 0
for i in string:
    if i == caractere:
        cont = cont + 1
print(cont)
    
   
    
