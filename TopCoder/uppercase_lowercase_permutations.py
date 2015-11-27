import sys
import itertools

def getPermutations(string, step = 0):
  if step == len(string):
    print "".join(string)
  for i in range(step, len(string)):
    string_copy = [char for char in string]
    string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
    getPermutations(string_copy, step+1)

if __name__ == "__main__":
  getPermutations(sys.argv[1])
