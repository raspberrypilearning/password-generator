#!/bin/python3

import random

print('''
Passwortgenerator
==================
''')

zeichen='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,? 0123456789'

anzahl = input('Anzahl der Passwoerter?')
anzahl = int(anzahl)

laenge = input('Laenge des Passwortes?')
laenge = int(laenge)

print('\nhier sind deine Passwoerter:')

for pwd in range(anzahl):
  passwort = "
  for c in range(laenge):
    passwort += random.choice(zeichen)
  print(passwort)