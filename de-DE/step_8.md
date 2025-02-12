### Choosing the number of passwords

Instead of always printing 3 passwords, you can allow the user to enter the number of passwords they want.

--- task ---


--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 1
line_highlights: 6-7, 12
---
# !/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('number of passwords?') number = int(number)

length = input('password length?') length = int(length)

for p in range(number): password = '' for c in range(length): password += random.choice(chars) print(password) --- /code ---

--- /task ---
