#4.Faça um programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input('Insira a 1º nota:'))
nota2 = float(input('Insira a 2º nota:'))
nota3 = float(input('Insira a 3º nota:'))
nota4 = float(input('Insira a 4º nota:'))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"Sua média é igual a {media}")


# Outra maneira de se calcular a média

# cont = 1
# lista_notas = []
# while cont <= 4:
#     nota = float(input(f'Insira a {cont}º nota:'))
#     lista_notas.append(nota)
#     cont = cont + 1
# media = sum(lista_notas) / 4
# print(f"Sua média é igual a {media}")



