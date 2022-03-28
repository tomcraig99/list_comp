original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
original_scores.sort(key=lambda x: x[1])
print(original_scores)

'''def sort(list):
    count = len(list)
    new = []
    while count != 0:
        tempOne = list[count][1]
        tempTwo = list[count-1][1]
        if tempOne>tempTwo:
            new.append(tempOne)
            new.append(tempTwo)'''