import random
from typing import List

__CONSONANTS = list('BCDFGHJKLMNPQRSTVWYXZ')
__VOWELS = list('AEIOU')

"""
There isn't an equal chance of picking every letter in the alphabet.
Less frequently used letters (like Z) should be picked less often.
Hence we need some weighting to our random selection.
"""
__PROB_DIST = {
    'A': 10, 'B': 4, 'C': 8, 'D': 9, 'E': 10, 'F': 7, 'G': 9, 'H': 7, 'I': 10,
    'J': 3, 'K': 6, 'L': 10, 'M': 8, 'N': 10, 'O': 10, 'P': 8, 'Q': 1, 'R': 10,
    'S': 10, 'T': 10, 'U': 10, 'V': 7, 'W': 7, 'X': 2, 'Y': 3, 'Z': 1
}

__CONSONANT_WEIGHTS = [v for k, v in __PROB_DIST.items() if k in __CONSONANTS]
__VOWEL_WEIGHTS = [v for k, v in __PROB_DIST.items() if k in __VOWELS]


def __pick_letter(selection: List[str], weights: List[int], number: int) -> List[str]:
    return random.choices(selection, weights, k=number)


def __pick_consonants(number: int) -> List[str]:
    return __pick_letter(__CONSONANTS, __CONSONANT_WEIGHTS, number)


def __pick_vowels(number: int) -> List[str]:
    return __pick_letter(__VOWELS, __VOWEL_WEIGHTS, number)


def generate(num_vowels: int) -> List[str]:
    vowels = __pick_vowels(num_vowels)
    consonants = __pick_consonants(9-num_vowels)
    letters = vowels + consonants
    random.shuffle(letters)
    return letters
