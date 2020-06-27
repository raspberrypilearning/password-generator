#!/bin/python3

import random

print('''
Gerador de Senhas
==================
''')

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

numero = input('número de senhas?')
numero = int(numero)

comprimento = input('comprimento da senha?')
comprimento = int(comprimento)

print('\n' + 'aqui estão suas senhas:')

for senha in range(numero):
  senha = ''
  for c in range(comprimento):
    senha += random.choice(caracteres)
  print(senha)