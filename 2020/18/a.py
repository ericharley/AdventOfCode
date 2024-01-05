#lines = open('test.txt').read().strip().split('\n')
lines = open('input.txt').read().strip().split('\n')

ops = set(['+', '*', '(', ')'])

def infixToRPN(exp, p):
    s = []
    output = ''

    for c in exp:
        if c not in ops:
            output += c

        elif c == '(':
            s.append('(')

        elif c == ')':
            while s and s[-1] != '(':
                output += s.pop()
            s.pop()

        else: 
            while s and s[-1] != '(' and p[c] <= p[s[-1]] :
                output += s.pop()
            s.append(c)

    while s:
        output += s.pop()

    return output

def evalRPN(rpn):
  s = []

  for c in rpn:
    if c.isdigit():
      s.append(int(c))

    elif c in ops:
      if c == '*':
        s.append(s.pop() * s.pop())

      elif c == '+':
        s.append(s.pop() + s.pop())

  return(s.pop())

p = {'+':1, '*':1}
print(sum([evalRPN(infixToRPN(line, p)) for line in lines]))

p = {'+':2, '*':1}
print(sum([evalRPN(infixToRPN(line, p)) for line in lines]))
