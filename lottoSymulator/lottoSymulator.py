""""
Lotto simulator , gonna pick 6 unique numbers from range 1-49
"""

import random


def choose_random_numbers(amount, total_amount):
    print(random.sample(range(1, total_amount + 1), amount))


choose_random_numbers(6, 49)
