print('hello world')
import string
print(string.ascii_letters)
print(string.ascii_lowercase)

# since we want a random selection we import random
import random
# from random library we want to utilize choice method
# can print any random letter from the given string
print(random.choice('pull a letter from here'))
print(random.choice(string.ascii_lowercase))

# user input
letter_input_1 = input('choose a letter: "v" for vowel "c" for consonant "l" for any other letter')
letter_input_2 = input('choose a letter: "v" for vowel "c" for consonant "l" for any other letter')
letter_input_3 = input('choose a letter: "v" for vowel "c" for consonant "l" for any other letter')
letter_input_4 = input('choose a letter: "v" for vowel "c" for consonant "l" for any other letter')
letter_input_5 = input('choose a letter: "v" for vowel "c" for consonant "l" for any other letter')

# variables for v, c, and l
vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letter = string.ascii_lowercase

# create a function to generate 5 separate random letter for 5 sep variables
def generator():

    # conditional statements for user input of v, c, or l
    if letter_input_1 == "v":
        letter1 = random.choice(vowels)
    elif letter_input_1 == "c":
        letter1 = random.choice(consonants)
    elif letter_input_1 == "l":
        letter1 = random.choice(string.ascii_lowercase)
    else:
        letter1 = letter_input_1  # allows user to input a specific letter

    # copy conditional loop for the rest of the letter inputs
    if letter_input_2 == "v":
        letter2 = random.choice(vowels)
    elif letter_input_2 == "c":
        letter2 = random.choice(consonants)
    elif letter_input_2 == "l":
        letter2 = random.choice(string.ascii_lowercase)
    else:
        letter2 = letter_input_2

    if letter_input_3 == "v":
        letter3 = random.choice(vowels)
    elif letter_input_3 == "c":
        letter3 = random.choice(consonants)
    elif letter_input_3 == "l":
        letter3 = random.choice(string.ascii_lowercase)
    else:
        letter3 = letter_input_3

    if letter_input_4 == "v":
        letter4 = random.choice(vowels)
    elif letter_input_4 == "c":
        letter4 = random.choice(consonants)
    elif letter_input_4 == "l":
        letter4 = random.choice(string.ascii_lowercase)
    else:
        letter4 = letter_input_4

    if letter_input_5 == "v":
        letter5 = random.choice(vowels)
    elif letter_input_5 == "c":
        letter5 = random.choice(consonants)
    elif letter_input_5 == "l":
        letter5 = random.choice(string.ascii_lowercase)
    else:
        letter5 = letter_input_5

    name = letter1+letter2+letter3+letter4+letter5
    return(name)

for i in range(20): # generate 20 diff names
    print(generator())






