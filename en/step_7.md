## Choosing a password length

Some websites require passwords to be a certain length. 

Allow the user to choose the length of their password.

--- task ---

Ask the user to input a password length, and store it in a variable called `length`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 6
---
#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

length = input('password length?')

password = ''
for c in range(10):
    password += random.choice(chars)
print(password)
--- /code ---

--- /task ---

--- task ---

Use `int()` to turn the user's input into a whole number.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 7
---
#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

length = input('password length?')
length = int(length)

password = ''
for c in range(10):
    password += random.choice(chars)
print(password)
--- /code ---

--- /task ---

--- task ---

Use your `length` variable to repeat as many times as the user entered.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 10
---
#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

length = input('password length?')
length = int(length)

password = ''
for c in range(length):
    password += random.choice(chars)
print(password)
--- /code ---

--- /task ---

--- task ---

**Test:** Click the **Run** button. 

The password created should be the length entered by the user.

--- /task ---
