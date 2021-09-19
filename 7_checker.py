with open("file.txt", "r") as fob:
    data = fob.read()

vowels = ("a", "e", "i", "o", "u")

vowel, consonant, upper, lower = 0, 0, 0, 0
for i in data:
    if i.isalpha():
        if i in vowels:
            vowel += 1
        else:
            consonant += 1
        if i.isupper():
            upper += 1
        else:
            lower += 1

print(f"""Vowels: {vowel}
Consonants: {consonant}
Uppercase letters: {upper}
Lowercase letters: {lower}""")