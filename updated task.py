import random
def person_is_playing(version, turn):
    return (version == 1) or (version == 2 and turn == 1) or (version == 3 and turn == 1 )

def computer_is_playing_easily(version, turn):
    return (version == 2 and turn == 2)

def computer_is_playing_hardly(version, turn):
    return (version == 3 and turn == 2)

def computers_strategical_push(turn):
    push = 0
    if hp[turn - 2] > 10:
        e = random.choice([int(i) for i in range(4,7)])
    if hp[turn - 2] <= 10:
        e = random.choice([int(i) for i in range(2,6)])
    push = random.choice(push_probability_list_generator(e)) 
    return push

def push_probability_list_generator(pickforce):
    probability = (100 - (pickforce * 10 - 10))//10
    f = [pickforce]*probability + [0]*(10 - probability)
    return f   

def pickforce(players,turn):
    phrase = str(players[turn-1]) + ', choose the force to attack! It may be an integer from 1 to 9.\n'
    try:
        pickforce = int(input(phrase))
    except ValueError:
        pickforce = int(input('This value should be an integer! Try again.\n'))
    push = random.choice(push_probability_list_generator(pickforce))
    return push

def success_of_computers_attack(push, enemyturn, hp):
    if push !=0:
        hp[enemyturn - 1] -= push
        print('The computer attacks you with a power of '+ str(push) + ' . You have ' + str(hp[enemyturn-1]) + ' hp left.')
    else:
        print('Attack was not succeeded!')

def human_steps(version, players, turn, enemyturn):
    push = pickforce(players,turn)
    if push!=0:
        hp[enemyturn-1] -= push
        print(str(players[turn-1])+' is attacking the enemy with a power of '+str(push)+'. An enemy has '+ str(hp[enemyturn-1]) + ' hp left.')
    else:
        print('Attack was not succeeded!')  
            
def dummy_comp_steps(hp, enemyturn):
    x = random.choice([int(i) for i in range (1,10)])
    push = random.choice(push_probability_list_generator(x))
    success_of_computers_attack(push, enemyturn, hp)

def intelligent_comp_steps(push, hp, enemyturn):
    success_of_computers_attack(push, enemyturn, hp)

def process(turn):
    playing = True
    while playing:
        if turn%2==0:
            enemyturn = 1
        else:
            enemyturn = 2
        if person_is_playing(version, turn):
            human_steps(version, players, turn, enemyturn)

        elif computer_is_playing_easily(version, turn):
            dummy_comp_steps(hp, enemyturn)

        elif computer_is_playing_hardly(version, turn):
            push = computers_strategical_push(2)
            intelligent_comp_steps(push, hp, enemyturn)
        turn = enemyturn   
        if hp[turn-1]<= 0:
            print('What a game! '+ str(players[enemyturn-1])+ ' loses!')
            playing = False
        elif hp[enemyturn-1] <= 0:
            print('What a game! '+ str(players[turn-1])+ ' loses!')
            playing = False
print('Hello, player! Select a game mode:')
print('1 - two players')
print('2 - an easy game with a computer')
print('3 - a complicated game with a computer')
version = int(input('So, what is your choice?\n'))
players=[]
if version == 1: 
    players.append(input('Input the name of the first player:\n'))
    players.append(input('Input the name of the second player:\n'))
else:    
    players.append(input('Input your name:\n'))
    players.append('Computer')
hp=[50, 50]
process(1)
