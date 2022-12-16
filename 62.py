'''
Faça um programa que leia um valor inteiro N. Após isso, leia duas listas A e B de tamanho N e coloque a soma das duas listas em uma terceira lista C. Por exemplo C[0] = A[0] + B[0], C[1] = A[1] + B[1]. 
Por fim, imprima a lista resultante C.
'''
n = int(input())
a = input().split()
b = input().split()
c = []
for i in range(n):
    elem = int(a[i])
    elem2 = int(b[i])
    s = elem + elem2
    c.append(s)
for item in c:
    print(item, end = ' ')

    
