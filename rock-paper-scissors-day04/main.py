import random

scissors = '''
.-.  _
| | / )
| |/ /
_|__ /_
/ __)-' )
\  `(.-')
> ._>-'
/ \/
'''

paper = '''
                   _
               _  / |
              / \ | | /\
               \ \| |/ /
                \ Y | /___
              .-.) '. `__/
             (.-.   / /
                 | ' |
                 |___|
                [_____]
'''

rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
'''

machine_hand = ['rock', 'paper', 'scissors']
hand_symbol = [rock, paper, scissors]
bot_win = 0
player_win = 0
for match in range(0,3):
    player_choice = input('Please choose your hand (rock, paper, scissors): ')
    machine_choice = random.randint(0,2)
    print(f'Computer choose: \n {hand_symbol[machine_choice]}')
    if machine_hand[machine_choice] == player_choice:
        print(f'You choose: \n {hand_symbol[machine_choice]}')
        print('tie')
    else:
        if machine_hand[machine_choice] == 'scissors' and player_choice == 'paper':
            print(f'You choose: \n {hand_symbol[1]}')
            print('Machine win')
            bot_win += 1
        elif machine_hand[machine_choice] == 'paper' and player_choice == 'rock':
            print(f'You choose: \n {hand_symbol[0]}')
            print("Machine win")
            bot_win += 1
        elif machine_hand[machine_choice] == 'rock' and player_choice == 'scissors':
            print(f'You choose: \n {hand_symbol[2]}')
            print("Machine win")
            bot_win += 1
        else:
            if machine_choice == len(machine_hand) - 1:
                machine_choice = -1
            print(f'You choose: \n {hand_symbol[machine_choice + 1]}')
            print('player win')
            player_win += 1

if bot_win < player_win:
    print("You have won the round")
elif player_win < bot_win:
    print("You lose please try again")
else:
    print("It's a draw")

