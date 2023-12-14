fd = open('freq.txt', 'r')
for (f, w) in sorted(vocab, key=vocab.get, reverse=True):
        fd.read('%d\t%s\n' % (f, w))
