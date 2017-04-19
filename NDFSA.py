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


    def match(self, s):
        global stack_size, isFinished, path
        stack_size = 0
        isFinished = False
        path = []

        path.append(self.start)
        self._recur_match(self.start, s)
        stq = ""
        for p in path: stq += (str(p) + " ")
        print(stq)
        if len(path) == 1:
            path = []
            stq = "\n"
        #return stq if path else ""
        return True if path else False

    def _recur_match(self, cur_st, s):
        global isFinished, stack_size, path
        if len(s) == 0 and cur_st.is_end == True:
            stack_size -= 1
            isFinished = True
            # path.append(self.end)
            return

        # input not consumed, but we already arrived at final state
        if len(s) != 0 and cur_st.is_end == True:
            stack_size -= 1
            return

        # infinite recursion
        if stack_size > self.num_of_states * len(s)+100:
            stack_size -= 1
            return

        if len(s) != 0:
            if s[0] in cur_st.transitions:
                cur_st = cur_st.transitions[s[0]]
                if cur_st:
                    path.append(cur_st)
                    stack_size += 1
                    self._recur_match(cur_st, s[1:])

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
            self._recur_match(cur_st, s)
            #cur_st = self._goBack()
            if isFinished:
                return
            else:
                stack_size -= 1
                path.pop()
                cur_st = path[-1]



    def _goBack(self):
        if path:
            path.pop()
            return path[-1]
        else:
            raise Exception("Path is empty, can't go back")






