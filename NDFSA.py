# Non deterministic finite state automaton

class State:
    def __init__(self, name):
        self.epsilon_moves = []
        self.transitions = {}
        self.name = name
        self.is_end = False

class NFA:
    def __init__(self, start: State, end: State) -> object:
        self.start = start
        self.end = end
        self.is_end = True

    def add_state(self, state, state_set):
        if state in state_set:
            return
        state_set.add(state)
        for e in state.epsilon_moves:
            self.add_state(e, state_set)

    def match(self, input_str):
        current_states = set()
        self.add_state(self.start, current_states)

        for character in input_str:
            next_states = set()
            for state in current_states:
                if character in state.transitions.keys():
                    trans_state = state.transitions[character]
                    self.add_state(trans_state, next_states)

            current_states = next_states

        for state in current_states:
            if state.is_end:
                return True
            return False









