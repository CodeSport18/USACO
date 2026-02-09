# https://usaco.org/index.php?page=viewproblem2&cpid=1468

num_of_integers = int(input())

the_integers = list(map(int,input().split(' ')))

first_occurrences = {}
last_single_occurrences = {}
last_double_occurrences = {}

for integer_index in range(num_of_integers):
    if the_integers[integer_index] not in first_occurrences:
        first_occurrences[the_integers[integer_index]] = integer_index

for integer_index in range(num_of_integers-1,-1,-1):
    if the_integers[integer_index] not in last_double_occurrences:

        if the_integers[integer_index] in last_single_occurrences and the_integers[integer_index] not in last_double_occurrences:
            last_double_occurrences[the_integers[integer_index]] = integer_index

    if the_integers[integer_index] in last_single_occurrences:
        del last_single_occurrences[the_integers[integer_index]]

    last_single_occurrences[the_integers[integer_index]] = integer_index


first_single_occurrences = {k: v for k, v in reversed(list(last_single_occurrences.items()))}
last_double_occurrences = {k: v for k, v in reversed(list(last_double_occurrences.items()))}

num_of_distinct_before = []

keys = list(last_double_occurrences)

num_of_os = len(last_double_occurrences)

counter = 0

for m in first_single_occurrences:

    for o in range(num_of_os):
        if last_double_occurrences[keys[0]] < first_single_occurrences[m]:
            num_of_os -= 1
            del last_double_occurrences[keys[0]]
            keys.pop(0)
        else:
            break
    
    counter += num_of_os

    if m in last_double_occurrences:
        counter -= 1

print(counter)