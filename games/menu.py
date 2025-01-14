from games import guessTheNumber, hangman, aboutTheDevs

# Create a Menu

'''

1. Hangman
2. Guess the Answer
3. Exit
4. About the Devs


'''

def main():
    print('''
    Uy! Ikaw pala yan bossing! Musta ang buhay-buhay? 
    Pili ka lang ng number na gusto mo, ako bahala sa'yo
    ''')

    while True:
        print('''
        1. Play Hangman
        2. Play Guess-the-number
        3. Exit
        4. About the Devs
        ''')

        optionMenu = int(input("Enter the number: "))

        try:
            if optionMenu <= 0 or optionMenu >= 5:
                print("Sabing 1 to 4 eh! Sasapakin na kita")
            elif optionMenu == 1:
                hangman()    
            elif optionMenu == 2:
                guessTheNumber()
            elif optionMenu == 4:
                aboutTheDevs()
            else:
                print("Salamat sa 10k boss!\n")
                exit()
        except ValueError:
                print("Invalid and na-type mo! Numbers from 1 to 4 lang nga sabi.")

    

main()
