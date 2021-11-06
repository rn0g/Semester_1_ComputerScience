## Brazilian CPF generator
## Disclaimer: This code was created for educational purposes. I am a student and I'm trying to apply my knowledge in code.
## Do not use this code for any other reason other than educational purposes. 

from math import e
import random


def generate_cpf():
    archive = open('cpf_list.txt', 'a+')
    count = 10
    digit_1 = 0
    digit_2 = 0

    generate_9_numbers = [e for e in range(1, 10, 1)]
    random.shuffle(generate_9_numbers)
    print("Sequence generated for CPF: ", generate_9_numbers)
    for i in range((len(generate_9_numbers))):
        digit_1 = (generate_9_numbers[i] * count) + digit_1
        count = count-1
    ## Calculating first digit...
    digit_1 = digit_1%11
    if digit_1 < 2:
        digit_1 = 0
    else:
        digit_1 = 11 - digit_1

    digit_1_copy = digit_1
    generate_9_numbers.append(digit_1_copy) ## Adding digit_1 temporarily
    count = 11

    for i in range((len(generate_9_numbers))):
        digit_2 = (generate_9_numbers[i] * count) + digit_2
        count = count-1

    generate_9_numbers.pop()
    print("First digit: ", digit_1)
    ## Calculating second digit...

    digit_2 = digit_2%11
    if digit_2 < 2:
        digit_2 = 0
    else:    
        digit_2 = 11 - digit_2
    print("Second digit: ", digit_2)
    digit_1 = str(digit_1)
    digit_2 = str(digit_2)
    cpf_ = "".join(str(i) for i in generate_9_numbers)
    cpf_ = cpf_+"-"+digit_1+digit_2
    print("Complete CPF: %s" %cpf_)
    archive.write("Complete CPF: %s \n" %cpf_)
    archive.close()



print("\t\t\t\t\t\tCoded by rn0g\n\n")
generate_cpf()








