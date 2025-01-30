import random

def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read().splitlines()
            if filename == "hooks.txt":
                return set(line.lower() for line in data)
            return set(data)
    except FileNotFoundError:
        print(f"Error: File {filename} not found!")
        return ["Unknown"] 
    
def race():
    race_data = random.randint(1, 3)
    if race_data == 1:
        print("human")
        return "Human"
    elif race_data == 2:
        print("dwarf")
        return "Dwarf"
    elif race_data == 3:
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
    
name = load_data(get_firstName_data())
surname = load_data(get_lastName_data())
work = load_data("occupations.txt")
city = load_data(get_city_data())
hooks = load_data("hooks.txt")



#randomly selects one name and one age
names = random.choice(list(name))
surnames = random.choice(list(surname))

cities = random.choice(list(city))
hook = random.choice(list(hooks))

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



    

def race_age():
    race_data = {
        "Dwarf": 80,
        "Human": 60,
        "Elf": 100,
    }
    if charRace in race_data:
            return race_data[charRace]
race_age()

def define_senior():
    senior_age = race_age()
    age = random.randint(20, 120)
    if age > senior_age:
        jobs = "Senior"
        return jobs, age
    else:
        jobs = random.choice(list(work))
        return jobs, age

final_age = define_senior()

jobs, age = define_senior()
#prints the bitchass
print(f"Hi, my name is {names} {surnames}and I am {age} year old {charRace}. I work as a {jobs} in {cities}.")
print(f"And as for the rest? Well, I was {hook}")