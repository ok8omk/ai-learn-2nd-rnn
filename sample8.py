# coding : UTF-8
filename = "sample8-output.txt"
array = ['aaa', 'bbb', 'ccc']

with open(filename, 'w') as f:
    for string in array:
        f.write(string + '\n')

f = open(filename, 'r')
string = f.readline()
while string:
    print(string)
    string = f.readline()
f.close()
