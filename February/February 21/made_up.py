# https://atcoder.jp/contests/abc202/tasks/abc202_c?lang=en

total = 0

n = int(input())
a,b,c = list(map(int,input().split(' '))),list(map(int,input().split(' '))),list(map(int,input().split(' ')))

for a_element in a:
    current = 1
    for b_element in b:
        if a_element == b_element:
            total += c.count(current)
        current += 1

print(total)