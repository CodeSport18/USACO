# https://usaco.org/index.php?cpid=664&page=viewproblem2

from collections import defaultdict

file = open('blocks.in','r')

for a in file:
    n = int(a.strip())
    break

chars_needed = defaultdict(int)

for a in file:

    the_input = a.strip().split(' ')

    chars_needed_temp = defaultdict(int)

    for side in the_input:
        for char in list(set(side)):
            chars_needed_temp[char] = max(side.count(char),chars_needed_temp[char])
    
    for char in chars_needed_temp:
        chars_needed[char] += chars_needed_temp[char]

file.close()

alphabet = list('abcdefghijklmnopqrstuvwxyz')

solution = ''

for letter in alphabet:
    if solution != '':
        solution += '\n'
    solution += str(chars_needed[letter])

file = open('blocks.out','w')
file.write(str(solution))
file.close()