x = [p for p in range(10)]
print(x)


#adding an expression - square of each number
squares = [i**2 for i in range(10)]
print(squares)


#multiply each element by 3
list1 = [3,4,5]
multiply = [item*3 for item in list1]
print(multiply)


#word manip
listOfWords = ["this","is","a","list","of","words"]
manip = [word[0] for word in listOfWords]
print(manip)


#lowercase(or upper)
list2 = ['A','B','C']
lower = [w.lower() for w in list2]
print(lower)


#if condition
new_range = [i*i for i in range(5) if i%2==0]
print(new_range)


#character type filter
string = "Hello 12345 World"
new_list = [char for char in string if char.isdigit()]
print(new_list)
newNew_list = [char for char in string if char.isalpha()]
print(newNew_list)


#file stuff
myfile = open("test.txt", 'r')
result = [i.rstrip("\n") for i in myfile if "line3" in i]
print(result)


#using functions
def double(x):
    return x*2

mynums = [double(x) for x in range(10) if x%2==0]
print(mynums)


#add multiple arguments
result = [x+y for x in [10,20,30] for y in [20,40,60]]
print(result)