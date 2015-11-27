# import ipdb; ipdb.set_trace()


def gen(n, depth = 0, prefix = []):
    if n > 9 or n < 1:
        return
    if len(prefix) == 0:
        prefix = [None for i in range(n)]
    if depth == n:
        print "".join(str(i) for i in prefix if i != None)
    else:
        start = None
        if prefix[0] == None:
            start = 1
        else:
            start = prefix[depth-1] + 1
        for i in range(start, 10):
            prefix[depth] = i
            gen(n, depth + 1, prefix)

gen(5)
