'''
sort a list of numbers with quick sort
'''


numbers = [3, 7, 8, 1, 5, 9, 6, 10, 2, 4]


def quick_sort(number_list):

    if len(number_list) <= 1:#when it has ethier no or only a value return!
        return number_list

    pivot = number_list.pop()#set up the pivot value as the last one for convenience

    smaller_group = []
    greater_group = []

    for value in number_list:#values smaller than the pivot goes to first group.
        if value < pivot:
            smaller_group.append(value)
        else:
            greater_group.append(value)

    return quick_sort(smaller_group) + [pivot] + quick_sort(greater_group)#recursion to sort rest of unsorted groups


print(quick_sort(numbers))
