#!/bin/python3

import random

print('''
Generatore di password
==================
''')

caratteri = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

numero = input('numero di password?')
numero = int(numero)

lunghezza = input('lunghezza della password?')
lunghezza = int(lunghezza)

print('\necco le tue password:')

for pwd in range(numero):
  password = ''
  for c in range(lunghezza):
    password += random.choice(caratteri)
  print(password)