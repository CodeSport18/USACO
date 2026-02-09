# https://cses.fi/problemset/task/1640

list_size,target_sum = map(int,input().split(' '))
the_list = list(map(int,input().split(' ')))

closest = [float('inf'),float('inf')]

for a in range(len(the_list)):
    for b in range(a+1,len(the_list)):

        if closest == [float('inf'),float('inf')] or abs(the_list[a]+the_list[b]-target_sum) < abs(the_list[closest[0]]+the_list[closest[1]]-target_sum):
            closest = [a,b]

print(closest[0],closest[1])