#8.Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganho_hora = float(input('Quanto você ganha por hora?'))
hora_trabalhada = int(input('Quantas horas você trabalha por mês?'))
salario_mes = ganho_hora * hora_trabalhada
print(f'O seu salário por mês é de R$ {salario_mes} reais')