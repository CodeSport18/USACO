# # https://usaco.org/index.php?page=viewproblem2&cpid=1539

# from math import ceil

# t = int(input())

# for testcase_number in range(1,t+1):

#     counter = 0
#     counter_two = 0
#     counter_three = 0

#     a,b,ca,cb,fa = map(int,input().split(' '))

#     a += b//cb * ca
#     b -= b//cb * cb

#     # print(a,b,ca,cb,fa)

#     if ca >= cb:
#         counter += max(0,fa-a)
#         if a < fa:
#             counter += max(0,cb-b-1)

#     else:
#         counter += max( 0 , ceil( (fa-a)/ca ) * cb - b)

#         if fa > a:

#             print(a,b,ca,cb,fa,counter_two)

#             counter_two += ( (fa-a)//ca * cb - b)
#             a += (fa-a)//ca * ca
#             if a==fa:
#                 a -= ca
#                 counter_two -= 1
            
#             counter_three = ()
            
#             print(a,b,ca,cb,fa,counter_two)
        
#             counter_two += (fa-a)
    
#     print(max(counter,counter_two))

def solve(A, B, cA, cB, fA):
    init = B // cB * cA + A
    if init >= fA:
        return 0
    nA0 = fA - 1 - init
    y = cB - 1 - B % cB  # nB0
    if cA >= cB:
        y += nA0
    else:
        y += nA0 // cA * cB + nA0 % cA
    return y + 1

def main():
    T = int(input())
    for _ in range(T):
        A, B, cA, cB, fA = map(int, input().split())
        print(solve(A, B, cA, cB, fA))

if __name__ == "__main__":
    main()