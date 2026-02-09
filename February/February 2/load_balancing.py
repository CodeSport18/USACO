from typing import List, Tuple


with open("balancing.in") as read:
	# The array of cows (to be sorted by x-pos)
	by_x = []
	for _ in range(int(read.readline())):
		by_x.append(tuple(int(i) for i in read.readline().split()))


def min_partition(x_line: int, cows: List[Tuple[int, int]]) -> int:
	"""
	Given a pre-defined vertical line, finds the most balanced horizontal line
	(Assumes that the cows have been sorted by y-pos already)
	"""
	left = [c for c in cows if c[0] < x_line]
	right = [c for c in cows if c[0] > x_line]

	most_balanced = float("inf")
	left_at = 0
	right_at = 0
	while left_at + right_at < len(cows):
		y_line = cows[left_at + right_at][1] + 1

		while left_at < len(left) and y_line > left[left_at][1]:
			left_at += 1

		while right_at < len(right) and y_line > right[right_at][1]:
			right_at += 1

		below_max = max(left_at, right_at)
		above_max = max(len(left) - left_at, len(right) - right_at)
		most_balanced = min(most_balanced, max(below_max, above_max))

	return most_balanced


by_x.sort()
# Same as by_x, but sorted by y-pos
by_y = sorted(by_x, key=lambda c: c[1])

most_balanced = float("inf")
# The cow which decides the vertical line
x_line_at = 0
while x_line_at < len(by_x):
	x_line = by_x[x_line_at][0] + 1
	most_balanced = min(most_balanced, min_partition(x_line, by_y))
	# Go through the list of cows until we hit one with a new x-pos
	while x_line_at < len(by_x) and x_line > by_x[x_line_at][0]:
		x_line_at += 1

print(most_balanced, file=open("balancing.out", "w"))