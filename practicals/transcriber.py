import sys

vocab = {}
Table = {}
fd = open('table.tsv', 'r')

for line in fd.readlines():
        row = line.strip('\n').split('\t')
        table[row[0]]=row[1]

print(table)

for line in sys.stdin.readlines():
        line = line.strip('\n')
        if '\t' not in line:
                print(line)
                continue

        row = line.split('\t')
        if len(row) != 10:
                continue
        form = row[1]
        row[9]= form

        print('\t'.join(row))
