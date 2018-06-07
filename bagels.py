import random
def getSecretNum(numDigits):
    #Returns a string that is numDigits long, made up of unique random digits
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    #Returns a string with the pico, fermi, bagels clues to the user
    if guess == secretNum:
        return 'You got it!'

    clue = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagels'

    clue.sort()
    return ' '.join(clue)

def isOnlyDigits(num):
    #Returns true if num is a string made up only of digits. Otherwise returns false
    if num.isdigit() == False: #We could even make this into a try/else
        return false
    #
    # for i in num:
    #     if i not in '0 1 2 3 4 5 6 7 8 9'.split():
    #         return false

    return True

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def instructions():
    clues = {
    'Pico' : 'one digit is correct but in the wrong position',
    'Fermi' : 'one digit is correct and in the right position',
    'Bagels' : 'no digit is correct'
    }
    print('Here are some clues:')
    print('When I say: ')
    for key, value in clues.items():
        print('{}, that means {}'.format(key, value))
    # print('When I say: That means')
    # print('Pico ...one digit is correct but in the wrong position')
    # print('Fermi ...one digit is correct and in the right position')
    # print('Bagels ...no digit is correct')

NUMDIGITS = 3
MAXGUESS = 10

print('I am thinking of a {}-digit number. Try to guess what it is.'.format(NUMDIGITS))
instructions()

while True:
    secretNum = getSecretNum(NUMDIGITS)
    print('I have thought up a number. You have {} guesses to get it'.format(MAXGUESS))

    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess = ''
        while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
            print('Guess #{}: '.format(numGuesses))
            guess = input()

        clue = getClues(guess, secretNum)
        print(clue)
        numGuesses += 1

        if guess == secretNum:
            break
        if numGuesses > MAXGUESS:
            print('You ran out of guesses. The answer was {}'.format(secretNum))

    if not playAgain():
        break
