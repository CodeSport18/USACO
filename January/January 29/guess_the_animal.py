# https://usaco.org/index.php?cpid=893&page=viewproblem2

file = open('guess.in','r')

characteristics = []

for a in file:
    number_of_animals = int(a.strip())
    break

for a in file:
    the_input = a.strip().split(' ')
    the_input.pop(0)
    the_input.pop(0)
    characteristics.append(set(the_input))

file.close()

maximum = 0

for characteristics_list_index_one in range(number_of_animals):
    for characteristics_list_index_two in range(characteristics_list_index_one+1,number_of_animals):
        z = characteristics[characteristics_list_index_one].intersection(characteristics[characteristics_list_index_two])
        maximum = max(maximum,len(z)+1)

file = open('guess.out','w')
file.write(str(maximum))
file.close()