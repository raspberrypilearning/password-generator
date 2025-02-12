## Using numbers and punctuation

Improve your program, so that it also chooses from:

+ Capital letters (A-Z)
+ Numbers (0-9)
+ Punctuation (!?.,-)

--- task ---

Add to your `chars` variable.

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 1
line_highlights: 3
---
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

password = random.choice(chars) print(password) --- /code ---

--- /task ---


--- task ---

**Test:** Click the **Run** button.

--- /task ---
