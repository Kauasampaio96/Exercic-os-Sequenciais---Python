 ### Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. ###

lado_quadrado = int(input('Digite o valor do lado do quadrado: '))
area = lado_quadrado**2
dobro_da_area = area * 2

print('A área do quadrado é de {}, e o dobro dessa área é de {}'.format(area,dobro_da_area))