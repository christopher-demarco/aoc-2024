#!/usr/bin/env python

import itertools
import sys

def parse_line(line):
    line = line.rstrip()
    result, inputs = line.split(': ')
    result = int(result)
    inputs = inputs.split()
    return result, inputs

def generate_operator_combinations(n):
    combinations = list(itertools.product(['+', '*'], repeat=n-1))
    return combinations

def construct_expression(inputs, operators):
    expression = \
        list(itertools.chain.from_iterable(
            list(zip(inputs[:-1], operators)))) \
        + inputs[-1:]
    return expression

def evaluate_expression(expression, rest):
    if rest != []:
        str_expression = ' '.join(expression)
        result = eval(str_expression)
        expression =  [str(result)] + rest[:2]
        rest = rest[2:]
        return evaluate_expression(expression, rest)
    else:
        result = eval(' '.join(expression))
        return result

def evaluate_line(line):
    expected, inputs = parse_line(line)
    operator_combinations = generate_operator_combinations(len(inputs))
    for operators in operator_combinations:
        expression = construct_expression(inputs, operators)
        result = evaluate_expression(expression[:3], expression[3:])
        if result == expected:
            return result
        else:
            continue
    return 0


if __name__ == '__main__':

    total = 0

    with open(sys.argv[1], 'r') as ifh:
        for line in ifh.readlines():
            # print(line)
            result = evaluate_line(line)
            # print(result)
            total += result

    print(total)
