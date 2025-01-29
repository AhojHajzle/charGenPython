import random

#defines sets of names and ages
#name = {'Alice', 'Jack', 'Daniel', 'Sophie'}

#with open('fantaseaNames.txt', 'r') as file:
#    name = set(file.read().splitlines())

"""with open('fantaseaSurnames.txt', 'r') as file:
    surname = set(file.read().splitlines())

with open('occupations.txt', 'r') as file:
    work = set(file.read().splitlines())

with open("cities.txt", 'r') as file:
    city = set(file.read().splitlines())"""


def race():
    race_data = random.randint(1, 3)
    if race_data == 1:
        print("human")
        return "Human"
    elif race_data == 2:
        print("dwarf")
        return "Dwarf"
    else:
        print("elf")
        return "Elf"

charRace = race()
print(charRace)

def get_city_data():
    return f"cities/city{charRace}.txt"
    
def get_firstName_data():
    return f"names/{charRace}/firstName.txt"

def get_lastName_data():
    return f"names/{charRace}/lastName.txt"

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            return set (file.read().splitlines())
    except FileNotFoundError:
        print(f"Error: File {filename} not found!")
        return ["Unknown"]  
    
name = load_data(get_firstName_data())
surname = load_data(get_lastName_data())
work = load_data("occupations.txt")
city = load_data(get_city_data())

age = random.randint(18, 50)

#randomly selects one name and one age
names = random.choice(list(name))
surnames = random.choice(list(surname))
jobs = random.choice(list(work))
cities = random.choice(list(city))
#prints the bitchass
print(f"Hi, my name is {names} {surnames}and I am {age} year old {charRace}. I work as a {jobs} in {cities}.")