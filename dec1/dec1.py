import os
curr_path = os.path.dirname(__file__)
input_file = os.path.join(curr_path, 'input.txt')


with open(input_file, 'r') as f:
    data =  f.read()
    splitdata = data.split("\n")
    maxArr = []
    count = 0
    sum = 0
    for i in splitdata:
        if i != "":
            sum += int(i)
        else:
            maxArr.insert(count, sum)
            sum = 0 
            count += 1

    print(maxArr[0])
    arr = maxArr.sort(reverse=True)
    sum = 0
    for i in maxArr[:3]:
        sum+=i

    print(sum)
