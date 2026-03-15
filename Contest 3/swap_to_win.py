# https://usaco.org/index.php?page=viewproblem&cpid=1577

from collections import defaultdict

number_of_testcases = int(input())

for testcase_number in range(1,number_of_testcases+1):

    operations = []

    n,m = map(int,input().split(' '))
    goal_string = list(input())

    strings = []

    for _ in range(n):
        strings.append(list(input()))

    for a in range(m):
        if strings[0][a] != goal_string[a]:

            if a<m-1 and goal_string[a] in strings[0][a+1::]:
                the_index = strings[0][a+1::].index(goal_string[a]) + (a+1)
                operations.append('1 '+'1 '+str(a+1)+' '+str(the_index+1))
                strings[1][a],strings[1][the_index] = strings[1][the_index],strings[1][a]
                break

            else:
                done = False

                for b in range(0,n):
                    if strings[b][a] == goal_string[a]:
                        operations.append('2 '+'1 '+str(b+1)+' '+str(a+1))
                        strings[1][a],strings[b+1][a] = strings[b+1][a],strings[1][a]
                        done = True
                        break
                
                if done == False:
                    for b in range(0,n):
                        if goal_string[a] in strings[b]:
                            operations.append('1 '+str(b+1)+' '+str(strings[b].index(goal_string[a])+1)+' '+str(a+1))
                            operations.append('2 '+'1 '+str(b+1)+' '+str(a+1))
                            break
    
    print(len(operations))
    for operation in operations:
        print(operation)