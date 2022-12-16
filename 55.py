#Faça um programa que leia dados de temperatura durante uma semana (7 leituras), armazenando em uma lista. Após isso, seu programa deve imprimir quantos dias dessa semana a temperatura esteve acima da média.
entrada = input().split()
soma = 0
lista = []
cont = 0
for i in range(7):
    temp = int(entrada[i])
    lista.append(temp)
    soma = soma + temp

media = soma / 7 
for i in range(len(lista)):
    if lista[i] > media:
        cont = cont + 1
print(cont)
    
    

    
    



    














    




    

    
    
    

   
    
        
