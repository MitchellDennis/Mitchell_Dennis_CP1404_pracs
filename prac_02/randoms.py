

import random
# print(random.randint(5, 20))  # line 1
# print(random.randrange(3, 10, 2))  # line 2
# print(random.uniform(2.5, 5.5))  # line 3


# Line 1 shows: 18, 13, 8, 10, 7, 8, 7, 16, 11, 6, 15, 13
# Largest seen was 18, smallest seen was 6

# Line 2 shows: smallest 3, largest 9. It is not possible to get a 4 frokm this line as it only produces odd numbers because it steps up in 2s from 3.


# Line 3 shows: smallest possible is 2.5, largest possible is 5.49999999999999 or 5.5 depending on rounding

print(random.randint(1, 100)) # Produces a random number between 1 and 100 inclusive

