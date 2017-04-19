# RegExpParser

This program converts a regular expression into a corresponding non deterministic finite automata using Thompson's algorithm. Based on the https://github.com/xysun/regex implementation of converting regex to automaton
Also, it builds an execution trace for input string.

Supports only POSIX regular expressions(Kleene star "*", concatenation "\b" also denoted as dot, alternation "|", brackets)

How to use:

  nfa = Regex.compile("YOUR_REGEX_HERE")
  path = nfa.match("INPUT_STRING")
  
 """ path: q0 q1 ... qn OR empty, if not matched """ 



More detailed description coming later...
