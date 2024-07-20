'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

l1 = [1,2,3]
l2 = [4,5,6]
# output = [5,7,9]
# Initial Thoughts: output values are sum of input values unless the values equate to more than 9

def add_two_nums(l1,l2):
    output = []
    l1flip = []
    l2flip = []
    for num in l1:
        l1flip = [num] + l1flip
    for num in l2:
        l2flip = [num] + l2flip
    for i in range(len(l1)):
        output.append(l1[i] + l2[i])
    return output


print(add_two_nums(l1,l2))