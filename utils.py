def get_splitted_input(input):
    from os import path

    dir = path.dirname(__file__)
    file = path.join(dir, input)

    with open(file, 'r') as f:
        return [i.split('\n') for i in f.read()]
    
# data = get_splitted_input('input2.txt')
# print(data)