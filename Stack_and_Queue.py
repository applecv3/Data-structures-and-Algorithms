'''
palindrome with stack and queue
if the target sentence appears to be a palindrome it returns True otherwise False
'''


def palindrome(sentence):#function to solve palindrome task

    chracters = []

    for char in sentence:

        if char.isalpha():#fill up the list with a value if it is an alphabet
            chracters.append(char)

    while True:
        #compare the values from dequeue and pop
        if chracters.pop(0).lower() != chracters.pop().lower():
            return False
        if len(chracters) <= 1:
            break

    return True


print(palindrome('ajwo  93 dd'))
print(palindrome('wow'))
print(palindrome('Wow'))
