# https://usaco.org/index.php?page=viewproblem&cpid=1575

num_of_testcases = int(input())

for testcase_number in range(num_of_testcases):

    n,k = map(int,input().split(' '))

    operations_count = 0

    testcase = list(map(int,input().split(' ')))

    while True:
        win_condition = True

        for index in range(n):

            check = testcase.copy()
            check.pop(index)
            while testcase[index] in check:
                operations_count += 1
                testcase[index] += k
                # print(testcase,index,check,operations_count)

                # win_condition = False

        if win_condition == True:
            break

    print(operations_count)