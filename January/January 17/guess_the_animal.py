# https://usaco.org/index.php?page=viewproblem2&cpid=893

first_input = int(input())

animal_characteristic = {}
characteristic_animal = {}

for animal_number in range(1,first_input+1):
    
    animal = input().split(' ')
    animal_characteristic[animal[0]] = animal[2::]

    for characteristic in animal[2::]:

        if characteristic not in characteristic_animal:
            characteristic_animal[characteristic] = []

        characteristic_animal[characteristic].append(animal[0])
    
print(animal_characteristic,characteristic_animal)