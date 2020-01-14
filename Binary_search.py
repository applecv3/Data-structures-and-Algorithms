'''
binary serach with recursion.
find a value's idx in a sorted list of numbers.
if the value u want to find doesn't exist, return -1
'''


numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81]


def binary_search(number_list, value_to_search, start):#list, the value to search, starting idx

    if len(number_list) == 1:

        if number_list[0] == value_to_search:# end recursion when the list has only one value!
            return start
        else:
            return -1

    if len(number_list) % 2 == 0:
        center = len(number_list) // 2 - 1
    else:
        center = len(number_list) // 2

    if value_to_search > number_list[center]:# use start+center+1 to remember starting point!
        return binary_search(number_list[center + 1:], value_to_search, start + center + 1)
    else:
        return binary_search(number_list[:center], value_to_search, start)


print(binary_search(numbers, 36, 0))
print(binary_search(numbers, 32, 0))
print(binary_search(numbers, 16, 0))
