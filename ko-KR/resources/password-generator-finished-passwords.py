#!/bin/python3

import random

print('''
비밀번호 생성기
==================
''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('비밀번호의 개수를 입력하세요.')
number = int(number)

length = input('비밀번호의 길이를 입력하세요.')
length = int(length)

print('\n' + '생성된 비밀번호입니다:')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)