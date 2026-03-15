# https://usaco.org/index.php?page=viewproblem2&cpid=785

file = open('outofplace.in','r')

lineup = []

for a in file:
    number_of_cows = int(a.strip())
    break

for a in file:
    lineup.append(int(a.strip()))

file.close()

sorted_lineup = sorted(lineup)

count = 0

for a in range(number_of_cows):
    if lineup[a] != sorted_lineup[a]:
        count += 1

file = open('outofplace.out','w')
file.write( str(max(0,count-1)) )
file.close()