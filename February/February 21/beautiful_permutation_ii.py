# https://cses.fi/problemset/task/3175

def permute(nums):

    result = []
    n = len(nums)

    def backtrack(first):

        if first == n:
            result.append(nums[:])
            return

        for i in range(first, n):
            nums[first], nums[i] = nums[i], nums[first]

            backtrack(first + 1)

            nums[first], nums[i] = nums[i], nums[first]

    backtrack(0)
    return result

permutation_length = int(input())

possible_values = [n for n in range(1,permutation_length+1)]
all_permutations = permute(possible_values)

the_answer = []

total_length = len(all_permutations)

for permutation_index in range(total_length-1,-1,-1):
    permutation = all_permutations[permutation_index]

    for permutation_element in range(0,permutation_length-1):

        if abs(permutation[permutation_element]-permutation[permutation_element+1]) == 1:
            all_permutations.pop(permutation_index)
            total_length -= 1
            break

total_length = len(all_permutations)

while total_length > 1:

    minimum = []

    for permutation in range(0,total_length):
        # all_permutations[permutation].pop(0)
        if minimum == []:
            minimum.append(all_permutations[permutation])
        elif all_permutations[permutation][0] < minimum[0][0]:
            minimum = [all_permutations[permutation]]
        elif all_permutations[permutation][0] == minimum[0][0]:
            minimum.append(all_permutations[permutation])

        # print(minimum,'a')
    
    the_answer.append(minimum[0][0])
    # print(the_answer)

    all_permutations = minimum.copy()
    total_length = len(all_permutations)

    for permutation in range(0,total_length):
        all_permutations[permutation].pop(0)

    # print(all_permutations)

for a in the_answer:
    print(a,end = ' ')
for a in all_permutations[0]:
    print(a,end = ' ')
print()