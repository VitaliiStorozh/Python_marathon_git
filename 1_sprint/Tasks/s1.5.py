# Convert a certain expression like 2+3 to expression in a postfix notation.
#
# The given expression can have one of the following tokens:
#
# a number;
# a parenthesis;
# arithmetic operator:
# subtraction (-);
# addition (+);
# multiplication (*);
# division (/);
# modulo operation (%).
# Example:
#
# For expression = ["2","+","3"] the output should be ["2","3","+"].
#
# [execution time limit] 4 seconds (py)
#
# [input] array.string expression
#
# An array of tokes of a valid expression in the standard notation.
#
# [output] array.string
#
# Tokens of the expression in the postfix notation.


def toPostFixExpression(e):
    out = []
    stack = []
    operators1 = ["-", "+"]
    operators2 = ["*", "/", "%"]
    operators3 = ["(", ")"]
    for i in range(len(e)):
        if e[i].isdigit():
            out.append(e[i])
        elif e[i] in operators1 or operators2 or operators3:
            if stack == [] or stack[-1] == '(':
                stack += e[i]
            elif e[i] in operators2 and stack[-1] in operators1:
                stack += e[i]
            elif e[i] in operators2 and stack[-1] in operators2:
                while stack[-1] in operators2:
                    out += stack.pop(-1)
                out += exp[i]
            elif e[i] in operators1 and stack[-1] in operators1:
                while stack[-1] in operators1:
                    out += stack.pop(-1)
                out += e[i]
            elif e[i] == '(':
                stack += e[i]
            elif e[i] == ')':
                while stack[-1] != '(':
                    out += stack.pop(-1)
                stack.remove('(')
    while stack != []:
        out += stack.pop(-1)
    return out


print(toPostFixExpression(["2", "+", "3"]))
print(toPostFixExpression(["20", "+", "3", "*", "(", "5", "*", "4", ")"]))
print(toPostFixExpression(["(", "(", "(", "1", "+", "2", ")", "*", "3", ")", "+", "6", ")", "/", "(", "2", "+", "3", ")"]))
