#
#       Name: Josephine Nguyen
#       Class: CS 3750.02
#       Description:            A recreation of the game, Hangman. Requires a list of phrases/words in a text file named "phrases.txt" where every line is
#                               a phrase.
#

import random

FILE_PATH = "phrases.txt"

#global variables:
phrasesList = []
phraseProgress = []             #tracks user's progress
solution = ""


#initialPhrases():
#Purpose:       Reads all phrases from file and initializes into global "phrasesList". Ensures to cut off the '\n' at the end of every phrase
def initialPhrases():
    global phrasesList
    phrasesList = []
    phrasesFile = open(FILE_PATH, "r")
    for line in phrasesFile:
        phrasesList.append(line[0:len(line)-1])     #save the entire line except for the last char


#getSolution():
#Purpose:       Chooses a random phrase from "phrasesList" as a solution, converts to uppercase for easy parsability
def getSolution():
    global phrasesList, solution
    lineNum = random.randint(1, len(phrasesList))
    solution = (phrasesList.__getitem__(lineNum-1).upper())


#createEmptySpaces():
#Purpose:       To create a list of the correct number of '_', accounting for spaces between words, apostrophe's, etc in the phrase
def createEmptySpaces():
    global solution
    emptyPhrase= []
    #Iterate word, if token is letter, save a '_', else --> save for what it is
    for token in solution:
        if(token.isalpha()):
            emptyPhrase.append('_')
        else:
            emptyPhrase.append(token)
    return emptyPhrase


#drawHanging():
#Purpose:       Draws the correct hanging position picture according to how many tries are left
def drawHanging(triesLeft):
    if triesLeft == 6:
        print("----------|\n|\n|\n|\n____________")
    elif triesLeft == 5:
        print("---------- |\n|          O\n|\n|\n____________")
    elif triesLeft == 4:
        print("---------- |\n|          O\n|          |\n|\n____________")
    elif triesLeft == 3:
        print("---------- |\n|          O\n|         /|\n|\n____________")
    elif triesLeft == 2:
        print("---------- |\n|          O\n|         /|\\\n|\n____________")
    elif triesLeft == 1:
        print("---------- |\n|          O\n|         /|\\\n|         /\n____________")
    elif triesLeft == 0:
        print("---------- |\n|          O\n|         /|\\\n|         / \\\n____________")


#updateProgess():
#Purpose:       Updates the List to reveal every space that was guessed correctly. Returns the List
def updateProgress(guess):
    global phraseProgress, solution
    for index in range(len(solution)):
        if(solution[index] == guess):
            phraseProgress[index] = guess


#execute()
#Purpose:       The "main" method to execute the game
def execute():
    global phraseProgress, solution
    #1.) Read File and Choose a solution:
    initialPhrases()        #initialize "phrases" List
    getSolution()

    #2.) Create empty List of '_':
    phraseProgress = createEmptySpaces()

    #Variables to track: # of tries have done, # of letters and words already guessed
    triesLeft = 6
    lettersGuessed = []
    phrasesGuessed = []
    correct = False
    round = 1


    #----------Play starts----------------------------
    #1.) Print instructions:
    print("\n\n---------------------------------------------------------------------------------------------------------------------")
    print("Welcome to Hangman!\n\nRULES:\n\t1.) You have 6 tries to get the phrase. Every time you guess incorrectly, a body part will be hung!\n\t2.) You can either guess one letter or guess the entire solution, nothing else!\n\nTake your time, and have fun!")
    print("---------------------------------------------------------------------------------------------------------------------")

    #2.) Continue gameplay: as long as (1) still have tries (2) have not guessed the word:
    while triesLeft > 0 and not correct:
        #1.) display updated picture and progress:
        print("\n\nRound " + str(round) + ":        # of tries left: " + str(triesLeft))
        print("                - letters guessed: " + str(lettersGuessed))
        print("                - phrases guessed: " + str(phrasesGuessed))
        drawHanging(triesLeft)
        print("\nYour phrase:\t\t", end="")
        for i in phraseProgress:
            print(i, end="")
        print("\n")

        #2.) Ask for a guess, convert to uppercase for easy checking
        guess = input("Type in your guess:\t").upper()

        #3.) Assess the guess:
        #Valid guess:
        #   (1) must be a letter
        #   (2) Must either be length of 1 (a char) or length of solution (phrase being guessed)
        #   (3) Must have not guessed it already
        if len(guess) == 1 and guess.isalpha() and guess not in lettersGuessed:
            #Now can check if in solution:
            lettersGuessed.append(guess)
            if guess in solution:
                print("Good job! " + guess + " was in the phrase!")
                updateProgress(guess)
                if("".join(phraseProgress) == solution):
                    correct = True
            else:
                print("Sorry! " + guess + " was not in the phrase!")
                triesLeft -= 1
        elif len(guess) == len(phraseProgress) and guess not in phrasesGuessed:
            phrasesGuessed.append(guess)
            if guess == solution:
                print("That was the correct phrase!")
                correct = True
            else:
                print("Sorry! " + guess + " was not the phrase!")
                triesLeft -= 1

        #Invalid guess:
        else:
            if guess in lettersGuessed or guess in phrasesGuessed:
                print("You already guessed that! ")
            else:
                print("Sorry! That wasn't a valid guess. Please refer to the rules again!")

        round += 1


    #Conclusion:
    if correct:
        print("\nYou won! The phrase was: " + solution)
    else:
        print("\nYou lost! The correct phrase was: " + solution)


execute()

