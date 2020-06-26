#!/bin/python3

import random

print('''
مولد كلمة السر
==================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = إدخال ("عدد كلمات المرور؟")
number = int(number)

length = input('طول كلمة المرور؟')
length = int (length)

print('\nهنا كلمات المرور الخاصة بك:')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)