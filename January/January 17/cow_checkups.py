# https://usaco.org/index.php?page=viewproblem2&cpid=1469

from collections import defaultdict

number_of_cows = int(input())
cow_line = list(map(int,input().split(' ')))
wanted_cow_line = list(map(int,input().split(' ')))

answers = defaultdict(int)

start = 0

for cow_index in range(number_of_cows):
    if wanted_cow_line[cow_index] == cow_line[cow_index]:
        start += 1

answers[start] = number_of_cows

for l in range(0,number_of_cows):
    for r in range(l+1,number_of_cows):

        answer = start

        cow_line_copy = cow_line.copy()

        for cow_index in range(l,r+1):
            if wanted_cow_line[cow_index] == cow_line_copy[cow_index]:
                answer -= 1

        cow_line_copy[l:r+1] = cow_line_copy[l:r+1][::-1]

        for cow_index in range(l,r+1):
            if wanted_cow_line[cow_index] == cow_line_copy[cow_index]:
                answer += 1

        answers[answer] += 1

for number in range(number_of_cows+1):
    print(answers[number])