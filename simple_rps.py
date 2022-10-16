# %%
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
if list_1 == list_2:
    print('The lists are the same.')
else:
    print('The lists are different.')
# %%
import random

player_1 = ['rock', 'paper', 'scissors']
player_2 = ['rock', 'paper', 'scissors']

if player_1 == player_2:
    print('equality verification check completed')

player_1_turn = random.choice(player_1)
player_2_turn = random.choice(player_2)

print(player_1_turn)
print(player_2_turn)

if player_1_turn == player_2_turn:
    print('its a tie')
elif player_1_turn == 'rock' and player_2_turn == 'scissors':
    print(f'player_1 wins with {player_1_turn}')
elif player_1_turn == 'rock' and player_2_turn == 'paper':
    print(f'player 2 wins with {player_2_turn}')
elif player_1_turn == 'paper' and player_2_turn == 'rock':
    print(f'player 1 with with {player_1_turn}')
elif player_1_turn == 'paper' and player_2_turn == 'scissors':
    print(f'player 2 with with {player_2_turn}')
elif player_1_turn == 'scissors' and player_2_turn == 'rock':
    print(f'Player 2 with wins {player_2_turn}')
elif player_1_turn == 'scissors' and player_2_turn == 'paper':
    print(f'Player 1 with {player_1_turn}')
# %%
