def stairs():
    n = int(raw_input())
    for i in range(n):
        line = ""
        for j in range(n):
            if (i + j) >= n-1:
                line += "#"
            else:
                line += " "
        print line

if __name__ == '__main__':
    stairs()
