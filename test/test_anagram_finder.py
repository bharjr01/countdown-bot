from unittest import TestCase

import src.anagram_finder


class TestAnagramFinder(TestCase):

    def test_find_anagrams_greater_than_3_chars(self):
        params_list = [
            ('ABCDEFGHI', ['BACHED', 'BIFACE', 'CHAFED', 'HIDAGE', 'BIGHEAD']),
            ('BCDEFGHIJ', ['CHIEF', 'FICHE', 'FIDGE', 'GIBED', 'JIBED']),
            ('DEFGHIJKL', ['KLEIG', 'KLIEG', 'LEIGH', 'LIKED', 'FLIDGE'])
        ]

        for params in params_list:
            with self.subTest():
                result = src.anagram_finder.find_anagrams(list(params[0]))
                self.assertEqual(result, params[1])
