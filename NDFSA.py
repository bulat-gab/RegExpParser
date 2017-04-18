# Non deterministic finite state automaton


stack_size = 0
isFinished = False
path = []

class State:
    def __init__(self, name):
        self.epsilon_moves = []
        self.transitions = {} # char : state
        self.name = name
        self.is_end = False


    def __str__(self):
        return self.name

    def dispose(self):
        self.epsilon_moves = None
        self.transitions = None
        self.name = "NONE"
        self.is_end = None


class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        end.is_end = True

        self.num_of_states = 0

    def addstate(self, state, state_set): # add state + recursively add epsilon transitions
        if state in state_set:
            return
        state_set.add(state)
        for eps in state.epsilon_moves:
            self.addstate(eps, state_set)
    """
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
    """


    def match(self, s):
        self._recur_match(self.start, s)
        for p in path: print(p)

    def _recur_match(self, cur_st, s):
        global isFinished, stack_size, path
        if len(s) == 0 and cur_st.is_end == True:
            stack_size -= 1
            return

        # input not consumed, but we already arrived at final state
        if len(s) != 0 and cur_st.is_end == False:
            stack_size -= 1
            return

        # infinite recursion
        if stack_size > self.num_of_states * len(s):
            stack_size -= 1
            return

        if len(s) != 0:
            if cur_st.transitions:
                cur_st = cur_st.transitions.values()[0]
                path.append(cur_st)
                stack_size += 1
                self._recur_match(cur_st, s[1:])

                if isFinished:
                    return
                else:
                    stack_size -= 1
                    path.pop()
                    cur_st = path[-1]
                    return

            else:
                for e in cur_st.epsilon:
                    cur_st = e
                    stack_size += 1
                    path.append(cur_st)
                    self._recur_match(cur_st, s)
                    #cur_st = self._goBack()
                    path.pop()

    def _goBack(self):
        if path:
            path.pop()
            return path[-1]
        else:
            raise Exception("Path is empty, can't go back")






