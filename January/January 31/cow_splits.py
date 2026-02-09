# # https://usaco.org/index.php?page=viewproblem2&cpid=1540

# t,k = map(int,input().split(' '))

# for testcase_number in range(1,t+1):
#     n = int(input())
#     s = input()

def check(s):
    for i in range(len(s)//2):
        if s[i]!=s[i + len(s)//2]:
            return False
    return True
 
t,k = list(map(int,input().split()))
for _ in range(t):
    n = int(input())
    s = input()
    if n%2==1:
        print(-1)
        continue
    if check(s):
        print(1)
        print(" ".join(["1"]*len(s)))
        continue
    ans=[1]*(n*3)
    for i in range(n//2):
        a=s[i*3:i*3+3]
        b=s[(i+n//2)*3:(i+n//2)*3+3]
        print(a,b)
        if a!=b:
            if a[:2]==b[1:]:
                ans[i*3+2]=ans[(i+n//2)*3]=2
            else:
                ans[i*3]=ans[(i+n//2)*3+2]=2
    print(max(ans))
    for i in range(n*3):
        print(ans[i],end=" \n"[i==3*n-1])