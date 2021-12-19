#10.Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#°F=(°C×9/5)+32
celsius = float(input("Informe a temperatura em Celsius:"))
fahrenheit = (celsius * 9 / 5) + 32
print(f'{celsius} ºC corresponde a {round(fahrenheit, 2)} ºF')