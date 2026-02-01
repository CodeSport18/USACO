# https://usaco.org/index.php?cpid=1060&page=viewproblem2

number_of_flowers = int(input())
flowers = list(map(int,input().split(' ')))

total = 0

for a in range(0,number_of_flowers):
    for b in range(a+1,number_of_flowers+1):

        the_flowers = flowers[a:b]
        average = sum(the_flowers)/len(the_flowers)

        if average in the_flowers:
            total += 1

print(total)