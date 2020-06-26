#!/bin/python3

import random

print('''
مولد كلمة السر
==================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

العدد=input('عدد كلمة المرور؟')
العدد = int(العدد)

الطول = input('طول كلمة المرور؟')
الطول = int(الطول)

print('\nهنا كلمات المرور الخاصة بك:')

(العدد): for pwd in range:
  كلمة المرور = ''
  for c in range(الطول):
    كلمة المرور + = random.choice (chars)
  print(كلمة المرور)