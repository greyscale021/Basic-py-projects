#language creator (Every vowel -> anyword)

def translation (phrase):
    translated = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translated += x.upper()
            else:
                translated += x.lower()
        else:
            translated += letter
    return translated

x = input("Enter a word to exchange with vowels: ")

print(translation(input("Enter a phrase: ")))
