#Faça um programa que leia um valor inteiro N. Após isso, leia N valores inteiros. Em seguida, seu programa deve imprimir os N valores na ordem inversa que foram lidos.
n = int(input())
entrada = input().split()
v = []
i = 0
j = len(entrada)-1

for y in range(n):
    elem = int(entrada[y])
    v.append(elem)
while i < j:
    aux = v[i]
    v[i] = v[j]
    v[j] = aux
    i = i + 1
    j = j - 1
for item in v:
    print(item, end =' ')
print()

         

    
