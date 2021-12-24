'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a 
velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
Fórmula:
Tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) = tempo em segundos.'''

tamanho_mb = float(input('Qual o tamanho do arquivo para download em MB?'))
velocidade = float(input('Qual a velocidade do download em Mbps?'))

tempo = (tamanho_mb / (velocidade / 8)) / 60

print(f'O tempo aproximado de download é de {tempo} minutos')