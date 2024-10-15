import random
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
player_move = ''
computer_move = ''
winner = ''

while True:
    player_move = input('Choose [r]ock, [p]aper or [s]cissor: ' )

    if player_move.strip().lower() == 'r':
        player_move = rock
    elif player_move.strip().lower() == 'p':
        player_move = paper
    elif player_move.strip().lower() == 's':
        player_move = scissors
    else:
        print('Invalid Input. try again..')
        continue
    break

computer_random_number = random.randint(1,3)

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissors

if player_move == rock and computer_move == scissors \
        or player_move == scissors and computer_move == paper \
        or player_move == paper and computer_move == rock:
    winner = 'Player'
elif player_move == rock and computer_move == rock \
        or player_move == scissors and computer_move == scissors \
        or player_move == paper and computer_move == paper:
    winner = 'Draw'
else:
    winner = 'Computer'

print(f'\033[1;32;40mPlayer chose: {player_move}\n\033[1;34;40mComputer chose: {computer_move}')
print()

if winner != 'Draw':
    print(f'{winner} wins!')
else:
    print(f'{winner} !!!')