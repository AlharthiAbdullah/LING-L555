import sys

vocab = {} # dict to store frequency list

# for each of the lines of input
for line in sys.stdin.readlines():
    # strip any excess newlines
        line = line.strip('\n')
    # if there is no tab character, skip the line
        if '\t' not in line:
                continue
    # make a list of the cells in the row
        row = line.split('\t')
    # if there are not 10 cells, skip the line
        if len(row) != 10:
                continue
    # the form is the value of the second cell
        form = row[1]
    # if we haven't seen it yet, set the frequency count to 0
        if form not in vocab:
                vocab[form] = 0
        vocab[form] = vocab[form] + 1

# I used the sorted() function because (the sort from list method which is in the practicals) didn't work for me for some reason!
# sort and print out the frequency list
for w in sorted(vocab, key=vocab.get, reverse=True):
        print('%d\t%s' % (vocab[w], w))

# Open the file freq.txt in write mode
fd = open('freq.txt', 'w+')
# For each of the items in the frequency list
for (f, w) in sorted(vocab, key=vocab.get, reverse=True):
    # Write out the frequency and the word to the file
    # separated by the tab character
        fd.write('%d\t%s\n' % (f, w))
# Close the file
fd.close()

fd = open('freq.txt', 'r')
for (f, w) in sorted(vocab, key=vocab.get, reverse=True):
        fd.read('%d\t%s\n' % (f, w))
