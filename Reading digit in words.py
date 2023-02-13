#!/usr/bin/env python
# coding: utf-8

# In[3]:


def spell_out_number(number):
    # Dictionary to store the spelling of numbers from 0 to 19
    single_digit_numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }

    # Dictionary to store the spelling of numbers from 20 to 90 in increments of 10
    tens_place_numbers = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }

    if number < 20:
        # Return the spelling of numbers 0 to 19
        return single_digit_numbers[number]
    elif number < 100:
        # Return the spelling of numbers 20 to 99
        tens_digit = number // 10
        ones_digit = number % 10
        if ones_digit == 0:
            return tens_place_numbers[tens_digit]
        else:
            return tens_place_numbers[tens_digit] + "-" + single_digit_numbers[ones_digit]
    elif number < 1000:
        # Return the spelling of numbers 100 to 999
        hundreds_digit = number // 100
        tens_and_ones = number % 100
        if tens_and_ones == 0:
            return single_digit_numbers[hundreds_digit] + " hundred"
        else:
            return single_digit_numbers[hundreds_digit] + " hundred " + spell_out_number(tens_and_ones)
    elif number < 10000:
        # Return the spelling of numbers 1000 to 9999
        thousands_digit = number // 1000
        hundreds = number % 1000
        if hundreds == 0:
            return single_digit_numbers[thousands_digit] + " thousand"
        else:
            return single_digit_numbers[thousands_digit] + " thousand " + spell_out_number(hundreds)

print(spell_out_number(4055))
print(spell_out_number(4110))
print(spell_out_number(3402))
print(spell_out_number(45))


# In[ ]:




