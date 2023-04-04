# This is a game of Rock, Paper, Scissors
import random, sys
print('ROCK, PAPER, SCISSORS')

# These variables keep track of the number of wins, losses, and ties
wins = 0
ties = 0
losses = 0

# the main game will loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    # Player input loop
    while True:
        print('Enter your move. (r)ock, (p)aper, (s)cissors, or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Breaks player input and moves to the next code block
        print('Type one of r, p, s, or q.')

# Display what the player chose:
if playerMove == 'r':
    print('ROCK versus...')
elif playerMove == 'p':
    print('PAPER versus...')
elif playerMove == 's':
    print('SCISSORS versus...')

# Display what the computer chose:
randomNumber = random.randint(1, 3)
if randomNumber == 1:
    computerMove = 'r'
    print('ROCK')
elif randomNumber == 2:
    computerMove = 'p'
    print('PAPER')
elif randomNumber == 3:
    computerMove = 's'
    print('SCISSORS')

# Display and record the win/loss/ties
if playerMove == computerMove:
    ties = ties + 1
    print('Tie!')
elif playerMove == 'r' and computerMove == 's':
    wins = wins + 1
    print('You won!')
elif playerMove == 'r' and computerMove == 'p':
    losses = losses + 1
    print('Computer wins!')
elif playerMove == 's' and computerMove == 'r':
    losses = losses + 1
    print('Computer wins!')
elif playerMove == 's' and computerMove == 'p':
    wins = wins + 1
    print('You win!')
elif playerMove == 'p' and computerMove == 'r':
    wins = wins + 1
    print('You win!')
elif playerMove == 'p' and computerMove == 's':
    losses = losses + 1
    print('Computer wins!')
