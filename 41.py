#Faça um programa que leia um número inteiro N e imprima a soma de todos os números primos entre 1 e N (inclusive N).
def testaPrimo(num):
   
	if (num == 1):
	 	return False
	for d in range(2,(int)(num/2)+1):
		if (num % d == 0):
			return False
	else:
	 	return True
soma = 0
n = int(input())
for i in range(1, n+1):
	if (testaPrimo(i)):
		 soma += i

else:
	print(soma)
