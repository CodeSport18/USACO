import sys

sys.stdin = open("tracing.in", "r")
sys.stdout = open("tracing.out", "w")

n, t = map(int, input().split())

infected = [int(i) for i in input().strip()]
shakes = []

for _ in range(t):
	shakes.append(list(map(int, input().split())))

# sorts by the first element (time)
shakes.sort()

ans_mink = float("inf")
ans_maxk = -float("inf")
num_possible = 0


def simulate(cow_zero):
	mink = float("inf")
	maxk = -float("inf")
	for k in range(251):
		cur_infected = [False] * n
		cur_infected[cow_zero] = True
		time = [0] * n
		for i in range(len(shakes)):
			# Subtract one for a zero-indexed index.
			cow1, cow2 = shakes[i][1] - 1, shakes[i][2] - 1

			# If any of the two cows are infected, increase their time infected by 1
			if cur_infected[cow1]:
				time[cow1] += 1
			if cur_infected[cow2]:
				time[cow2] += 1

			# cow1 infects cow2
			if cur_infected[cow1] and not cur_infected[cow2] and time[cow1] <= k:
				cur_infected[cow2] = True

			# cow2 infects cow1
			if cur_infected[cow2] and not cur_infected[cow1] and time[cow2] <= k:
				cur_infected[cow1] = True
		"""
		Does our resulting array of infected cows equal the one
		that was given?
		"""
		if infected == cur_infected:
			mink = min(mink, k)
			maxk = max(maxk, k)
	return [mink, maxk]


for i in range(len(infected)):
	"""
	Since infected cows stay infected, only infected cows can
	qualify as "cow zero"
	"""
	if infected[i]:
		result = simulate(i)
		# At least one value of K worked.
		if result[0] != float("inf"):
			ans_mink = min(ans_mink, result[0])
			ans_maxk = max(ans_maxk, result[1])
			num_possible += 1

# Worked for every possible value of K.
if ans_maxk == 250:
	ans_maxk = "Infinity"

print(num_possible, ans_mink, ans_maxk)