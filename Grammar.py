# Grammar file contains regular expression's partition on tokens

class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Lexer:
    def __init__(self, pattern):
        self.pattern = pattern
        self.symbols = { '(' : 'LEFT_PAREN', ')' : 'RIGHT_PAREN',
                         '*' : 'STAR', '|' : 'ALT'}
        self.cur_index = 0
        self.length = len(self.pattern)

    def get_token(self):
        if self.cur_index < self.length:
            char = self.pattern[self.cur_index]
            self.cur_index += 1

            if char not in self.symbols.keys():
                token = Token('CHAR', char)
            else:
                token = Token(self.symbols[char], char)
            return token
        else:
            return Token('NONE', '')