# https://usaco.org/index.php?cpid=856&page=viewproblem2

MAX_TIME = 1000

change = [0 for _ in range(MAX_TIME + 1)]
with open("blist.in") as read:
	n = int(read.readline().strip())
	for _ in range(n):
		start, end, amt = map(int, read.readline().strip().split())

		# at the start, we'll need some additional buckets
		change[start] += amt
		# at the end, those buckets are no longer needed
		change[end] -= amt

max_buckets = 0  # max # of buckets we'll need
curr_buckets = 0  # # of buckets we need at the current processing time
for t in range(MAX_TIME + 1):
	# update the # of buckets we're using
	curr_buckets += change[t]
	# update the maximum accordingly
	max_buckets = max(max_buckets, curr_buckets)

print(max_buckets, file=open("blist.out", "w"))