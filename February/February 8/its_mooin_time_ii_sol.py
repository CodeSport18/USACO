# https://usaco.org/index.php?page=viewproblem2&cpid=1468

n = int(input())
array = [int(x) for x in input().split()]
# find indices of occurrences of each number
frequency = dict()
for i in range(n):
	if array[i] in frequency:
		frequency[array[i]].append(i)
	else:
		frequency[array[i]] = [i]

# precompute number of distinct values to the left of each index
num_distinct = []
distinct_vals = set()
for i in range(n):
	num_distinct.append(len(distinct_vals))
	distinct_vals.add(array[i])

# calculate answer
ans = 0
for num in frequency:
	if len(frequency[num]) >= 2:
		ans += num_distinct[frequency[num][-2]]
		if len(frequency[num]) >= 3:
			ans -= 1
print(ans)