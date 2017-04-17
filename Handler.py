from NDFSA import State, NFA


class Handler:
    def __init__(self):
        self.handlers = {'CHAR' : self.handle_char,
                         'CONCAT' : self.handle_concat,
                         'ALT' : self.handle_alt,
                         'STAR' : self.handle_star
                         }
        self.state_count = 0

    def create_state(self):
        new_state = State('q' + str(self.state_count))
        self.state_count += 1
        #print(str(new_state) + " ") # TODO remove print_state

        return new_state

    def handle_char(self, t, nfa_stack):
        q0 = self.create_state()
        q1 = self.create_state()
        q0.transitions[t.value] = q1
        nfa = NFA(q0, q1)
        nfa_stack.append(nfa)

    def handle_concat(self, t, nfa_stack):
        p1 = nfa_stack.pop()
        p0 = nfa_stack.pop()
        #p0.start.epsilon_moves.append(p1.start)

        for key, value in p0.start.transitions.items():
            if value == p0.end:
                p0.start.transitions[key] = p1.start

        p0.end.dispose()
        #self.state_count -= 1
        nfa = NFA(p0.start, p1.end)
        nfa_stack.append(nfa)



    def handle_alt(self, t, nfa_stack):
        p1 = nfa_stack.pop()
        p0 = nfa_stack.pop()
        q0 = self.create_state()
        q0.epsilon_moves = [p0.start, p1.start]
        q1 = self.create_state()
        p0.end.epsilon_moves.append(q1)
        p1.end.epsilon_moves.append(q1)
        p0.end.is_end = False
        p1.end.is_end = False
        nfa = NFA(q0, q1)
        nfa_stack.append(nfa)


    def handle_star(self, t, nfa_stack):
        p0 = nfa_stack.pop()
        q0 = self.create_state()
        q1 = self.create_state()
        q0.epsilon_moves = [p0.start]
        q0.epsilon_moves.append(q1)
        p0.end.epsilon_moves.extend([q1, p0.start])
        p0.end.is_end = False
        nfa = NFA(q0, q1)
        nfa_stack.append(nfa)