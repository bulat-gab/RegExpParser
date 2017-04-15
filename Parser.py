from Grammar import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokens = []
        self.next_token = self.lexer.get_token()

    def consume(self, name):
        if self.next_token.name == name:
            self.next_token = self.lexer.get_token()
        else:
            raise Exception

    def parse(self):
        self.exp()
        return self.tokens

    def exp(self):
        self.term()
        if(self.next_token.name == 'ALT'):
            t = self.next_token
            self.consume('ALT')
            self.exp()
            self.tokens.append(t)

    def term(self):
        self.factor()
        if self.next_token.value not in ')|':
            self.term()
            self.tokens.append(Token('CONCAT', '\b'))

    def factor(self):
        self.primary()
        if self.next_token.name == 'STAR':
            self.tokens.append(self.next_token)
            self.consume(self.next_token.name)

    def primary(self):
        if self.next_token.name == 'LEFT_PAREN':
            self.consume('LEFT_PAREN')
            self.exp()
            self.consume('RIGHT_PAREN')
        elif self.next_token.name == 'CHAR':
            self.tokens.append(self.next_token)
            self.consume('CHAR')

