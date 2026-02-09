# https://usaco.org/index.php?page=viewproblem2&cpid=1251

number_of_cows = int(input())
tuitions = list(map(int,input().split(' ')))
tuitions = sorted(tuitions)

# tuitions_set = set(tuitions)
# print(tuitions_set)

maximum = 0
maximum_tuition = 0

previous_tuition = 0
tuition = 1

for tuition in tuitions:

    if tuition != previous_tuition and number_of_cows*tuition > maximum:
        maximum = number_of_cows*tuition
        maximum_tuition = tuition

    previous_tuition = tuition

    number_of_cows -= 1

print(maximum,maximum_tuition)