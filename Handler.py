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
        self.state_count += 1
        #print("State_count = " + str(self.state_count))
        return State('q' + str(self.state_count))

    def handle_char(self, t, nfa_stack):
        q0 = self.create_state()
        q1 = self.create_state()
        q0.transitions[t.value] = q1
        nfa = NFA(q0, q1)
        nfa_stack.append(nfa)

    def handle_concat(self, t, nfa_stack):
        p1 = nfa_stack.pop()
        p0 = nfa_stack.pop()
        p0.end.is_end = False
        p0.end.epsilon_moves.append(p1.start)
        nfa = NFA(p0.start, p1.end)
        nfa_stack.append(nfa)



    def handle_alt(self, t, nfa_stack):
        """
        :type nfa_stack: NFA
        """
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