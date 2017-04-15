from Grammar import Lexer
from Handler import Handler
from Parser import Parser


def compile(p):

    lexer = Lexer(p)
    parser = Parser(lexer)
    tokens = parser.parse()
    handler = Handler()

    nfa_stack = []

    for t in tokens:
        handler.handlers[t.name](t, nfa_stack)

    assert len(nfa_stack) == 1
    return nfa_stack.pop()