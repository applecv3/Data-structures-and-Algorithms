'''
sorting a list with Bubble sort!
'''


numbers = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]


for i in range(len(numbers)):

    for j in range(len(numbers) - i - 1):

        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]#send the smaller one to the left!


print(numbers)
