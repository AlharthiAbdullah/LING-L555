import sys

vowels = 0
total = 0

for c in sys.stdin.read():
        if c in " " :

                total = total + 1

        if c in "\n" :

                total = total + 1

        if c in 'AEIOUIeaeiouie' :
                vowels = vowels + 1

# average number of vowels per word
average = vowels / total


print(vowels)
print(average)
