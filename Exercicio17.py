'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

'''

print('----- LOJA DE TINTAS -----')

area = float(input('Digite o tamanho da area a ser pintada em m2: '))

cober_em_litros = area / 6

qtde_latas_de_tinta = cober_em_litros / 18

qtde_galoes_de_tinta = cober_em_litros / 3.6 

mist_galao = qtde_galoes_de_tinta / 2 

mist_lata = qtde_latas_de_tinta / 2 

preço_lata = qtde_latas_de_tinta * 80

preço_lata_mist = mist_lata * 25

preço_galao = qtde_galoes_de_tinta * 25

preço_galao_mist = mist_galao * 25

print(f'Para essa área será preciso:\n Em latas de 18 Litros {qtde_latas_de_tinta:.2f} latas que custará R${preço_lata:.2f} \n Em Galões de 3,6 litros {qtde_galoes_de_tinta:.2f} galões que custará R${preço_galao:.2f} \n Caso queira misturar as quantidades: será preciso {mist_lata:.2f} latas de tintas, {mist_galao:.2f} galoes de tintas, e sairá (R$ {preço_lata_mist:.2f} de lata de tintas), (R$ {preço_galao_mist:.2f} de galoes de tinta) = R$ {preço_galao_mist + preço_lata_mist:.2f}')








