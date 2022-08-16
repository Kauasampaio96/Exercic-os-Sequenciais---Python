 ### Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. ###

temp_f = int(input('Digite a temperatura em Fahrenheit: '))

temp_c = 5 * ((temp_f-32) / 9)

print('{}°F em graus celsius é {:.0f}°'.format(temp_f, temp_c))

