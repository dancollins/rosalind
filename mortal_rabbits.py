'''
Problem

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence
Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that
each pair of rabbits reaches maturity in one month and produces a single pair of
offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic
programming solution in the case that all rabbits die out after a fixed number
of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live
for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th
month if all rabbits live for m months.
'''

import fileinput
from functools import lru_cache

@lru_cache(maxsize=None)
def calculate_rabbits(n_months, max_age):
    if n_months < 2:
        return 1

    # We have two different recurrance relationships, as we only want to add in
    # deaths once our rabbits come of age. Before that point, we have a pure
    # fibonacci sequence.
    if (n_months < max_age):
        return (calculate_rabbits(n_months - 1, max_age) +
                calculate_rabbits(n_months - 2, max_age))
    else:
        return (calculate_rabbits(n_months - 1, max_age) +
                calculate_rabbits(n_months - 2, max_age) -
                calculate_rabbits(n_months - max_age - 1, max_age))

if __name__ == '__main__':
    for line in fileinput.input():
        months, max_age = map(int, line.rstrip().split())
        print(calculate_rabbits(months - 1, max_age))
