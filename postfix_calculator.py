#!/usr/bin/env python3

import fileinput
from collections import deque

def eval_postfix(tokens):
	stack = deque()

	for token in tokens:
		assert len(stack) < 50, 'Stack too big!'

		if token in ('+', '-', '*', '/'):
			arg_two = stack.pop()
			arg_one = stack.pop()

			if token == '+':
				stack.append(arg_one + arg_two)
			elif token == '-':
				stack.append(arg_one - arg_two)
			elif token == '*':
				stack.append(arg_one * arg_two)
			elif token == '/':
				stack.append(arg_one / arg_two)
		else:
			stack.append(float(token))

	output = stack.pop()
	assert len(stack) == 0, 'Stack should be empty when tokens are exhausted'

	return output

for line in fileinput.input():
	s = line.strip()

	if s:
		print(eval_postfix(s.split(' ')))
