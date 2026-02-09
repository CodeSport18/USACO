# https://usaco.org/index.php?cpid=688&page=viewproblem2

file = open('hps.in','r')

for a in file:
    number_of_games = int(a.strip())
    break

win_arrangement_one = {1:2,2:3,3:1}
win_arrangement_two = {1:3,3:2,2:1}

games = []

for a in file:
    game = list(map(int,a.strip().split(' ')))
    games.append(game)

number_of_wins = [0,0]

for a in games:
    if win_arrangement_one[a[0]] == a[1]:
        number_of_wins[0] += 1

for a in games:
    if win_arrangement_two[a[0]] == a[1]:
        number_of_wins[1] += 1

file = open('hps.out','w')
file.write(str(max(number_of_wins)))
file.close()