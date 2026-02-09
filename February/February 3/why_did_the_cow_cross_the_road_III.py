# https://usaco.org/index.php?page=viewproblem2&cpid=713

from collections import defaultdict,OrderedDict

file = open('cowqueue.in','r')

cow_arrivals = defaultdict(list)

for a in file:
    num_of_cows = int(a.strip())
    break

for a in file:
    the_input = a.strip().split(' ')
    cow_arrivals[int(the_input[0])].append(int(the_input[1]))

cow_arrivals = OrderedDict(sorted(cow_arrivals.items(), key=lambda item: item[0]))

file.close()

time = 0

for arrival in cow_arrivals:
    time = max(time,arrival)
    for interrogation_length in cow_arrivals[arrival]:
        time += interrogation_length

file = open('cowqueue.out','w')
file.write(str(time))
file.close()