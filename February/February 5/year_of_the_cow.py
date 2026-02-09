# https://usaco.org/index.php?page=viewproblem2&cpid=1107

from collections import defaultdict

cows = {'Bessie':[0,'Ox']}

num_of_phrases = int(input())

cycle = ['Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat']

cycle_dict = {}

# for a in range()

for phrase_number in range(1,num_of_phrases+1):
    phrase = input().split(' ')
    cow_one,previous_or_next,zodiac_animal,cow_two = phrase[0],phrase[3],phrase[4],phrase[-1]

    if previous_or_next == 'previous':

        count = cows[cow_two][0]
        count_activation = False

        for animal in reversed(cycle.copy()):
            if count_activation == True:
                count -= 1
                if animal == zodiac_animal:
                    break
            elif animal == cows[cow_two][1]:
                count_activation = True

    else:

        count = cows[cow_two][0]
        count_activation = False

        for animal in cycle.copy():
            if count_activation == True:
                count += 1
                if animal == zodiac_animal:
                    break
            elif animal == cows[cow_two][1]:
                count_activation = True


    cows[cow_one] = [count,zodiac_animal]

print(abs(cows['Elsie'][0]))