# Non deterministic finite state automaton

# Global variables used to build path in NFA that matches given regExp

stack_size = 0 # depth of recursion
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
        del self


class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        end.is_end = True

        # self.num_of_states initialized only in the last NFA, intermediate NFAs dont need it.
        # In fact, it is equal to a number of ALL states that are created while processing
        # the regexp. When two NFAs are concatenated the final state of the first NFA
        # merged with the start state of the second NFA, thus two states result in one
        # I don't need to know the actual number of states, because it is used only to prevent
        # an infinite loops while matching the string.
        self.num_of_states = 0


    def match(self, s):
        global stack_size, isFinished, path
        stack_size = 0
        isFinished = False
        path = []

        path.append(self.start)
        self._recursiveMatch(self.start, s)
        stq = ""
        for p in path: stq += (str(p) + " ")

        if len(path) == 1:
            path = []
            stq = "\n"
        #print(stq)
        return path

    def _recursiveMatch(self, cur_st, s):
        global isFinished, stack_size, path

        # Accepting case, string is consumed and final state is reached
        if len(s) == 0 and cur_st.is_end == True:
            stack_size -= 1
            isFinished = True
            return

        # input not consumed, but we have already arrived at final state
        if len(s) != 0 and cur_st.is_end == True:
            stack_size -= 1
            return

        # infinite recursion case, this is crude upper bound for a depth of recursion
        if stack_size > self.num_of_states * len(s)+100:
            stack_size -= 1
            return

        if len(s) != 0:
            if s[0] in cur_st.transitions:
                cur_st = cur_st.transitions[s[0]]
                if cur_st:
                    path.append(cur_st)
                    stack_size += 1
                    self._recursiveMatch(cur_st, s[1:])

                    if isFinished:
                        return
                    else:
                        stack_size -= 1
                        path.pop()
                        cur_st = path[-1]

        for e in cur_st.epsilon_moves:
            cur_st = e
            stack_size += 1
            path.append(cur_st)
            self._recursiveMatch(cur_st, s)

            if isFinished:
                return
            else:
                stack_size -= 1
                path.pop()
                cur_st = path[-1]