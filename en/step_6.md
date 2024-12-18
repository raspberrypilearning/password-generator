## A random password

A single character isn't very useful.

Improve your program to create a longer password.

To create a password, you will add random characters to it, one at a time.

--- task ---

To start with, your `password` variable should be empty. 

Add this line to your code:

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

password = ''
password = random.choice(chars)
print(password)
--- /code ---

--- /task ---

You want to choose a random character 10 times. 

To do this, add the following line:

--- task ---

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

password = ''
for c in range(10):
password = random.choice(chars)
print(password)
--- /code ---

--- /task ---

--- task ---

Indent (move in) the line to choose a random character, so that it happens 10 times.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 8
---
#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

password = ''
for c in range(10):
    password = random.choice(chars)
print(password)
--- /code ---

--- /task ---

--- task ---

You need to use `+=` to __add__ the new character to the password each time.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 8
---
#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

password = ''
for c in range(10):
    password += random.choice(chars)
print(password)
--- /code ---

--- /task ---

--- task ---

**Test:** Click the **Run** button. 

You should see a password that's 10 characters long.

--- /task ---

--- task ---

Try changing the number `10` to a bigger number and Run your code to see the results!

--- /task ---
