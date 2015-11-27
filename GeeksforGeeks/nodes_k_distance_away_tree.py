class node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

# let x be a node we output
# 3 cases
# case 1: x is in the subtree rooted at target
#   traverse the tree rooted at target and track depth
#   if depth == k
#     print root
# case 2/3: 2) x is an ancestor of target or
#           3) x is a child of an ancestor of target
#   keep track of distance- distance from target
#   postorder traversal of the tree and search for target
#   if root is None
#     return inf
#   if root is target
#     return distance + 1
#   distance = min(recurse left, recurse right)
#   if distance < k: case 3
#     do case 1 with depth = distance
#   if distance == k: case 2
#     print root
#   return distance
#

def kDistAway(root, target, k):
    one(target, target, k)
    two(root, target, k)

def one(root, target, k, depth = 0, visited = {}):
    if root == None or root.value in visited:
        return
    if root.value == target.value and depth != 0:
        return
    if k == depth:
        print root.value
        return
    if depth > k:
        return
    one(root.left, target, k, depth + 1, visited)
    one(root.right, target, k, depth + 1, visited)

def two(root, target, k, distance = 0, visited = {}):
    if root == None:
        return float("inf")
    if root.value == target.value:
        return distance + 1
    distance = min(two(root.left,target, k, distance, visited), two(root.right, target, k, distance, visited))
    if distance < k:
        one(root, target, k, distance, visited)
    if distance == k:
        print root.value
    if distance != float("inf"):
        visited[root.value] = True
    return distance + 1
#
# two(20, 8, 2, 0)
#     two(8, 8, 2, 0)
#         return 1
#     two(22, 8, 2, 0)
#         two(None, 8, 2, 0)
#             return inf
#         two(None, 8, 2, 0)
#             return inf
#         return inf
#     distance = 1
#     one(20, 8, 2, 1)
#         one(8, 8, 2, 2)
#             return
#         one(22, 8, 2, 2)
#             print 22

root = node(20)
root.left = node(8)
root.right = node(22)
root.left.left = node(4)
root.left.right = node(12)
root.left.right.left = node(10)
root.left.right.right = node(14)

kDistAway(root, root.left, 2)
kDistAway(root, root.left.right.right, 3)
