# import ipdb; ipdb.set_trace()

class node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# do a post order traversal
# start a counter at 1
# if root is null, return counter - 1
# each time we recurse on a child we increase a counter by 1
# return max value returned by left and rigth children

def maxDepth(root, counter = 1):
    if root == None:
        return counter - 1
    return max(maxDepth(root.left, counter + 1), maxDepth(root.right, counter + 1))

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.right = node(5)
root.right.right = node(7)

print maxDepth(root)

# maxDepth(1, 1)
#     maxDepth(2,2)
#         maxDepth(None,3)
#             return 2
#         maxDepth(5,3)
#             maxDepth(None,4)
#                 return 3
#             maxDepth(None,4)
#                 return 3
#             return 3
#         return 3
#     maxDepth(3,2)
#         maxDepth(None,3)
#             return 2
#         maxDepth(7, 3)
#             maxDepth(None,4)
#                 return 3
#             maxDepth(None,4)
#                 return 3
#         return 3
#     return 3
