#!/usr/bin/python3
"""
a function def roman_to_int(roman_string):
that converts a Roman numeral to an integer
"""


def roman_to_int(roman_string):
    n_places = {'1000': 1000, '100': '100', '10': 10, '1': 1}
    roman_letters_dict = {'1000': ['M', 'MM', 'MMM'],
                          '100': ['C', 'CC', 'CCC', 'CD', 'D', 'DC',
                                  'DCC', 'DCCC', 'CM'],
                          '10': ['X', 'XX', 'XXX', 'XL', 'L', 'LX',
                                 'LXX', 'LXXX', 'XC'],
                          '1': ['I', 'II', 'III', 'IV', 'V', 'VI',
                                'VII', 'VIII', 'IX']}

    position = 0
    digit = 0
    if not roman_string or not isinstance(roman_string, str):
        return 0

    for p, v in n_places.items():
        letter_list = roman_letters_dict[p]
        for i in range(len(letter_list), 0, -1):
            letter = letter_list[i - 1]
            sub_let = roman_string[position:len(letter) + position]
            if sub_let == letter:
                position = position + len(letter)
                digit = digit + (int(v) * i)
                break

    return digit
