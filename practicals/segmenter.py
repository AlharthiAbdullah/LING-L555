import sys

text = sys.stdin.readline()


while text:
	text = text.replace('. ', '\n')
	print(text)
	text = sys.stdin.readline()
