import sys

counter1 = 0
counter2 = 0
counter3 = 0

for c in sys.stdin.read():

        if c in "ABĊDEFĠGGħHĦIIeJKLMNOPQRSTUVWXŻZabċdefġggħhħiiejklmnopqrstuvwxżz" :

                counter3 = counter3 + 1

        if c in " " :

                counter1 = counter1 + 1

        if c in "\n" :

                counter2 = counter2 + 1

print(counter1)
print(counter2)
print(counter3)
