#15.Faça um programa que receba do usuario uma string. O programa imprime a string sem suas vogais.
string = str(input('Digite qualquer mensagem:'))
vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for letra in vogais:
    if letra in string:
        sem_vogais = string.replace(letra, ' ')
        string = sem_vogais
print(string)
