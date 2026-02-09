# https://usaco.org/index.php?page=viewproblem2&cpid=1107

from collections import defaultdict

cows = {'Bessie':['Ox',0]}

cycle = ['Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat']

relations = defaultdict(lambda: defaultdict(list))

for animal in range(12,24):
    for animal_two in range(animal-12,animal):
        relations [cycle[animal]] [cycle[animal_two]] .append( animal_two-animal )
    for animal_three in range(animal+1,animal+13):
        relations [cycle[animal]] [cycle[animal_three]] .append( animal_three-animal )

number_of_relationships = int(input())

for relationship_number in range(1,number_of_relationships+1):

    the_relationship = input().split(' ')
    pivot_cow = the_relationship[-1]
    new_cow = the_relationship[0]
    previous_or_next = the_relationship[3]
    new_year = the_relationship[4]
    pivot_year = cows[pivot_cow][1]
    old_year = cows[pivot_cow][0]

    if previous_or_next == 'previous':
        cows[new_cow] = [new_year,pivot_year+relations[old_year][new_year][0]]
    else:
        cows[new_cow] = [new_year,pivot_year+relations[old_year][new_year][1]]

print(abs(cows['Elsie'][1]))