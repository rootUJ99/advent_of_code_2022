from os import path

curr_dir = path.dirname(__file__)
input = path.join(curr_dir, 'input.txt')

with open(input, 'r') as f:
    string = f.read()
    
    start_at = None
    for indx, i in enumerate(string):
        # till_char = 4
        till_char = 14
        chunk = string[indx:indx+till_char]
        if len(set(chunk)) == till_char:
            start_at = indx+till_char
            break
    
    print(start_at)

