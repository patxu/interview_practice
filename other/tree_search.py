#10.22.15
#implement a tree search

class node():
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right

def tree_search(node, value):
	if node == None:
		return None
	if value < node.value:
		return tree_search(node.left, value)
	elif value > node.value:
		return tree_search(node.right, value)
	else:
		return node

if __name__ == '__main__':
	root = node(10)
	root.left = node(4)
	root.right = node(12)
	root.left.right = node(8)
	root.right.right = node(16)
	root.right.left = node(11)

	print tree_search(root, 13).value
