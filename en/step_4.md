## Random characters

Let's create a program to choose a random character for your password.

--- task ---

Open the [Password Generator starter project](https://editor.raspberrypi.org/en/projects/password-generator-starter){:target="_blank"}.

--- /task ---

--- task ---

Create a list of characters, stored in a variable called `chars`.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 3
---
#!/bin/python3

chars = 'abcdefghijklmnopqrstuvwxyz'
--- /code ---

--- /task ---

--- task ---

To choose a random character, you'll need to `import` the `random` module.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 2
---
#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyz'
--- /code ---

--- /task ---

--- task ---

Now you can choose a random character from the list, and store it in a variable called `password`.

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

chars = 'abcdefghijklmnopqrstuvwxyz'

password = random.choice(chars)
--- /code ---

--- /task ---

--- task ---

Finally, you can print your (very short!) password to the screen.

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

chars = 'abcdefghijklmnopqrstuvwxyz'

password = random.choice(chars)
print(password)
--- /code ---

--- /task ---

--- task ---

**Test:** Click the **Run** button. 

You should see a single random character on the screen.

If you run your program a few times, you should see different characters appear.

--- /task ---

A password isn't very secure if it only contains letters. 

--- task ---

Add some numbers to your `chars` variable.

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 4
---
#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'

password = random.choice(chars)
print(password)
--- /code ---

--- /task ---

**Test:** Click the **Run** button again a few times, and you should see that sometimes a number is chosen.
