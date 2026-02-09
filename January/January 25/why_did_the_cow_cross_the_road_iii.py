# https://usaco.org/index.php?page=viewproblem2&cpid=713

file = open('cowqueue.in','r')

cows = {}

for a in file:
    number_of_cows = int(a.strip())
    break

for a in file:
    the_input = list(map(int,a.strip().split(' ')))
    cows[the_input[0]] = the_input[1]

cows = {key: value for key, value in sorted(cows.items())}

file.close()

time = 0

for cow in cows:
    time = max(time,cow)
    time += cows[cow]

file = open('cowqueue.out','w')
file.write(str(time))
file.close()