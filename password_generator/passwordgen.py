import random
import string

def questionnaire():
    special_char = input("Are special characters allowed? [Y,N]")

    if special_char == "Y":
        generator_special()
    else:
        generator_number()

def generator_special(): 

    index = 0

    while index < 15:
        print(random.choice(string.ascii_letters), end='')
        index +=1
        print(random.choice(string.punctuation), end='')
        index +=1

def generator_number(): 

    index = 0

    while index < 15:
        print(random.choice(string.ascii_letters), end='')
        index +=1
        print(random.choice(string.digits), end='')
        index +=1

questionnaire()