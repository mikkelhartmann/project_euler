"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there 
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how 
many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 
23 letters and 115 (one hundred and fifteen)contains 20 letters. The use of "and" when writing 
out numbers is in compliance with British usage.
"""
num_to_word = dict()
num_to_word[0] = ""
num_to_word[1] = "one"
num_to_word[2] = "two"
num_to_word[3] = "three"
num_to_word[4] = "four"
num_to_word[5] = "five"
num_to_word[6] = "six"
num_to_word[7] = "seven"
num_to_word[8] = "eight"
num_to_word[9] = "nine"
num_to_word[10] = "ten"
num_to_word[11] = "eleven"
num_to_word[12] = "twelve"
num_to_word[13] = "thirteen"
num_to_word[14] = "fourteen"
num_to_word[15] = "fifteen"
num_to_word[16] = "sixteen"
num_to_word[17] = "seventeen"
num_to_word[18] = "eighteen"
num_to_word[19] = "nineteen"

num_to_word[20] = "twenty"
num_to_word[30] = "thirty"
num_to_word[40] = "forty"
num_to_word[50] = "fifty"
num_to_word[60] = "sixty"
num_to_word[70] = "seventy"
num_to_word[80] = "eighty"
num_to_word[90] = "ninety"

# num_to_word[100] = "onehundred"

num_to_word[1000] = "onethousand"
import numpy as np


def tens_to_string(num):
    tens = int(np.floor(num/10)*10)
    reminder = num % tens
    
    words = num_to_word[tens] + num_to_word[reminder] 

    num_letters = len(num_to_word[tens]) + len(num_to_word[reminder])
    return words, num_letters 
    

total_letters = 0
for num in range(1,1001):
    if ((num<21) or num==1000):
        words = num_to_word[num]
        total_letters += len(words)
        print(num, words, len(words), total_letters)
    
    if 20<num<100:
        words, num_letters = tens_to_string(num)
        total_letters += len(words)
        print(num, words, len(words), total_letters)
    if 99<num<1000:
        hundreds = int(np.floor(num/100))
        reminder = num % (int(np.floor(num/100))*100)
        if reminder == 0:
            words = num_to_word[hundreds]+"hundred"
            total_letters += len(words)
            print(num, words, len(words), total_letters)
        elif reminder<21:
            words = num_to_word[hundreds]+"hundredand" + num_to_word[reminder]
            total_letters += len(words)
            print(num, words, len(words), total_letters)
        else:
            words_hundreds = num_to_word[hundreds]+"hundredand"
            words_tens, num_letters = tens_to_string(reminder)
            words = words_hundreds + words_tens
            total_letters += len(words)
            print(num, words, len(words), total_letters)

print("total", total_letters)
print(total_letters == 21124)


