# coding : UTF-8
array = [3.14, 1592, 6535, 8979, 'あり']
print(len(array), array)
array.append('をり')
print(len(array), array)
array.extend(['はべり', 'いまそかり'])
print(len(array), array)
del array[7]
print(len(array), array)
array.pop(6)
print(len(array), array)
array.remove('をり')
print(len(array), array)
