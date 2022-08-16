'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

'''
altura_homem = float(input('Digite sua altura em m (1.60) HOMEM: '))
altura_mulher = float(input('Digite sua altura em m (1.60) MULHER: '))

form_h = (72.7 * altura_homem) - 58
form_m = (62.1 * altura_mulher) - 44.7

print(f'Seu peso ideal (HOMEM) é {form_h:.2f}')
print(f'Seu peso ideal (MULHER) é {form_m:.2f}')


