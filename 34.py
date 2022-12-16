'''
Um matemático italiano da idade média conseguiu modelar o ritmo de crescimento da população de coelhos através de uma sequência de números naturais que passou a ser conhecida como Sequência de Fibonacci. O n-ésimo número da sequência de Fibonacci Fn é dado pela seguinte formula: Fi = Fi-1 + Fi-2. O resultado é a sequência {1, 1, 2, 3, 5, 8, 13, 21, ...}.

Faça um programa que leia um número inteiro positivo N e imprima os N primeiros números da sequência de Fibonacci, todos em uma linha separados por espaço.
'''
n =int( input())
t1 = 1
t2 = 1
i = 0

print("{} {} ".format(t1,t2),end="")

cont = 3

while cont <= n:
    t3 = t1 + t2
    print ("{}".format(t3),'',end="")
    t1 = t2
    t2 = t3
    cont +=1

  
