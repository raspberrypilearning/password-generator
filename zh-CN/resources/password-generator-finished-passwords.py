#!/bin/python3

import random

print('''
密码生成器
==================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('密码数量?')
number = int(number)

length = input('密码长度?')
length = int(length)

print('\n'+'以下是你的密码：')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)