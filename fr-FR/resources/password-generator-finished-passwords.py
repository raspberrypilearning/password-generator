#!/bin/python3

import random

print('''
Générateur de mot de passe
======================
''')

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

nombre = input('nombre de mots de passe?')
nombre = int(nombre)

longueur = input('longueur du mot de passe?')
longueur = int(longueur)

print('\nvoici tes mots de passe:')

for pwd in range(nombre):
  motdepasse = ''
  for c in range(longueur):
    motdepasse += random.choice(caracteres)
  print(motdepasse)