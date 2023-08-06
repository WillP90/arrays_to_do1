import random

# create shuffle(arr), to efficiently shuffle a given array’s values. Work in-place, naturally. Do you need to return anything from your function?
def shuffle(list1):
    # setting the random index to have a starting point of 0, and an end the size of the list -1 to account for the index
    random_index = random.randint(0, len(list1)-1)
    # for loop to iterate through the list
    for i in range(len(list1)):
        # setting a temp variable as whatever the index number is depending on the itteration
        temp = list1[i]
        # setting the lists index to a random index number while temp holds the variable
        list1[i] = list1[random_index]
        # a new random index is set to the temp variable from the loops original index variable
        list1[random_index] = temp
    # return the list to print
    return list1

print(shuffle([1,2,3,4,5]))


# You are situated at street level. Return array containing heights of buildings you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always with challenges, do not use built-in array functions such as unshift().
def burbank(list1):
    # setting a variable to catch the tallest building so far in the array
    max_building = 0
    # creating an empty list to append to
    list2 = []
    # for loop to iterate through the list
    for i in range(len(list1)):
        # if statement to catch if it the tallest building in sight at the moment
        if list1[i] > max_building:
            # if it is, appends to the new list
            list2.append(list1[i])
            # then replaces the tallest building in sight for the next loop iteration
            max_building = list1[i]
    # returning the new list with visible buildings
    return list2

print(burbank([-1,1,1,7,3]))
print(burbank([0,4]))


# Create a standalone function that accepts two arrays and combines their values sequentially into a new array. Extra values from either array should be included afterward. Given [4,15,100] and [10,20,30,40], return new array containing [4,10,15,20,30,40,100].
def zipit(list1,list2):
    # declaring empty list to append to
    list3 = []
    # for loops for appending both lists to the third to sort.
    for i in range(len(list1)):
        list3.append(list1[i])
    for j in range(len(list2)):
        list3.append(list2[j])
    # for loop to iterate through the list once
    for k in range(len(list3)):
        # iterates through the list again while checking the values against original index number
        for l in range(len(list3)):
            # if the index of the original is lower then the new index, the indexes are switched
            if list3[k] < list3[l]:
                list3[k], list3[l] = list3[l], list3[k]
    # return statement to return new list
    return list3

print(zipit([4,15,100],[10,20,30,40]))