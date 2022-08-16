'''
Faça um programa de caixa eletrônico com as opções: 
(1) consulta saldo, 
(2) saque, 
(3) depósito e 
(4) sair.
 O saldo inicial é sempre de R$ 0,00. A cada saque ou depósito atualize o 
 valor do saldo e apresente-o na tela

'''

'''
####### LÓGICA ############
1(dados necessários) - um numero que ira corresponder a função no sistema e interação com essas funções
2(oq irei fazer com os dados) - Somar, diminuir ou printar os dados colhidos do usuário
3(restrições / regras) - navegação somente por Somente numeros
4 (resultado esperado) - Navegação fluida e compreensiva do usuario durante o uso do programa


5:
'''

print('----------- CAIXA ELETRONICO -----------\n')

saldo = 0


while True:
    '''comando_adm = input('Deseja para o sistema [ADM]')

    if comando_adm == 'S':
        break
    
    else:
    
    '''
    entrada = input(f'Olá, bem-vindo ao banco ABCDE\n\n Digite para cada ação:\n\n [1] - Consulta de saldo\n [2] - Realizar Saque\n [3] - Realizar Depósito\n [4] - Sair do Sitema\n\n SELECIONE A OPÇÃO:.....  ')



# tratando respostas do usuário e possíveis erros
    
    if not entrada.isnumeric():
        print('Por favor Digite apenas das opções para prosseguir')
    

# repostas certas

    if entrada == '1':
        print(f'\n\nSeu saldo é de R$ {saldo:,}\n\n')
      

    elif entrada == '2':
        saque_valor = int(input('Digite o valor do SAQUE que você quer SACAR na conta: '))
        saldo -=  saque_valor
        print(f'\n\nFoi SACADO R$ {saque_valor} da sua conta\n\n')

    elif entrada == '3': 
        deposito_valor = int(input('Digite o valor do DEPOSITO que você quer depositar na conta: '))

        saldo +=  deposito_valor
        print(f'\nFoi DEPOSITADO R${deposito_valor} na sua conta\n\n')


    elif entrada == '4': 
        print('\nObrigado por usar nosso sistema, seu saldo será zerado, volte sempre!\n\n')  
        break  


    
    

