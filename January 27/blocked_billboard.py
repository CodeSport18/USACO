# https://usaco.org/index.php?cpid=759&page=viewproblem2

import sys

class Rect:
	def __init__(self):
		# Read rectangle coordinates from input
		self.x1, self.y1, self.x2, self.y2 = map(int, input().split())

	def area(self):
		# Calculate area of the rectangle
		return (self.y2 - self.y1) * (self.x2 - self.x1)


def intersect(p, q):
	# Calculate overlap in x direction
	x_overlap = max(0, min(p.x2, q.x2) - max(p.x1, q.x1))
	# Calculate overlap in y direction
	y_overlap = max(0, min(p.y2, q.y2) - max(p.y1, q.y1))
	return x_overlap * y_overlap  # Area of intersection


sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")

rects = []
for _ in range(3):
	rects.append(Rect())  # Read the two billboards and the truck

print(
	rects[0].area()  # Area of first billboard
	+ rects[1].area()  # Area of second billboard
	- intersect(rects[0], rects[2])  # Subtract area of first billboard covered by truck
	- intersect(
		rects[1], rects[2]
	)  # Subtract area of second billboard covered by truck
)