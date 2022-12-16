#Faça um programa que leia uma string S, composta apenas por uma palavra. Seu programa deve imprimir os caracteres de S na ordem inversa que aparecem em S, separados por espaço.
string = input()
i = len(string)
nova_string = ''
while i:
    i = i - 1
    nova_string += string[i]
for x in nova_string:
    espaco = ''
    print(x,espaco, end = '')

        
    
