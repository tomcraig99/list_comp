import numbers


remainder = lambda num: num % 2

print(remainder(5))

product = lambda x, y: x * y

print(product(2, 3))


def testfunc(num):
    print(num)
    return lambda x: x * num


result10 = testfunc(10)
result100 = testfunc(100)

print(result10(5))
print(result100(5))

result10 = lambda x: x * 10
result100 = lambda x: x * 100

print(result10(5))
print(result100(5))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


numberedList = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]

filteredList = list(filter(lambda num: (num > 7), numberedList))

print(filteredList)


def addition(n):
    return n + n


numbers = [1, 2, 3, 4]
result = map(addition, numbers)

print(list(result))

result = list(map(lambda n: n+n, numbers))

print(result)



import os
clear = lambda: os.system('cls')

clear()