#!/bin/python3

import random

print('''
Γεννήτρια Κωδικών Πρόσβασης
========================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! @ £ $% ^ & * ()., 0123456789'

number = input ("πλήθος κωδικών πρόσβασης;")
number = int (number)

length = input ('μήκος κωδικού πρόσβασης;')
length = int(length)

print('\n'+'να οι κωδικοί πρόσβασης:')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)