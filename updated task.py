import random
finish = False
print('Hello, player! Select a game mode:')
print('1 - two players')
print('2 - an easy game with a computer')
print('3 - a complicated game with a computer')
version = int(input('So, what is your choice?\n'))
players=[]
if version == 1:
    name1 = input('Input the name of the first player:\n')
    name2 = input('Input the name of the second player:\n')
    players.append(name1)
    players.append(name2)
else:    
    name = input('Input your name:\n')
    players.append(name)
    players.append('Computer')
hp=[50, 50]
f=[ 
    [0,0,0],
    [1,1,1,1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2,2,2,0],
    [3,3,3,3,3,3,3,3,0,0],
    [4,4,4,4,4,4,4,0,0,0],
    [5,5,5,5,5,5,0,0,0,0],
    [6,6,6,6,6,0,0,0,0,0],
    [7,7,7,7,0,0,0,0,0,0],
    [8,8,8,0,0,0,0,0,0,0],
    [9,9,0,0,0,0,0,0,0,0]
]
def process(turn):
    playing = True
    while playing:
        if turn % 2 == 0:
            enemyturn = 1
        else:
            enemyturn = 2
        if (version == 1) or (version == 2 and turn == 1) or (version == 3 and turn == 1):
            phrase = str(players[turn - 1]) + ', choose the force to attack! It may be an integer from 1 to 9.\n'
            pickforce = int(input(phrase))
            push = random.choice(f[pickforce])
            if push!=0:
                hp[enemyturn - 1] -= push
                print(str(players[turn - 1])+' is attacking the enemy with a power of '+str(push)+'. An enemy has '+ str(hp[enemyturn - 1]) + ' hp left.')
                if turn % 2 == 0:
                    turn -= 1
                else:
                    turn += 1
            else:
                print('Attack was not succeeded!')
                if turn % 2 == 0:
                    turn -= 1
                else:
                    turn += 1
        elif (version == 2 and turn == 2):
            x = [int(i) for i in range (len(f))]
            push = random.choice(f[random.choice(x)])
            if push !=0:
                hp[enemyturn - 1] -= push
                print('The computer attacks you with a power of '+ str(push) + ' . You have '+str(hp[enemyturn-1])+' hp left.')
                if turn % 2 == 0:
                    turn -= 1
                else:
                    turn += 1
            else:
                print('Attack was not succeeded!')
                if turn % 2 == 0:
                    turn -= 1
                else:
                    turn += 1
        elif (version == 3 and turn == 2):
            if hp[turn - 1]-hp[turn - 2]>=20 or hp[turn - 1]>=25:
                e = random.choice([int(i) for i in range(4,8)])
                push = random.choice(f[e]) 
            elif hp[turn-1]<25 and hp[turn-1]>=10:
                e = random.choice([int(i) for i in range(8,10)])
                push = random.choice(f[e])
            elif hp[turn-1]<10:
                e = random.choice([int(i) for i in range(1,4)])
                push = random.choice(f[e])
            if push !=0:
                    hp[enemyturn - 1] -= push
                    print('The computer attacks you with a power of '+ str(push)+' . You have '+str(hp[enemyturn-1])+' hp left.')
                    if turn % 2 == 0:
                        turn -= 1
                    else:
                        turn += 1
            else:
                print('Attack was not succeeded!')
                if turn % 2 == 0:
                    turn -= 1
                else:
                    turn += 1    
        if hp[turn - 1]<= 0:
            print('What a game! '+ str(players[enemyturn - 1])+ ' wins!')
            playing = False
        elif hp[enemyturn - 1] <= 0:
            print('What a game! '+ str(players[turn - 1])+ ' wins!')
            playing = False
process(1)



