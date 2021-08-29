def duplicate(list1):  # Defined a function to check duplicate items in list
    list2 = []  # create an empty list to append the item which comes unique

    # an empty set is created so that no item comes more than one times
    # everytime a function is called the set gets empty
    set1 = set()

    for item in list1:

        if item not in list2:  # check if the item is unique
            list2.append(item)  # if unique then add in list 2

        else:  # if already comes then add it into set e.g 2
            set1.add(item)

    list3 = list(set1)  # SET IS CONVERTED INTO LIST
    # ITEM WHICH COMES MORE THAN 1 TIME IS RETURN IN LIST3
    return list3


list1 = [1, 2, 10, 7, 2, 5, 7, 3, 2]
print(duplicate(list1))  # function is called and print

list1 = [-5, -6, 7, 10, -5, 10, -6, 7]
print(duplicate(list1))  # function is called and print
