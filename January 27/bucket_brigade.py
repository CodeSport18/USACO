# https://usaco.org/index.php?cpid=939&page=viewproblem2

import sys

sys.stdin = open("buckets.in", "r")
sys.stdout = open("buckets.out", "w")

for i in range(10):
	row = input()
	for j in range(10):
		if row[j] == "B":
			barn_i = i
			barn_j = j
		if row[j] == "R":
			rock_i = i
			rock_j = j
		if row[j] == "L":
			lake_i = i
			lake_j = j

# distance without accounting for the rock
cows = abs(barn_i - lake_i) + abs(barn_j - lake_j) - 1

# if the barn, lake and rock are in the same row
# and the rock is between the barn and the lake
if barn_i == rock_i == lake_i and (
	lake_j < rock_j < barn_j or barn_j < rock_j < lake_j
):
	cows += 2
# if the barn, lake and rock are in the same column
# and the rock is between the barn and the lake
elif barn_j == rock_j == lake_j and (
	lake_i < rock_i < barn_i or barn_i < rock_i < lake_i
):
	cows += 2
print(cows)