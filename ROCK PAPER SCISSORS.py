import random
def calculate_score(val_1,val_2,score):
	if(val_1-1==val_2):
			score=score+1
	elif(val_1+2==val_2):
		score=score+1
	return score
def user_input():
	choices=[1,2,3]
	print('''Type 
	1 for Rock
	2 for paper
	3 for sicissor
	''')
	while True:
		user=int(input('Enter your choice: '))
		if(user not in choices):
			print('Wrong input...Enter again')
		else:
			break
	return user
def computer():
	print('Max Score is 5 and You have only 5 turns...So move on....!')
	print('\n')
	print('YOU VS COMPUTER')
	options=['Rock','Paper','Sicissors']
	score=0
	turns=1
	while turns<=5:
		choices=[1,2,3]
		computer=random.choice(choices)
		user=user_input()
		print(f'Computer choice: {options[computer-1]}   Your Choice:{options[user-1]}')
		print('\n')
		print(f'Chances left:{5-turns} ')
		print('\n')
		score=calculate_score(user,computer,score)
		print('Score: ',score)
		turns=turns+1
	print('Turns Over')
	print('\n')
	print('Total Score is',score)

def multiplayer():
	print('Max score is 5.....Those who gets it first will be the winner....!')
	print('\n')
	print('MULTIPLAYER')
	options=['Rock','Paper','Sicissors']
	player_1_score=0
	player_2_score=0
	while True:
				print('\n')
				print('PLAYER 1')
				player_1=user_input()
				print(f'Player 1:{options[player_1-1]}')
				print('\n')
				print('PLAYER 2')
				player_2=user_input()
				print('\n')
				print(f'Player 2:{options[player_2-1]}')
				player_1_score=calculate_score(player_1,player_2,player_1_score)
				player_2_score=calculate_score(player_2,player_1,player_2_score)
				if(player_1_score==5):
					print('PLAYER 1 WON')
					break
				elif(player_2_score==5):
					print('PLAYER 2 WON')
					break
				print(f'PLAYER 1 SCORE:{player_1_score}  PLAYER 2 SCORE:{player_2_score}')
								
def main():
    while True:
        print('\n')
        print('Welcome to Rock Paper Scissors Gam....')
        mode_of_play = int(input('''How do you want to play...? Type
    1 to play with computer
    2 to play as Multiplayer
    3 to exit   '''))
        if mode_of_play == 1:
            computer()
        elif mode_of_play == 2:
            multiplayer()
        else:
            print('Thank You')
            break
main()