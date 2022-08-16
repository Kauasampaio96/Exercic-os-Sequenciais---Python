 ### Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

# (0 °C × 9/5) + 32 = 32 °F


user = float(input('Digite a temperatura em Celsius: '))

form = (user * 9 / 5) + 32

print(f'{user} graus Celsius em Fahrenheit é {form}°F')


