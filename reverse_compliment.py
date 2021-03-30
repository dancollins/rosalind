'''
Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C'
and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing
the symbols of s, then taking the complement of each symbol (e.g., the reverse
complement of "GTCA" is "TGAC").

Given: A DNA string s

of length at most 1000 bp.

Return: The reverse complement sc of s.
'''

import fileinput

def reverse_compliment(string):
    return reversed(string.translate(string.maketrans('ATCG', 'TAGC')))

if __name__ == '__main__':
    for line in fileinput.input():
        print(''.join(reverse_compliment(line.rstrip())))