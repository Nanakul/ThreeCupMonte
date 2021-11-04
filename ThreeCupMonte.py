from random import shuffle

#Initial Starting Cup
threecups =  [' ', 'O', ' ']

#Shuffle Cups
def shuffle_cups(threecups:list) -> list: #NOTE (arguement: type) -> *Arrow indicates expected return type)* list
    shuffle(threecups)
    return threecups

#Player makes their guess
def player_guess() -> int:
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input('Pick a number: 0, 1, or 2!\n')

    return int(guess)

#Game checks player's guess to see if it was correct
def check_guess(threecups, guess) -> bool:
    if threecups[guess] == 'O':
        print('Nice job!')
        return True
    else:
        print('Better luck next time!')
        print(threecups)
        return False

        
def playGame():
    while True:
        mixcups = shuffle_cups(threecups)
        guess = player_guess()
        if check_guess(mixcups, guess) == True:
            break

playGame()