people = [
    {"name": "Arun", "age": 25},
    {"name": "Balu", "age": 17},
    {"name": "Chanthuru", "age": 19},
    {"name": "Dhinesh", "age": 16},
    {"name": "Ezhi", "age": 22}
]

# Filter out people under 18
adults = filter(lambda person: person["age"] >= 18, people)

# Map remaining people's names to a new list
adult_names = list(map(lambda person: person["name"], adults))

print(adult_names)
