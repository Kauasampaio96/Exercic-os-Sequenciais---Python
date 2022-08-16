'''

Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo.


'''


user_1 = int(input('Digite um número: '))
user_2 = int(input('Digite outro número: '))
user_3 = float(input('Digite um número com virgula: '))


form_1 = (user_1 * 2) * (user_2/2)

form_2 = (user_1 * 3) + user_3

form_3 = user_3 ** 3

print(f'o produto do dobro do primeiro com metade do segundo = {form_1}\n a soma do triplo do primeiro com o terceiro. = {form_2}\n o terceiro elevado ao cubo. = {form_3}')
 

