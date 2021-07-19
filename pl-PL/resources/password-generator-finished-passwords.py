#!/bin/python3

import random

print('''
Generator haseł
==================
''')

znaki = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

ilosc = input('Podaj liczbę haseł: ')
ilosc = int(ilosc)

dlugosc = input('Podaj długość hasła: ')
dlugosc = int(dlugosc)

print('\n' + 'Oto Twoje hasła:')

for hsl in range(ilosc):
  haslo = ''
  for z in range(dlugosc):
    haslo += random.choice(znaki)
  print(haslo)