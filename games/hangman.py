

def hangmanMain():
    lowerWord = randomizer()
    underscore(lowerWord)

    # Make lowerword into a list
    lowerList = list(lowerWord)

    correctLetters = []
    chances = 5

    while chances > 0:
        guessLetters = input("\nWhat is your letter guess? ").lower()

        if guessLetters in correctLetters:
            print(f"You already guessed the letter '{guessLetters}'. Try a different one!")
            continue

        correctLetters.append(guessLetters)

        if set(correctLetters) == set(lowerList):
            print(f"\nYou win! The word is '{lowerWord.capitalize()}'")
            break
        else:
            for char in guessLetters:
                if char not in lowerList:
                    chances -= 1
                    print(f"Letter {guessLetters} is not included! Try Again!")
                    print("\n",f"You only have {chances} left! Be careful!")

        print(hangmanPics(chances))
        underscoreGuess(lowerWord, correctLetters)
    
    if chances == 0:
        print(f"\nSorry but you failed because your chances now are {chances}. The word was '{lowerWord.capitalize()}'")

# UI for instruction
def underscore(word) -> str:

    print("Guess the word: ")
    for i in range(len(word)):
        print("_", end="  ")
    print("\n")


# Chooses a random word
def randomizer()-> str:
    import random
    
    # Food list
    food = ["Apple", "Bread", "Rice", "Milk", "Egg", "Fish", "Meat", "Cheese", "Sugar", "Water"]

    # Country list
    countries = ["USA", "Canada", "China", "India", "Japan", "Brazil", "France", "Germany", "Italy", "Australia"]

    # Animal list
    animals = ["Dog", "Cat", "Cow", "Horse", "Lion", "Tiger", "Fish", "Bird", "Snake", "Elephant"]

    while True:
        categoryChoice = input("""\nChoose a category you want to guess:     
                                        
        a. Food
        b. Country
        c. Animals                          
                                
Type the letter you have chosen: """)
        
        if categoryChoice.lower() == 'a':
            wordPool = food
        elif categoryChoice.lower() == 'b':
            wordPool = countries
        elif categoryChoice.lower() == 'c':
            wordPool = animals
        else:
            print("Just choose between a, b, and c!")
            continue


        randomWord = random.choice(wordPool)
        lowerCase = randomWord.lower()
        return lowerCase


# Prints underscore/letter based on correctness of guess
def underscoreGuess(word: str, correctGuess: list) -> str:
    for letter in word:
        if letter in correctGuess:
            print("", letter.upper(), "" , end="")
        else:
            print(" _ ", end="")

def hangmanPics(index):
    HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    
    if index == 5:
        return HANGMANPICS[0]
    elif index == 4:
        return HANGMANPICS[1]
    elif index == 3:
        return HANGMANPICS[2]
    elif index == 2:
        return HANGMANPICS[3]
    elif index == 1:
        return HANGMANPICS[4]
    else:
        return HANGMANPICS[5]


