#!/usr/bin/env python3
# memo = {}
n,k = list(map(int, input().split()))
array = list(map(int, input().split()))
import functools
# import random
# array = [random.randrange(math.pow(10,9)) for _ in range(n)]


# determine if subrange is non-increasing, non-decreasing, both, or neither by
# looking at the values (defined below) of [a,b-1] and [b-1,b]
# if both return 0
# if neither return None
# if non-decreasing return 1
# if non-increasing return -1

@functools.lru_cache(maxsize=None)
def subrangeMemo(a,b):
    val = None
    if b-a == 1: #if elements are adjacent there are no previous elements to consider
        if array[b] == array[a]: #both
            val = 0
        if array[b] > array[a]: #increasing
            val = 1
        if array[b] < array[a]: #decreasing
            val = -1
        return val
    else:
        val = subrangeMemo(b-1, b)

    #determine value of subrange recursively
    prev = subrangeMemo(a,b-1)

    if prev == val: #both ranges are either increasing or decreasing or both
        return prev
    if prev == 0: #prev is both so it's whatever the last two elemnts are
        return val
    if val == 0: #val is both so it's whatever the prev is
        return prev
    return None #neither

# def subrange(a,b):
#     if (a,b) in memo: #already computed
#         return memo[(a,b)]
#
#     val = None
#     if b-a == 1: #if elements are adjacent there are no previous elements to consider
#         val = value(array[a], array[b])
#         memo[(a,b)] = val #memoize
#         return val
#     else:
#         if (b-1,b) in memo:
#             val = memo[(b-1,b)]
#         else:
#             val = value(array[b-1], array[b])
#             memo[(b-1,b)] = val #memoize
#
#     #determine value of subrange recursively
#     prev = None
#     if (a,b-1) in memo:
#         prev = memo[(a,b-1)]
#     else:
#         prev = subrange(a,b-1)
#         memo[(a,b-1)] = prev
#
#     if prev == val: #both ranges are either increasing or decreasing or both
#         memo[(a,b)] = prev
#         return prev
#     if prev == 0: #prev is both so it's whatever the last two elemnts are
#         memo[(a,b)] = val
#         return val
#     if val == 0: #val is both so it's whatever the prev is
#         memo[(a,b)] = prev
#         return prev
#     return None #neither
#
# # determine if two adjacent elements are increasing, decreasing, or equal
# def value(valA, valB):
#     if valB == valA: #both
#         return 0
#     if valB > valA: #increasing
#         return 1
#     if valB < valA: #decreasing
#         return -1
# #
# def upvotes():
#     if n != len(array) or k>n:
#         print("invalid input")
#         return
#     for outer in range(n-k+1):
#         sum = 0
#         for i in range(outer,outer+k-1):
#             for j in range(i+1,outer+k):
#                 val = subrange(i,j)
#                 if val != None:
#                     sum += val
#         print(sum)

def upvotesMemo():
    if n != len(array) or k>n:
        print("invalid input")
        return
    for outer in range(n-k+1):
        sum = 0
        for i in range(outer,outer+k-1):
            for j in range(i+1,outer+k):
                val = subrangeMemo(i,j)
                if val != None:
                    sum += val
        print(sum)

# import time
# s = time.time()
# upvotes()
# reg = time.time()-s
# s = time.time()
upvotesMemo()
# print("reg " + str(reg))
# print("memo " + str(time.time() - s))
