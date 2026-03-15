# https://codeforces.com/gym/104520/problem/H

array_length = int(input())

a = list(map(int,input().split(' ')))
b = list(map(int,input().split(' ')))

for multiplier in range(0,array_length):
    a[multiplier] *= (multiplier+1)*(array_length-multiplier)

a.sort()
b.sort()
b.reverse()

total = 0

for index in range(array_length):
    total += a[index]*b[index]

print(total)