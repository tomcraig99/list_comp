'''string = 'Hello12123'


requirements = ['lower','upper','digit','length']

testing = [True for x in requirements if (any(x.islower()) and any(x.isupper()) and any(x.isdigit()) for x in string)]


def test(string):
    test=[]
    if any(x.islower() for x in string):
        test.append(True)
    else:
        test.append(False)
    if any(x.isupper() for x in string):
        test.append(True)
    else:
        test.append(False)
    if any(x.isupper() for x in string):
        test.append(True)
    else:
        test.append(False)
    if len(string)>=8:
        test.append(True)
    else:
        test.append(False)

    return all(test)

print(test(string))
'''


password = '19aaaaAa'
method = lambda x: (any(b.islower() for b in password) and any(b.isupper() for b in password) and any(b.isdigit() for b in password)) and len(password)>=8
print(method(password))
