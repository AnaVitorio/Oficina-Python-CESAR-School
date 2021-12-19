#12.Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal em Kg usando a seguinte fórmula:
#peso_ideal=(72.7×altura)−58

altura = float(input('Informe a altura:'))
peso_ideal = (72.7 * altura) - 58
print(f'O peso ideal é: {round(peso_ideal, 2)} Kg')
