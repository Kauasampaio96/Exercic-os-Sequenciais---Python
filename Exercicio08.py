 ### Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. ###

valor_h = int(input('Digite o valor da sua hora trabalhada: '))
dias_t = int(input('Digite a quantidade de dias trabalhados no mes: '))

total_h = dias_t * 8

salario = valor_h * total_h

print('O total do seu salário mensal é de: {}'.format(salario))