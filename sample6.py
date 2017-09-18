# coding : UTF-8
a = 3
b = 6
c = 2
array = [ 1, 3, 4 ]

if a * c == 6 and b % c == 0:
    print(a, "*", c, "is 6, and", b, "%", c, "is 0")
elif a * c == 6 or b % c == 0:
    print(a, "*", c, "is 6, or", b, "%", c, "is 0")
else:
    print(a, "*", c, "is 6, nor", b, "%", c, "is 0")

if a in array:
    print(a, "in", array)
else:
    print(a, "not in", array)
