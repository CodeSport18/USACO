# https://usaco.org/index.php?cpid=689&page=viewproblem2

from typing import List


TIPPED = "0"


def flip(r: int, c: int, cows: List[List[int]]) -> bool:
	if cows[r][c]:
		for ri in range(r + 1):
			for ci in range(c + 1):
				cows[ri][ci] = not cows[ri][ci]
		return True
	return False


with open("cowtip.in") as read:
	width = int(read.readline())
	cows = []
	for _ in range(width):
		row = read.readline()
		to_add = []
		for c in range(width):
			to_add.append(row[c] != TIPPED)
		cows.append(to_add)

min_flips = 0
x = width - 1
y = width - 1
while x >= 0 and y >= 0:
	# Flip the rectangle with lower right corner at (x, y)
	min_flips += flip(x, y, cows)
	if x != y:
		# Also flip rectangle at (y, x) if it is different
		min_flips += flip(y, x, cows)

	"""
	Transition to the next cell, first going to the left and then
	to the next row if the current row has finished.
	"""
	if x > 0:
		x -= 1
	else:
		y -= 1
		x = y

print(min_flips, file=open("cowtip.out", "w"))