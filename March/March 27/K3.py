iterate_through_log = 0

index = 0

length = int(input())
nums = list(map(int,input().split(' ')))

done = False

while done == False:

    for a in range(2**iterate_through_log):
        if nums[index] == 0:
            print(index)
            print(iterate_through_log+1)
            done = True
            break
        index += 1
    
    iterate_through_log += 1