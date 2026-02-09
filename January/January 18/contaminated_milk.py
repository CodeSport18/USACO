# https://usaco.org/index.php?page=viewproblem2&cpid=569

from collections import defaultdict

file = open('badmilk.in','r')

drinks = []

for a in file:
    n_m_d_s = list(map(int,a.strip().split(' ')))
    break

what_was_drank_by_who = defaultdict(list)

counter = 0
for a in file:
    drink = list(map(int,a.strip().split()))
    drinks.append(drink)
    what_was_drank_by_who[drink[1]].append(drink[0])
    counter += 1
    if counter == n_m_d_s[2]:
        break

sicknesses = {}

for a in file:
    sickness = list(map(int,a.strip().split(' ')))
    # print(sickness)
    sicknesses[sickness[0]] = sickness[1]
    # print(sicknesses)

drinks = sorted(drinks, key=lambda x: x[2])

file.close()

for sickness in sicknesses:
    # print(sickness)
    new_dict = {}

    for drink in what_was_drank_by_who:
        # print(what_was_drank_by_who[drink],drink)
        if sickness in what_was_drank_by_who[drink]:
            new_dict[drink] = what_was_drank_by_who[drink]
    
    what_was_drank_by_who = new_dict.copy()

# print(what_was_drank_by_who)

maximum = 0

for milk in what_was_drank_by_who:
    # print(maximum,milk,what_was_drank_by_who[milk])
    maximum = max(maximum,len(what_was_drank_by_who[milk]))


file = open('badmilk.out','w')
# print(str(maximum))
file.write(str(maximum))
file.close()