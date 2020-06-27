#!/bin/python3

import random

print('''
パスワード生成ツール
==================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('パスワードの数は?')
number = int(number)

length = input('パスワードの文字数は?')
length = int(length)

print('\n'+'これがあなたのパスワードです。')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)