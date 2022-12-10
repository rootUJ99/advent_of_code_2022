import os

file = os.path.dirname(__file__)
input = os.path.join(file, 'input.txt')

# import sys

# sys.path.append(os.path.join(os.getcwd(), ""))

# print(sys.path)
# import utils

# data = utils.get_splitted_input('input.txt')
# print(data)

def convert(n_rnage):
    return [int(i) for i in n_rnage.split('-')]

def num_in_range(start, end, num):
    return num >= start and num <= end
    

with open(input, 'r') as f:
    data = f.read()
    splitted_data = [i.split(',') for i in data.split('\n')]

    count = 0
    for (first, second) in splitted_data:
        f_start, f_end = convert(first) 
        s_start, s_end = convert(second) 
        # print(f_start, f_end, s_start, s_end)
        if (f_start <= s_start and s_end <= f_end) or (s_start <= f_start and f_end <= s_end) :
            count+=1

    print(count)

    count1 = 0
    for (first, second) in splitted_data:
        f_start, f_end = convert(first) 
        s_start, s_end = convert(second) 
        # print(f_start, f_end, s_start, s_end)
        if num_in_range(f_start, f_end, s_start) or num_in_range(f_start, f_end, s_end) or num_in_range(s_start, s_end, f_start) or num_in_range(s_start, s_end, f_end):
            count1+=1

    print(count1)
