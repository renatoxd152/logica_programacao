'''
Você está responsável pelo bolo de aniversário da sua priminha e decidiu que o bolo terá uma vela para cada ano da idade total dela. Quando ela assopra as velas, ela só é capaz de apagar apenas as velas mais altas. Sua tarefa é fazer um programa que leia a idade A da sua sobrinha e a altura das velas. Após isso, seu programa deve imprimir a quantidade de velas que ela vai conseguir apagar.

Por exemplo, se sua sobrina está fazendo 4 anos e o bolo possui 4 velas de tamanhos 4, 4, 1, 3, então ela só vai conseguir apagar as duas mais altas, de tamanho 4. Portanto, a resposta deve ser 2.
'''
idade = int(input())
cont = 0
maior1 = 0
maior2 = 0
i = 0
if idade > 0:
    while cont < idade:
        vela = int(input())
        cont = cont + 1
        if((maior1==0)and(maior2==0)):
            maior1 = vela
            maior2 = vela
        if maior1 <= vela:
            maior2 = maior1
            maior1 = vela
            i = i + 1
    print(i)
