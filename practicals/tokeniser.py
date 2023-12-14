import sys

sent_id = 1
for line in sys.stdin:
	line = line.strip()
	line = line.replace('(', ' ( ')
	line = line.replace(')', ' ) ')
	line = line.replace(',', ' , ')
	line = line.replace(':', ' : ')
	tokens = line.split()
	for i, token in enumerate(tokens):
		print(f"{i+1}\t{token}\t_\t_\t_\t_\t_\t_\t_\t_")
	print()
	sent_id +=1
