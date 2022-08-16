'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)

'''

print('----- TEMPO DE DOWNLOAD -----')

tam_mb = float(input('Digite o tamanho do arquivo a ser baixado em MB: '))

vel = float(input('Digite a velocidade da sua internet em MBps: '))

megabytes = vel / 8

form = tam_mb / megabytes

minutos = form / 60

print(f'Um arquivo de {tam_mb} MB levará um tempo de {minutos:.1f} minutos, ou {form:.0f} segundos para ser beixado, na velocidade de {vel}Mbps')










