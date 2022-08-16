'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.


'''


valor_hora = float(input('Digite quanto ganha por hora: '))
horas_trabalhadas = float(input('Digite quantas horas você trabalha por mês: '))

total_salario = valor_hora * horas_trabalhadas

imposto = 11 * total_salario / 100 
inss = 8 * total_salario / 100 
sindi = 5 * total_salario / 100 

sal_liquido = total_salario - imposto - inss - sindi

print(f'O seu salário mensal é de {total_salario} e foi descontado do seu salário: \n - IR (11%) : R$ {imposto} \n - INSS (8%) : R$ {inss} \n - Sindicato (5%) : R$ {sindi} \n - SALÁRIO LIQUIDO : R$ {sal_liquido}')






