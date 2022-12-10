import os

curr_path = os.path.dirname(__file__)
input_file = os.path.join(curr_path, 'input.txt')

def give_score(letter):
    return ord(letter) - 96 if ord(letter) - 96 > 0 else (ord(letter) - 64) + 26 

with open(input_file, 'r') as f:
    splitted_racks = f.read().split('\n')
    arr = [(i[:len(i)//2], i[len(i)//2:]) for i in splitted_racks]
    
    score = 0

    for (first, second) in arr:
        # print(first, second)
        set_first = set(first)
        set_second = set(second)
        intersection = [*set_first.intersection(set_second)]
        score+=give_score(intersection[0])
    
    print(score)

    arr = []
    D = 3
    score2 = 0
    for indx, i in enumerate(splitted_racks):
        if (indx+1) % D == 0:
            arr.append(set(i))
            comm = arr[0].intersection(arr[1]).intersection(arr[2])
            score2+=give_score([*comm][0])
            arr = []
        else:
            arr.append(set(i))

    print(score2)

        