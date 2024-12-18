## Lots of passwords

Allow the user to create 3 passwords at once.

--- task ---

Add this code to create 3 passwords:

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 9
---
#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

length = input('password length?')
length = int(length)

for p in range(3):
password = ''
for c in range(length):
    password += random.choice(chars)
print(password)
--- /code ---

--- /task ---

--- task ---

Indent the code for creating a password, so that it repeats 3 times.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 10-13
---
#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

length = input('password length?')
length = int(length)

for p in range(3):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
--- /code ---

--- /task ---

--- task ---

**Test:** Click the **Run** button. 

You should now see 3 passwords of your chosen password length.

--- /task ---
