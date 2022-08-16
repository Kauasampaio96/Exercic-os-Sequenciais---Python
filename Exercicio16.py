'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''


print('----- LOJA DE TINTAS -----')

area = float(input('Digite o tamanho da area a ser pintada em m2: '))

cober_em_litros = area / 3

qtde_latas_de_tinta = cober_em_litros / 18

preço_lata = qtde_latas_de_tinta * 80

print(f'Para essa area será preciso, {qtde_latas_de_tinta:.2f} latas de tintas, e isso custará: R$ {preço_lata:.2f}')





