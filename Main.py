import Regex
from IO import IO

if __name__ == '__main__':
       io = IO()
       lines = io.read("input.txt")
       output = ""
       nfa = Regex.compile(lines[0])
       N = int(lines[1])
       for i in range(0, N):
            output += nfa.match(lines[2+i]) + "\n"


       io.write("output.txt", output[:-1])
