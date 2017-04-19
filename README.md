# RegExpParser

This program converts a regular expression into a corresponding non deterministic finite automata using Thompson's algorithm.
Also, it builds an execution trace for input string.

How to use:

  nfa = Regex.compile("YOUR_REGEX_HERE")
  path = nfa.match("INPUT_STRING")
  
 """ path: q0 q1 ... qn OR empty, if not matched """ 



More detailed description coming later...
