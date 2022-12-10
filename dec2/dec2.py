import os

curr_path = os.path.dirname(__file__)
input_file = os.path.join(curr_path, 'input.txt')


with open(input_file) as f:
    splittedData = [i.split(' ') for i in f.read().split('\n')]

    points = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    winmapping = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }

    drawmapping = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }

    lossmapping = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }

    score = 0

    for (opp, me) in splittedData:
        if winmapping[opp] == me:
            winscore = points[me] + 6
            score+=winscore
        elif drawmapping[opp] == me:
            drawscore = points[me] + 3
            score+=drawscore
        else:
            lossscore = points[me] 
            score+=lossscore

    print(score)

    score2 = 0

    decisionmapping = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }

    for (opp, me) in splittedData:
        if me == 'X':
            lossscore = decisionmapping[me] + points[lossmapping[opp]]
            score2+=lossscore
        elif me == 'Y':
            drawscore = decisionmapping[me] + points[drawmapping[opp]]
            score2+=drawscore
        else:
            winscore = decisionmapping[me] + points[winmapping[opp]]
            score2+=winscore
        
    print(score2)