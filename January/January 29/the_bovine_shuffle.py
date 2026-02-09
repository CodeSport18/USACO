# https://usaco.org/index.php?cpid=760&page=viewproblem2

from collections import defaultdict

file = open('shuffle.in','r')

for a in file:
    number_of_cows = int(a.strip())
    break

for a in file:
    shuffle = list(map(int,a.strip().split(' ')))
    break

for a in file:
    cow_ids = list(map(int,a.strip().split(' ')))
    break

file.close()

previous = {}

counter = 1

for a in cow_ids:
    previous[counter] = a
    counter += 1

for a in range(3):

    current = {}

    for b in range(1,number_of_cows+1):
        current[b] = previous[shuffle[b-1]]

    previous = current.copy()


answer = ''

for a in current:
    if answer != '':
        answer += '\n'
    answer += str(current[a])

file = open('shuffle.out','w')
file.write(answer)
file.close()