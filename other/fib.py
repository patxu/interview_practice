import time
i = 400

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

start = time.clock()
# print fib(i)
first = time.clock()-start

def fib_memo(n, memo={0:0, 1:1}):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

start = time.clock()
print fib_memo(i)
second = time.clock()-start

print first - second
