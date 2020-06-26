#!/bin/python3

import random

print('''
Wachtwoordgenerator
===================
''')

tekens = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

aantal = input('aantal wachtwoorden?')
aantal = int(aantal)

lengte = input('wachtwoordlengte?')
lengte = int(lengte)

print('\nhier zijn je wachtwoorden:')

for ww in range(aantal):
  wachtwoord = ''
  for c in range(lengte):
    wachtwoord += random.choice(tekens)
  print(wachtwoord)