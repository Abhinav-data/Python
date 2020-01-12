import random
wordList = [
"lion", "umbrella", "window", "computer", "glass", "juice", "chair", "desktop",
"laptop", "dog", "cat", "lemon", "cabel", "mirror", "hat"]

guess_word=[]
secretWord=random.choice(wordList)
length_word=len(secretWord)
alphabet="abcdefghijklmnopqrstuvwxyz"
letter_storage=[]

def beginning():
    while True:
        name=input("Enter your name")
        break

beginning()

def change():
    for character in secretWord:
        guess_word.append("*")
    print("The word you need to guess has",length_word,"characters")
    print("You can enter only one letter at a time")

    print(guess_word)

def guessing():
    guess_taken=1
    while guess_taken<10:
        guess=input("Pick a letter\n").lower()

        if not guess in alphabet:
            print("Enter letters from a-z")
        elif guess in letter_storage:
            print("You have already guessed it")
        else:
            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correcty")
                for x in range(0,length_word):
                    if secretWord[x]==guess :
                        guess_word[x]=guess
                        print(guess_word)
                if not "*" in guess_word:
                    print("You Won")
                    break
            else:
                print("Letter is not in the word")
                guess_taken+=1
                if guess_taken==10:
                    print("Sorry you lost")

change()
guessing()

print("Game Over")