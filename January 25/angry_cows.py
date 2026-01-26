# https://usaco.org/index.php?page=viewproblem2&cpid=592

file = open('angry.in','r')

bales = []

for a in file:
    number_of_bales = int(a.strip())
    break

for a in file:
    bales.append(int(a.strip()))

bales = sorted(bales)

previous_bale = 0

bale_distances_from_left = []

for bale in bales:
    bale_distances_from_left.append(bale-previous_bale)
    previous_bale = bale

bales.reverse()

previous_bale = 0

bale_distances_from_right = []

for bale in bales:
    bale_distances_from_right.append(previous_bale-bale)
    previous_bale = bale

bale_distances_from_right.reverse()
bales.reverse()

# print(bales)

# print(bale_distances_from_left,bale_distances_from_right)

max_possibility = 0

if number_of_bales >= 3:
    for bale_index in range(1,number_of_bales-1):
        current_possibility = 1

        # Check the bales going right
        for distance_index in range(bale_index+1,number_of_bales):
            if bale_distances_from_left[distance_index] > (distance_index-bale_index):
                break
            # print(bale_distances_from_left[distance_index],(distance_index-bale_index),'a')
            current_possibility += 1

        # Check the bales going left
        for distance_index in range(bale_index-1,-1,-1):
            if bale_distances_from_right[distance_index] > (bale_index-distance_index):
                break
            # print(bale_distances_from_right[distance_index],(bale_index-distance_index),'b')
            current_possibility += 1
        
        max_possibility = max(max_possibility,current_possibility)

        # print(max_possibility)

file = open('angry.out','w')
file.write(str(max_possibility))
file.close()