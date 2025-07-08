"""
Imagine you are a creative writer who loves to come up with interesting and unique character names. 
Your task is to create a Python program that generates a list of character names and saves them in a file.

Requirements:
The program should ask the user for the number of character names to generate.
Each character name should consist of a random combination of three syllables.
The program should generate unique character names and ensure that no two names are the same.
Save the generated character names in a text file named "character_names.txt", with each name on a new line.
"""
import random
import string


# Function to generate a random syllable (consonant + vowel)
def generate_syllable():
    consonants = "bcdfghjklmnpqrstvwxyz"  # All consonant letters
    vowels = "aeiou"                      # All vowel letters
    # Randomly select one consonant and one vowel, then combine them
    random_syllable = random.choice(consonants) + random.choice(vowels)
    return random_syllable

# Function to generate a name by combining three syllables
def generate_name():
    # Create a name by joining three random syllables
    random_string = ''.join(generate_syllable() for i in range(3))
    # Capitalize the first letter to make it look like a name
    return random_string.title()

# Ask the user how many unique names to generate
user_input = input("Characters to generate: ")

names = set()  # Set to store unique names

# Open the file for writing (will overwrite if it already exists)
file = open("character_names.txt", "w")

# Keep generating names until we have the desired number of unique names
while len(names) < int(user_input):
    names.add(generate_name())  # Set will only add if the name is not already present

# Write each unique name to the file, one per line
for name in names:
    file.write(name + '\n')

# Close the file to save changes
file.close()