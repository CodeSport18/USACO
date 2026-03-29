alphabet = list('abcdefghijklmnopqrstuvwxyz')

key_value_pairs = {}

for a in range(len(alphabet)):
    key_value_pairs[alphabet[a]] = a

the_input = input()
the_shift = int(input())

for char in the_input:

    if char in key_value_pairs:
        print( alphabet[ (key_value_pairs[char] + the_shift) % 26 ] , end = '')

    else:
        print( ' ' , end = '')

print()