from Parser import Parser, Lexer
from Handler import Handler

def compile(p):

    lexer = Lexer(p)
    parser = Parser(lexer)
    tokens = parser.parse()
    handler = Handler()

    nfa_stack = []
    
    for t in tokens:
        handler.handlers[t.name](t, nfa_stack)
    
    assert len(nfa_stack) == 1

    nfa = nfa_stack.pop()
    nfa.num_of_states = handler.state_count
    return nfa

