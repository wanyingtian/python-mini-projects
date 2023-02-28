## Lists

def every_three_nums(start):
    '''
    Create a function called every_three_nums that has one parameter named start.

    The function should return a list of every third number between start and 100 (inclusive). 
    For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.
    '''
    if start > 100:
        return []
    return list(range(start, 101, 3))

print(every_three_nums(91))


def remove_middle(my_list, start, end):
    '''
    Create a function named remove_middle which has three parameters named my_list, start, and end.

    The function should return a list where all elements in my_list with an index between start and end (inclusive) have been removed.

    For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

    remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)
    '''
    return my_list[:start] + my_list[end+1:]

def double_index(my_list, index):
    '''
    Create a function named double_index that has two parameters: a list named my_list and a single number named index.
    The function should return a new list where all elements are the same as in my_list except for the element at index. The element at index should be double the value of the element at index of the original my_list.
    If index is not a valid index, the function should return the original list.

    '''
    # Checks to see if index is too big
    if index >= len(my_list):
        return my_list
    else:
        # Gets the original list up to index
        my_new_list = my_list[0:index]
    # Adds double the value at index to the new list 
    my_new_list.append(my_list[index]*2)
    #  Adds the rest of the original list
    my_new_list = my_new_list + my_list[index+1:]
    return my_new_list
    '''
    Note that this solution is careful not to modify the original input list. 
    If we were to simply use my_list[index] = my_list[index] * 2 
    then the list that was passed into the function would be modified outside of the function as well. 
    Creating a new list and writing the values to it prevents this from happening. 
    We use slicing to extract the values before and after the index and we append the modified value at the index to our new list.
    '''