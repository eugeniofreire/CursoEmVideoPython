'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final, mostre:
    a. quantas vezes apareceu o valor 9
    b. em que posição foi digitado o primeiro valor 3
    c. quais foram os numeros pares
'''

tupla = (int(input()), int(input()), int(input()), int(input()))

print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O valor 3 esta na {tupla.index(3) + 1}º posição')
else:
    print('O valor 3 nao foi digitado')

print('Números pares: ', end='')

for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
