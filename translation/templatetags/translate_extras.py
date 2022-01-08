from django import template

import re

letters_numbers = {
    'w': 'و',
    'e': 'ي',
    'r': 'ر',
    't': 'ت',
    'y': 'ي',
    'i': 'ي',
    'o': 'و',
    'a': 'ا',
    's': 'س',
    'd': 'د',
    'f': 'ف',
    'g': 'ق',
    'h': 'ه',
    'k': 'ك',
    'c': 'ك',
    'l': 'ل',
    'z': 'ز',
    'j': 'ج',
    'b': 'ب',
    'n': 'ن',
    'm': 'م',
    '2': 'ء',
    '3': 'ع',
    '4': 'ذ',
    '5': 'خ',
    '6': 'ط',
    '7': 'ح',
    '8': 'ق',
    '9': 'ص',
    ',': ',',
}

digraphs = {
    'sh': 'ش',
    'ch': 'ج',
    "6'": 'ظ',
    "3'": 'غ',
    "9'": '1',
    "t'": 'ث',
}

register = template.Library()


@register.simple_tag
def translate(sentence):
    sentence = sentence.lower()
    for key in digraphs.keys():
        find_letter = re.compile(r'{}'.format(key))
        two_letters = find_letter.findall(sentence)
        grouped_letters = two_letters

        for keys, values in digraphs.items():
            for di in grouped_letters:
                if keys == di:
                    sentence = sentence.replace(di, digraphs[keys])

    for key, value in letters_numbers.items():
        for letter in sentence:
            if letter == key:
                x = sentence.replace(letter, value)
                sentence = x
    # reshapes arabic letters to make them linked
    return sentence
