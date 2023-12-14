import sys

vowels = 0
consonants = 0

for c in sys.stdin.read():
        if c in 'AEIOUIeaeiouie' :
                vowels = vowels + 1


        if c in 'BĊDFĠGGħHĦJKLMNPQRSTVWXŻZbċdfġggħhħjklmnopqrstvwxżz' :
                consonants = consonants + 1

print(vowels)
print(consonants)
