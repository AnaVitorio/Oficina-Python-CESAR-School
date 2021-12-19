#9.Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#Fórmula: °C=5×((°F−32)/9)

fahrenheit = float(input("Informe a temperatura em Fahrenheit:"))
celsius = 5 * ((fahrenheit - 32) / 9)
print(f'{fahrenheit} ºF corresponde a {round(celsius, 2)} ºC')