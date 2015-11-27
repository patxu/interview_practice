def reverseAlpha(string):
	string = list(string)
	left = 0
	right = len(string)-1
	while left < right:
		if not string[left].isalpha():
			left += 1
		elif not string[right].isalpha():
			right += -1
		else:
			temp = string[left]
			string[left] = string[right]
			string[right] = temp
			left += 1
			right += -1
	return "".join(string)

print reverseAlpha("a!!!b.c.d,e\'f,ghi")
