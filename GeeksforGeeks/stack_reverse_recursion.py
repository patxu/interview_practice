stack = []
def reverse(item):
    global stack
    if len(stack) == 0:
        stack.append(item)
    else:
        temp = stack.pop(0)
        reverse(item)
        stack.append(temp)

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print stack
item = stack.pop()
reverse(item)
print stack
'''
reverse(4)
    temp = 3
    reverse(4)
        temp = 2
        reverse(4)
            temp = 1
            reverse(4)
                stack.append(4)
'''
