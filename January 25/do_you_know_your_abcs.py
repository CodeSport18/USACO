# https://usaco.org/index.php?cpid=1059&page=viewproblem2

abcs = list(map(int,input().split(' ')))
abcs.sort()

abc = abcs[6]
a = abcs[0]
b = abcs[1]
c = abc-a-b

print(a,b,c)