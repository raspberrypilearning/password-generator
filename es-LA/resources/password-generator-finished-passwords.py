#!/bin/python3

import random

print('''
Generador de contraseñas
==================
''')

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

numero = input('¿número de contraseñas? ')
numero = int(numero)

longitud = input('¿longitud de la contraseña? ')
longitud = int(longitud)

print('\naquí están tus contraseñas:')

for con in range(numero):
  contrasena = ''
  for c in range(longitud):
    contrasena += random.choice(caracteres)
  print(contrasena)