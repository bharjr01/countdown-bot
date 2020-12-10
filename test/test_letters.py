from unittest import TestCase

import src.letters


class TestLetters(TestCase):

    def test_generate_random_letters(self):
        for i in range(0, 10):
            with self.subTest():
                result = src.letters.generate(i)

                num_vowels = count_vowels(result)
                num_consonants = count_consonants(result)

                self.assertEqual(num_vowels, i)
                self.assertEqual(num_consonants, 9-i)


def count_vowels(haystack):
    return count(src.letters.__VOWELS, haystack)


def count_consonants(haystack):
    return count(src.letters.__CONSONANTS, haystack)


def count(needles, haystack):
    return [c in needles for c in haystack].count(True)
