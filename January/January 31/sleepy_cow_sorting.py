# https://usaco.org/index.php?page=viewproblem2&cpid=892

file = open('sleepy.in','r')

for a in file:
    num_of_cows = int(a.strip())
    break

for a in file:
    cows = list(map(int,a.strip().split(' ')))

file.close()

max_unsorted_index = 0

for cow in range(1,num_of_cows):
    if cows[cow-1] > cows[cow]:
        max_unsorted_index = cow

file = open('sleepy.out','w')
file.write(str(max_unsorted_index))
file.close()