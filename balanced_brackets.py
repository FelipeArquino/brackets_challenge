#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.
def isBalanced(brackets):
    closing_bracket = None
    list_brackets = []
    list_results = []

    while brackets != "":
        if closing_bracket == -1:
            return "NO"
        closing_bracket = brackets.rfind(getClosingBracket(brackets[0]))
        sub_brackets = brackets[0:closing_bracket+1]
        list_brackets.append(sub_brackets[1:-1])
        brackets = brackets.replace(sub_brackets, "")

    if closing_bracket is not None:
        for b in list_brackets:
            list_results.append(isBalanced(b))
    for result in list_results:
        if result == "NO":
            return "NO"
    return "YES"

def getClosingBracket(bracket):
    if bracket == '(':
        return ')'
    if bracket == '[':
        return ']'
    if bracket == '{':
        return '}'
    return '*'

if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
