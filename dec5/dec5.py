import os

curr_dir = os.path.dirname(__file__)
input = os.path.join(curr_dir, 'input.txt')

with open(input, 'r') as f:
    stacks, instructions = f.read().split('\n\n')

    instructions = instructions.split('\n')

    stacks = [
       ['T','R','D','H','Q','N','P','B'], 
       ['V', 'T','J','B','G','W'],
       ['Q','M','V','S','D','H','R','N'],
       ['C','M','N','Z','P'],
       ['B','Z','D'],
       ['Z','W','C','V'], 
       ['S','L','Q','V','C','N','Z','G'],
       ['V','N','D','M','J','G','L'],
       ['G','C','Z','F','M','P','T'],
    ]

    # stacks = [
    #     ['N', 'Z'],
    #     ['D','C','M'],
    #     ['P']
    # ]
    
    stacks_n = [i for i in stacks]

    print(stacks)

    splitted_inst = []
    for i in instructions:
        splitted = i.split(' ')
        splitted_inst.append((
            int(splitted[1]), 
            int(splitted[3]), 
            int(splitted[5])
        ))

    for (indx, src, dest) in splitted_inst:
        fr = src - 1
        to =  dest - 1
        selected_fr = stacks_n[fr]
        # detacted_fr = selected_fr[:indx][::-1] #for 1st problem
        detacted_fr = selected_fr[:indx]
        new_from = selected_fr[indx:]
        stacks_n[fr] = new_from
        stacks_n[to] = [*detacted_fr, *stacks_n[to]]

    last = ""
    for i in stacks_n:
        last+=i[0]

    print(last)


