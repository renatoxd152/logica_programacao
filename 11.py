#Faça um programa que leia o salário fixo de um vendedor e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 18% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês.
sal = float(input())

vendas = float(input())

porc = (vendas * 18) / 100

novo_sal = sal + porc

print("{:.2f}".format(novo_sal))
