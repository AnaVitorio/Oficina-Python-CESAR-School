'''
16.Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, 
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:

 + Salário Bruto : R$
 - IR (11%) : R$
 - INSS (8%) : R$
 - Sindicato (5%) : R$
 = Salário Liquido : R$
'''
ganho_por_hora = float(input('Quanto você ganho por hora?'))
horas_traba = int(input('Quantas horas você trabalha por mês?'))

sal_bruto = ganho_por_hora * horas_traba
ir = (sal_bruto * 11) / 100
inss = (sal_bruto * 8) / 100
sindicato = (sal_bruto * 5) / 100
sal_liquido = sal_bruto - ir - inss - sindicato

print(f'O seu salário bruto é de R${sal_bruto}')
print(f'Desconto do Imposto de Renda: R${ir}')
print(f'Desconto do INSS: RS{inss}')
print(f'Desconto para o Sindicato: R${sindicato}')
print(f'O seu Salário Líquido é de R${sal_liquido}')
