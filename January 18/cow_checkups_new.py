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


# Odd-subarray length iteration
for i in range(number_of_cows):
	left = i
	right = i

	# current_placement = (# cows moved into correct positions) - (# cows moved out of correct positions)
	answer = start

	while left >= 0 and right < number_of_cows:
		if cow_line[left] == wanted_cow_line[right]:
			answer += 1

		if cow_line[right] == wanted_cow_line[left]:
			answer += 1

		if cow_line[left] == wanted_cow_line[left]:
			answer -= 1

		if cow_line[right] == wanted_cow_line[right]:
			answer -= 1

		answers[answer] += 1

		left -= 1
		right += 1


# Even-subarray length iteration
for i in range(1, number_of_cows):
	left = i - 1
	right = i

	# current_placement = (# cows moved into correct positions) - (# cows moved out of correct positions)
	answer = start

	while left >= 0 and right < number_of_cows:
		if cow_line[left] == wanted_cow_line[right]:
			answer += 1

		if cow_line[right] == wanted_cow_line[left]:
			answer += 1

		if cow_line[left] == wanted_cow_line[left]:
			answer -= 1

		if cow_line[right] == wanted_cow_line[right]:
			answer -= 1

		answers[answer] += 1

		left -= 1
		right += 1



for number in range(number_of_cows+1):
    print(answers[number])