# 10.22.15
# attempt to implement midterm exam question 1

class node():
	def __init__(self, length, value, best = float("inf"), left = None, right = None):
		self.length = length
		self.value = value
		self.best = best
		self.left = left
		self.right = right

def tree_search(root, length, best):
	if root == None:
		if best == float("inf"):
			return None
		else:
			return best

	if root.length >= length:
		if root.right != None:
			best = min(best, root.right.best, root.value)
		else:
			best = min(best, root.value)

	if length > root.length:
		return tree_search(root.right, length, best)
	elif length < root.length:
		return tree_search(root.left, length, best)
	else:
		return best


if __name__ == "__main__":
	root = node(130,50,20)
	root.left = node(100,20,20)
	root.right = node(175,40,30)
	root.right.right = node(200,35,35)
	root.right.left = node(150,30,30)

	print str(tree_search(root,100,float("inf"))) + " Should be 20"
	print str(tree_search(root,120,float("inf"))) + " Should be 30"
	print str(tree_search(root,160,float("inf"))) + " Should be 35"
	print str(tree_search(root,210,float("inf"))) + " Should be None"
