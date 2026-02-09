# https://usaco.org/index.php?page=viewproblem2&cpid=591

file = open('promote.in','r')

divisions = []

for a in file:
    divisions.append(list(map(int,a.strip().split(' '))))

divisions.pop(0)
divisions.reverse()

file.close()

# print(divisions)

previous = 0

answer = []

for division in divisions:
    # if answer != '':
    #     answer += '\n'
    answer.append(str(division[1]-division[0]+previous))
    previous = division[1]-division[0]+previous

answer.reverse()
the_text_answer = ''
for a in answer:
    if the_text_answer != '':
        the_text_answer += '\n'
    the_text_answer += a

file = open('promote.out','w')
file.write(the_text_answer)
file.close()