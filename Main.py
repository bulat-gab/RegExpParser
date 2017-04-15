import unittest

import Regex
from IO import IO


def test():
    nfa = Regex.compile('0|1')

    print(nfa.match(''))

if __name__ == '__main__':
    unittest.main()

class TestRegexParser(unittest.TestCase):
    def test_simple_match(self):
        nfa = Regex.compile('0')
        result = nfa.match('0')
        self.assertEqual(True, result)

    def test_klenee_star(self):
        nfa = Regex.compile('01*')
        result = nfa.match('011')
        self.assertEqual(True, result)

