import unittest

import Regex

if __name__ == '__main__':
    unittest.main()



class Test_RegexParser(unittest.TestCase):
    def test_simple_match(self):
        nfa = Regex.compile('0')
        result = nfa.match('0')
        self.assertEqual(True, result)

    def test_klenee_star_match_1(self):
        nfa = Regex.compile('01*')
        result = nfa.match('011')
        self.assertEqual(True, result)

    def test_klenee_star_match_2(self):
        nfa = Regex.compile('0*1*')
        result = nfa.match('00011')
        self.assertEqual(True, result)

    def test_from_example_1(self):
        nfa = Regex.compile('01*')
        result = nfa.match('000011111')
        self.assertEqual(False, result)

    def test_from_example_2(self):
        nfa = Regex.compile('01*')
        result = nfa.match('011111')
        self.assertEqual(True, result)

    def test_from_example_3(self):
        nfa = Regex.compile('01*')
        result = nfa.match('10')
        self.assertEqual(False, result)

    def test_from_example_4(self):
        nfa = Regex.compile('01*')
        result = nfa.match('0')
        self.assertEqual(True, result)

    def test_from_example_2_1(self):
        nfa = Regex.compile('(0|1)01')
        result = nfa.match('001')
        self.assertEqual(True, result)

    def test_from_example_2_2(self):
        nfa = Regex.compile('(0|1)01')
        result = nfa.match('101')
        self.assertEqual(True, result)

    def test_from_example_2_3(self):
        nfa = Regex.compile('(0|1)01')
        result = nfa.match('010')
        self.assertEqual(False, result)



