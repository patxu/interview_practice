def permutations(prefix, string):
    n = len(string)
    if n == 0:
        print prefix
    for i in range(n):
        permutations(prefix + string[i], string[:i] + string[i+1:])

permutations("", "abc")
