"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michal Hurai
email:  michal@hurai.com
"""

from collections import Counter
from string import punctuation

# Registrovaní uživatelé
REGISTERED_USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Texty na analýzu
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

# Prihlásenie
username = input("username: ")
password = input("password: ")

if username not in REGISTERED_USERS or REGISTERED_USERS[username] != password:
    print("unregistered user, terminating the program..")
    exit()

print("-" * 40)
print(f"Welcome to the app, {username}")
print(f"We have {len(TEXTS)} texts to be analyzed.")
print("-" * 40)

# Výber textu
selection = input("Enter a number btw. 1 and 3 to select: ")

if not selection.isdigit():
    print("Invalid input, terminating the program.")
    exit()

index = int(selection) - 1
if index < 0 or index >= len(TEXTS):
    print("Invalid number, terminating the program.")
    exit()

print("-" * 40)

# Výber a spracovanie textu
text = TEXTS[index]
words = [word.strip(punctuation) for word in text.split()]

word_count = len(words)
titlecase_count = sum(1 for word in words if word.istitle())
uppercase_count = sum(1 for word in words if word.isupper())
lowercase_count = sum(1 for word in words if word.islower())
numeric_strings = [word for word in words if word.isdigit()]
numbers_sum = sum(int(num) for num in numeric_strings)

print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {len(numeric_strings)} numeric strings.")
print(f"The sum of all the numbers {numbers_sum}")
print("-" * 40)

# Histogram
lengths = [len(word) for word in words]
counter = Counter(lengths)

print(f"{'LEN':>3}|{'OCCURENCES':^15}|{'NR.':<3}")
print("-" * 40)

for length in sorted(counter):
    stars = '*' * counter[length]
    print(f"{length:>3}|{stars:<15}|{counter[length]}")
