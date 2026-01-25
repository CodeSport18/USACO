# https://usaco.org/index.php?page=viewproblem2&cpid=1228

num_of_cow_statements = int(input())

greater_than = []
less_than = []
check_these_locations = []

for cow_statement_number in range(1,num_of_cow_statements+1):
    statement = input().split(' ')
    statement[1] = int(statement[1])
    if statement[0] == 'G':
        greater_than.append(statement[1])
        if statement[1] not in check_these_locations and statement[1]+1 < 1000000000:
            check_these_locations.append(statement[1])
    else:
        less_than.append(statement[1])
        if statement[1] not in check_these_locations:
            check_these_locations.append(statement[1])

greater_than.sort()
less_than.sort()
# less_than.reverse()
check_these_locations.sort()

len_of_greater_than = len(greater_than)
len_of_less_than = len(less_than)

minimum_number_of_liars = float('inf')

index_of_liars_in_greater_than = 0
index_of_liars_in_less_than = 0

previous_location = -1

print(check_these_locations)

number_of_liars = len_of_greater_than

for location in check_these_locations:

    print(greater_than[index_of_liars_in_greater_than],location)

    while index_of_liars_in_greater_than < len_of_greater_than and (greater_than[index_of_liars_in_greater_than] >= location):
        index_of_liars_in_greater_than += 1
        number_of_liars -= 1
        print(location,index_of_liars_in_greater_than,number_of_liars,'a')
    
    while index_of_liars_in_less_than < len_of_less_than and (location > less_than[index_of_liars_in_less_than]):
        index_of_liars_in_less_than += 1
        number_of_liars += 1
        print(location,index_of_liars_in_less_than,number_of_liars,'b')
    
    # current_number_of_liars = (len_of_greater_than-index_of_liars_in_greater_than-1)+(index_of_liars_in_less_than)
    
    minimum_number_of_liars = min(number_of_liars,minimum_number_of_liars)
    
    previous_location = location

print(minimum_number_of_liars)