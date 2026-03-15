# https://usaco.org/index.php?page=viewproblem&cpid=1576

t = int(input())

for test_index in range(t):
    the_num = str(input())

    operations = 0

    if int(the_num) > 0:

        new_num = ''

        condition = False

        for a in the_num:
            new_num += str(int(a)%2)
            if a not in ['0','1']:
                condition = True
        
        the_num = str(int(new_num))
        if condition == True:
            operations += 1

    # print(the_num,operations)

    counter = 1

    if the_num != '0':

        zero_count = 0

        for a in range(len(the_num)-1,-1,-1):
            # print(the_num)
            if the_num[a] == '0':
                zero_count += 1

            else:
                if zero_count > 0:
                    operations += counter
                else:
                    operations += 1

                zero_count += 1

            if zero_count == 1:
                counter = 3
            else:
                counter *= 2
    
            # print(operations % (10**9 + 7),a,zero_count)
    
    print(operations % (10**9 + 7))