#!/bin/python3
from sys import stderr

def count_expressions(x, n, vals):
    
    s = sum(v**n for v in vals)

    print('The current expression looks like:', ' + '.join('{}^{}'.format(v, n) for v in vals), file=stderr)

    if s == x:
        print("We've found a solution!", file=stderr)
        return 1
    else:
        answer = 0
        v = vals[-1] + 1 if vals else 1
        while s + v**n <= x:
            answer += count_expressions(x, n, vals + [v])
            v += 1

        return answer

print(count_expressions(int(input()), int(input()), []))