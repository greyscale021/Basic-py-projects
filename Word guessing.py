
secret_word =  "My_liege"
guess = ""
guesses = 0
print("(Hint:The only one you value more)")
gues_limit = int(input("Enter guess limit: "))

while guess != secret_word and guesses <= gues_limit:
    guess = input("Enter your guess : ")
    guesses += 1
    if guess == secret_word:
        print("You won!")
        break
    if guesses == gues_limit:
        print("Out of guesses you lose")
        print("Correct guess was (My_liege) ")
        break
    print("Wrong guess")
