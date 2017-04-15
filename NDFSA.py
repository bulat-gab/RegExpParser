# Non deterministic finite state automaton


class State:
    def __init__(self, name):
        self.epsilon_moves = []
        self.transitions = {} # char : state
        self.name = name
        self.is_end = False

class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        end.is_end = True

    def addstate(self, state, state_set): # add state + recursively add epsilon transitions
        if state in state_set:
            return
        state_set.add(state)
        for eps in state.epsilon_moves:
            self.addstate(eps, state_set)

    def match(self,s):
        current_states = set()
        self.addstate(self.start, current_states)

        for c in s:
            next_states = set()
            for state in current_states:
                if c in state.transitions.keys():
                    trans_state = state.transitions[c]
                    self.addstate(trans_state, next_states)


            current_states = next_states

        for s in current_states:
            if s.is_end:
                return True
        return False









