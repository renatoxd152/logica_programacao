#Faça um programa que leia um número inteiro (assuma que esse número terá 4 digitos obrigatoriamente) e inverta esse número. Por fim escreva o número invertido. O seu programa deve apenas manipular números inteiros. Não é permitido usar strings, lista, etc.
n = int(input())
milhar  = n // 1000
centena = (n % 1000) // 100
dezena = (n %100) // 10
unidade = n % 10
soma = (unidade*1000)+(dezena*100)+(centena*10)+(milhar*1)
print(soma)
