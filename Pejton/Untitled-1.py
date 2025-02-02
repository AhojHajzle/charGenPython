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
    
def get_city_data():
    return f"cities/city{charRace}.txt"
    
def get_firstName_data():
    return f"names/{charRace}/firstName.txt"

def get_lastName_data():
    return f"names/{charRace}/lastName.txt"
    
pets = load_data("pets.txt")
name = load_data(get_firstName_data())
surname = load_data(get_lastName_data())
work = load_data("occupations.txt")
city = load_data(get_city_data())
hooks = load_data("hooks.txt")
weapons = load_data("weapons.txt")
traits = load_data("traits.txt")



#randomly selects one name and one age
names = random.choice(list(name))
surnames = random.choice(list(surname))
cities = random.choice(list(city))
weapon = random.choice(list(weapons))
trait = random.choice(list(traits)).lower()

def pet():
    if random.randint(1, 100) <= 20:
        pet = random.choice(list(pets))
        return f"I have a {pet} as a pet."
    else:
        return "I have no pets."
pet = pet()

def has_hook():
    print(charRace)
    race_data = {"Dwarf": 15,
               "Elf": 15,
               "Human": 35}
    if random.randint(1, 100) <= race_data[charRace]:
        hook = random.choice(list(hooks))
        return hook
    else:
        hook = "living a calm life."
        return hook
hook = has_hook()


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


jobs, age = define_senior()
#prints the bitchass
print(f"Hi, my name is {names} {surnames}and I am {age} year old {charRace}. I work as a {jobs} in {cities}.")
print(f"I am proficient with {weapon}.")
print(f"And as for the rest? Well, I was {hook}")
print(pet)
print(f"Others would describe me as {trait}")