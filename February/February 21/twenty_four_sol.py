ans = 0
hand = [0] * 4  # The given card hand.
hand_permutation = []  # The generated permutation of the card hand.
chosen = [False] * 4  # Whether a given card is present in `hand_permutation`.

# Function that takes in two numbers and an operation and returns the result.
def operation(op, num1, num2):
	if op == 0:
		return num1 + num2
	elif op == 1:
		return num1 - num2
	elif op == 2:
		return num1 * num2
	else:
		# The divisor cannot be 0 and the quotient must be a whole number.
		if num2 == 0 or num1 % num2 != 0:
			return float("-inf")
		return num1 // num2


# Function that generates all possible permutations of the card hand.
def generate_hand_permutation():
	global ans

	if len(hand_permutation) == 4:
		# We have generated a permutation, so we can try placing the operators.
		for op1 in range(4):
			for op2 in range(4):
				for op3 in range(4):
					first = operation(op1, hand_permutation[0], hand_permutation[1])
					# If the operation is invalid, continue;
					if first == float("-inf"):
						continue

					second = operation(op2, first, hand_permutation[2])
					if second == float("-inf"):
						continue

					third = operation(op3, second, hand_permutation[3])
					if third == float("-inf"):
						continue

					if third <= 24:
						ans = max(ans, third)

		# Case 2: (( ) ( ))
		for op1 in range(4):
			for op2 in range(4):
				for op3 in range(4):
					first = operation(op1, hand_permutation[0], hand_permutation[1])
					if first == float("-inf"):
						continue

					second = operation(op2, hand_permutation[2], hand_permutation[3])
					if second == float("-inf"):
						continue

					third = operation(op3, first, second)
					if third == float("-inf"):
						continue

					if third <= 24:
						ans = max(ans, third)
	else:
		# Otherwise, we continue to build our permutation array.
		for i in range(4):
			if chosen[i]:
				continue
			chosen[i] = True
			hand_permutation.append(hand[i])
			generate_hand_permutation()
			chosen[i] = False
			hand_permutation.pop()


for _ in range(int(input())):
	ans = float("-inf")
	for i in range(4):
		hand[i] = int(input())

	# Start complete search.
	generate_hand_permutation()
	print(ans)