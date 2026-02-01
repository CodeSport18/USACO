# https://usaco.org/index.php?cpid=1515&page=viewproblem2

from collections import defaultdict

num_of_symbols,num_of_games = map(int,input().split(' '))

# print(num_of_symbols,num_of_games)

beaten_by_who = defaultdict(set)

for bracket_line in range(1,num_of_symbols+1):

    beatings = list(input())
    going_against_who = 1

    for matchup in beatings:

        # print(bracket_line,going_against_who,matchup)

        if matchup == 'W':
            beaten_by_who[going_against_who].add(bracket_line)
        elif matchup == 'L':
            beaten_by_who[bracket_line].add(going_against_who)

        going_against_who += 1

# print(beaten_by_who)

for game_number in range(1,num_of_games+1):

    count = 0

    symbol_one,symbol_two = map(int,input().split(' '))
    common_beaters = beaten_by_who[symbol_one].intersection(beaten_by_who[symbol_two])

    num_of_beaters = len(common_beaters)
    num_of_non_beaters = num_of_symbols-len(common_beaters)

    count += 2*num_of_non_beaters*num_of_beaters

    count += num_of_beaters*num_of_beaters

    print(count)