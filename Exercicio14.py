'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
'''

peso_peixe = int(input('Digite o peso do peixe pesado em KG: '))

if peso_peixe > 50:
    regulamento_excesso = peso_peixe - 50

    multa = regulamento_excesso * 4

    print(f'O peixe pescado EXCEDEU o limite estabelecido pelo governo, {regulamento_excesso} KGs além do limite\no valor da multa é de {multa}')

else:
    print('O peixe está nos padroes exigidos pelo governo, Boa pesca!')





