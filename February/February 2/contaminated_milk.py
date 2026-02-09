# https://usaco.org/index.php?page=viewproblem2&cpid=569

from functools import cmp_to_key

with open("badmilk.in") as read:
	data = [int(i) for i in read.readline().split()]
	people_num, milk_num, drink_times, sick_times = data

	"""
	Let's treat someone drinking milk and someone getting sick
	as both "events".
	An event will be represented by a 3-tuple formatted like so:
	(person, milk, time)

	We can differentiate the two by setting the value of milk
	as -1 for someone getting sick.
	"""
	events = []
	for _ in range(drink_times):
		e = [int(i) for i in read.readline().split()]
		e[0] -= 1
		e[1] -= 1
		events.append(tuple(e))

	for _ in range(sick_times):
		e = [int(i) for i in read.readline().split()]
		e[0] -= 1
		events.append((e[0], -1, e[1]))

"""
Sort the events based on when they occurred.
Note that since one can only get sick if they drank
the milk at a *strictly* earlier point in time, we have to put
the sick events before the drinking events if they occur at
the same point in time.
"""
cmp = lambda e1, e2: e1[2] - e2[2] if e1[2] != e2[2] else e1[1] - e2[1]
events.sort(key=cmp_to_key(cmp))

max_med = 0
# Go through each milk and check if it could be the bad one.
for m in range(milk_num):
	possible = True
	can_be_sick = [False for _ in range(people_num)]
	# Simulate the events, marking if each person could possibly be sick.
	for e in events:
		if e[1] == -1:
			if not can_be_sick[e[0]]:
				possible = False
				break
		elif e[1] == m:
			can_be_sick[e[0]] = True

	"""
	If this milk could possibly be the bad one,
	we see how many people could possibly be sick in total.
	"""
	if possible:
		max_med = max(max_med, sum(can_be_sick))

print(max_med, file=open("badmilk.out", "w"))