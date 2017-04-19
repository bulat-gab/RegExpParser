# Lexer is a class for performing partition of a regexp into the tokens

class Token:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return self.name + ":" + self.value

class Lexer:
    def __init__(self, pattern):
        self.pattern = pattern
        self.symbols = {'(':'LEFT_PAREN', ')':'RIGHT_PAREN', '*':'STAR',
                        '|':'ALT', '\b':'CONCAT'}
        self.cur_index = 0
        self.length = len(self.pattern)

    def get_token(self):
        if self.cur_index < self.length:
            c = self.pattern[self.cur_index]
            self.cur_index += 1
            if c not in self.symbols.keys(): # CHAR
                token = Token('CHAR', c)
            else:
                token = Token(self.symbols[c], c)
            return token
        else:
            return Token('NONE', '')