import unittest
import Regex


class Test_RegexParse(unittest.TestCase):
    def test_simple_match(self):
        nfa = Regex.compile('0')
        path = nfa.match('0')
        result = True if path else False
        self.assertEqual(True, result)

    def test_klenee_star_match_1(self):
        nfa = Regex.compile('01*')
        path = nfa.match('011')
        result = True if path else False
        self.assertEqual(True, result)

    def test_klenee_star_match_2(self):
        nfa = Regex.compile('0*1*')
        path = nfa.match('00011')
        result = True if path else False
        self.assertEqual(True, result)

    def test_from_example_1(self):
        nfa = Regex.compile('01*')
        path = nfa.match('000011111')
        result = True if path else False
        self.assertEqual(False, result)

    def test_from_example_2(self):
        nfa = Regex.compile('01*')
        path = nfa.match('011111')
        result = True if path else False
        self.assertEqual(True, result)

    def test_from_example_3(self):
        nfa = Regex.compile('01*')
        path = nfa.match('10')
        result = True if path else False
        self.assertEqual(False, result)

    def test_from_example_4(self):
        nfa = Regex.compile('01*')
        path = nfa.match('01')
        result = True if path else False
        self.assertEqual(True, result)

    def test_from_example_5(self):
        nfa = Regex.compile('01*')
        path = nfa.match('0')
        result = True if path else False
        self.assertEqual(True, result)

    def test_from_example_2_1(self):
        nfa = Regex.compile('(0|1)01')
        path = nfa.match('001')
        result = True if path else False
        self.assertEqual(True, result)

    def test_from_example_2_2(self):
        nfa = Regex.compile('(0|1)01')
        path = nfa.match('101')
        result = True if path else False
        self.assertEqual(True, result)

    def test_from_example_2_3(self):
        nfa = Regex.compile('(0|1)01')
        path = nfa.match('010')
        result = True if path else False
        self.assertEqual(False, result)

    def test_from_example_3_1(self):
        nfa = Regex.compile('00(0|1)*')
        path = nfa.match('00000')
        result = True if path else False
        self.assertEqual(True, result)

    def test_from_example_3_2(self):
        nfa = Regex.compile('00(0|1)*')
        path = nfa.match('00')
        result = True if path else False
        self.assertEqual(True, result)

    def test_from_example_3_3(self):
        nfa = Regex.compile('00(0|1)*')
        path = nfa.match('1000')
        result = True if path else False
        self.assertEqual(False, result)

    def test_from_example_3_4(self):
        nfa = Regex.compile('00(0|1)*')
        path = nfa.match('0011')
        result = True if path else False


    def tests_of_my_friend(self):
        testcases = {
            "abc":           {"a": False,  "abc": True},
            "ab|c":          {"ab": True,  "ac": False,  "c": True,         "abc": False},
            "ab*c":          {"ac": True,  "abc": True,  "abbbbbbbc": True, "bc": False,    "ab": False},
            "a(bb)*c":       {"ac": True,  "abc": False, "abbc": True,      "abbbc": False, "abbbbc": True},
            "(ab|cx)*":      {"": True,    "ab": True,   "abab": True,      "cx": True,     "cxcx": True,    "abcx": True},
            "ca*|b":         {"cb": False, "ca": True,   "caaaaa": True,    "c": True},
            "01*":           {"01111": True, "011000": False},
            "(a|b*)*":       {"ab": True, "abba": True},
            "(0|1)01":       {"001": True, "101": True, "010": False}
        }

        for expr, tests in testcases.items():
            nfa = Regex.compile(expr)

            for string, expected_answer in tests.items():
                path = nfa.match(string)
                actual_answer = True if path else False
                self.assertEqual(expected_answer, actual_answer)

    def test_double_star(self):
        nfa = Regex.compile('(1*)*')
        path = nfa.match('1')
        result = True if path else False
        self.assertEqual(True, result)

    def test_complex_example_1_1(self):
        nfa = Regex.compile('11001|01011|01100')
        path = nfa.match('11001')
        result = True if path else False
        self.assertEqual(True, result)

    def test_complex_example_1_2(self):
        nfa = Regex.compile('11001|01011|01100')
        path = nfa.match('01011')
        result = True if path else False
        self.assertEqual(True, result)

    def test_complex_example_1_3(self):
        nfa = Regex.compile('11001|01011|01100')
        path = nfa.match('01100')
        result = True if path else False
        self.assertEqual(True, result)

    def test_complex_example_1_4(self):
        nfa = Regex.compile('11001|01011|01100')
        path = nfa.match('11011')
        result = True if path else False
        self.assertEqual(False, result)

    def test_complex_example_2_1(self):
        nfa = Regex.compile('(0|11*0)*')
        path = nfa.match('00000')
        result = True if path else False
        self.assertEqual(True, result)

    def test_complex_example_2_2(self):
        nfa = Regex.compile('(0|11*0)*')
        path = nfa.match('10')
        result = True if path else False
        self.assertEqual(True, result)

    def test_complex_example_2_3(self):
        nfa = Regex.compile('(0|11*0)*')
        path = nfa.match('11111')
        result = True if path else False
        self.assertEqual(False, result)


