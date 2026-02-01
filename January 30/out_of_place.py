# https://usaco.org/index.php?cpid=785&page=viewproblem2

file = open('outofplace.in','r')

for a in file:
    number_of_cows = int(a.strip())
    break

cows = []

for a in file:
    cow = int(a.strip())
    cows.append(cow)

bessie_index = -1

file.close()

file = open('outofplace.out','w')

if len(cows) > 1:

    # print(cows)

    for cow_index in range(1,number_of_cows):
        if cows[cow_index-1] > cows[cow_index]:
            bessie_index = cow_index
            break

    # print(bessie_index)

    set_left = cows[0:cow_index+1]
    counter = 0
    for a in range(len(set_left)-1):
        if set_left[counter] == set_left[counter+1]:
            set_left.pop(counter)
        else:
            counter += 1

    set_left = list(dict.fromkeys(cows[0:bessie_index+1]))
            
    set_right = list(dict.fromkeys(cows[bessie_index::]))

    # print(set_left,set_right)

    for a in range(len(set_left)):
        if set_left[0] >= cows[bessie_index]:
            break
        set_left.pop(0)
    for a in range(len(set_right)):
        if set_right[-1] <= cows[bessie_index]:
            break
        set_right.pop(-1)

    maximum = max(len(set_left)-1,len(set_right)-1)

    file.write(str(maximum))

else:

    file.write('0')

file.close()