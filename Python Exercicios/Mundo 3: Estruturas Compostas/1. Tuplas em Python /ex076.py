'''
Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
No final, mostre uma listagem de preços, organizando os dados em forma tabular
'''

produtos = ('Feijão', 5.50, 'Arroz', 3.5, 'Macarrão', 3, 'Bolo', 10, 'Pizza', 25)
ponto = '.'

print('-' * 36)

for i in range(0, len(produtos)-1, 2):
    print('{0:.<24}'.format(produtos[i]), end='')
    print('R$ {0:>7.2f}'.format(produtos[i+1]))

print('-' * 36)
