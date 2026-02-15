from sys import exit

with open("bcs.in") as read:
	n, k = [int(i) for i in read.readline().split()]
	# First piece in this array is the one we're trying to match to
	pieces = []
	sides = []
	for i in range(k + 1):
		top = n - 1
		bottom = 0
		left = n - 1
		right = 0
		piece = [[False for _ in range(n)] for _ in range(n)]

		for r in range(n):
			row = read.readline()
			for c in range(n):
				piece[r][c] = row[c] == "#"
				if piece[r][c]:
					bottom = max(bottom, r)
					top = min(top, r)
					left = min(left, c)
					right = max(right, c)

		pieces.append(piece)
		sides.append((left, right, top, bottom))


def check(piece: [[bool]], x: int, y: int) -> bool:
	"""checks if a piece location is in bounds and is '#'"""
	return 0 <= x < len(piece) and 0 <= y < len(piece[x]) and piece[x][y]


target = pieces[0]
# Try all the pieces & shifts to find the correct one
for i in range(1, k + 1):
	for j in range(1, k + 1):
		for idx in range(sides[i][3] - n + 1, sides[i][2] + 1):
			for idy in range(sides[i][1] - n + 1, sides[i][0] + 1):
				for jdx in range(sides[j][3] - n + 1, sides[j][2] + 1):
					for jdy in range(sides[j][1] - n + 1, sides[j][0] + 1):
						good = True
						for x in range(n):
							for y in range(n):
								ipiece = check(pieces[i], x + idx, y + idy)
								jpiece = check(pieces[j], x + jdx, y + jdy)
								# two '#' are in the same place
								if ipiece and jpiece:
									good = False
									break
								# the result doesn't match the figurine
								if target[x][y] != (ipiece or jpiece):
									good = False
									break

							if not good:
								break

						if good:
							print(i, j, file=open("bcs.out", "w"))
							exit()