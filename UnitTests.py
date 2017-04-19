import unittest

import Regex

if __name__ == '__main__':
    unittest.main()



class Test_RegexParse(unittest.TestCase):

    def test_walking(self):
        nfa = Regex.compile('01*')
        result = nfa.match('011')
        print(result)
        #print(result.num_of_states)
        # self.assertEqual(True, result)

    def test_simple_match(self):
        nfa = Regex.compile('0')
        result = nfa.match('0')
        self.assertEqual(True, result)

    def test_klenee_star_match_1(self):
        nfa = Regex.compile('01*')
        result = nfa.match('011')
        self.assertEqual(True, result)
       # self.assertEqual(True, result)

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
        result = nfa.match('01')
        self.assertEqual(True, result)

    def test_from_example_5(self):
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

    def test_from_example_3_1(self):
        nfa = Regex.compile('00(0|1)*')
        result = nfa.match('00000')
        self.assertEqual(True, result)

    def test_from_example_3_2(self):
        nfa = Regex.compile('00(0|1)*')
        result = nfa.match('00')
        self.assertEqual(True, result)

    def test_from_example_3_3(self):
        nfa = Regex.compile('00(0|1)*')
        result = nfa.match('1000')
        self.assertEqual(False, result)

    def test_from_example_3_4(self):
        nfa = Regex.compile('00(0|1)*')
        result = nfa.match('0011')
        self.assertEqual(True, result)


    def test_Mike(self):
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

            for string, answer in tests.items():
                self.assertEqual(nfa.match(string), answer)



    def test_double_star(self):
        nfa = Regex.compile('(1*)*')
        result = nfa.match('1')
        self.assertEqual(True, result)

