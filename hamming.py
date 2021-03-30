'''
Problem

Given two strings s and t of equal length, the Hamming distance between s and t,
denoted dH(s,t), is the number of corresponding symbols that differ in s and t.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
'''

import fileinput

def hamming(string_a, string_b):
    assert(len(string_a) == len(string_b))

    distance = 0
    for a, b in zip(string_a, string_b):
        if a != b:
            distance += 1

    return distance

if __name__ == '__main__':
    strings = []
    for line in fileinput.input():
        strings.append(line.rstrip())
    assert(len(strings) == 2)

    print(hamming(*strings))
