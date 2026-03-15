class Logo:
	def __init__(self, x, y, ch):
		# Rotate logos to reduce the amount of casework
		# Longer side = x, shorter side = y
		if x < y:
			y, x = x, y

		self.x = x
		self.y = y
		self.ch = ch

	def rotate(self):
		# Rotate the rectangle by 90 degrees
		self.x, self.y = self.y, self.x

	def print_rectangle(self):
		for _ in range(self.y):
			print(self.ch * self.x)


def main():
	values = [int(i) for i in input().split()]

	a = Logo(values[0], values[1], "A")
	b = Logo(values[2], values[3], "B")
	c = Logo(values[4], values[5], "C")

	# First case: all 3 have the same width, so try to place them one under the other
	if a.x == b.x == c.x:
		if a.y + b.y + c.y == a.x:  # If they actually form a square
			print(a.x)
			a.print_rectangle()
			b.print_rectangle()
			c.print_rectangle()

			return

	# Let a be the logo with the largest x
	if c.x > b.x:
		b, c = c, b
	if b.x > a.x:
		a, b = b, a

	remaining_y = a.x - a.y

	# Rotate the rectangles if their longer side, x, matches the remaining height
	if b.x == remaining_y:
		b.rotate()
	if c.x == remaining_y:
		c.rotate()

	if b.y == remaining_y and c.y == remaining_y:
		print(a.x)
		a.print_rectangle()

		for _ in range(b.y):
			print(b.ch * b.x + c.ch * c.x)

		return

	print(-1)


if __name__ == "__main__":
	main()