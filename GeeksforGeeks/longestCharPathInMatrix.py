# adjacency list representation since graph
# probably isn't very dense

# AL is dictionary where key is vertex (coord)
# and value is a list of tuples -> (v, u)
# which represent undirected edges

# vertices are named by their x,y coordinate

# separate store vertices in a dictionary
# where key is vertex coord
class Graph:
    def __init__(self):
        self.AL = {}
        self.vertices = {}
    def addVertex(self, v):
        if v not in self.AL:
            self.AL[v.coord] = []
            self.vertices[v.coord] = v
    #update the adjacency list for a vertex
    def updateAL(self):
        for c in self.vertices:
            v = self.vertices[c]
            for x in range(v.coord[0]-1, v.coord[0]+2):
                for y in range(v.coord[1]-1,v.coord[1]+2):
                    coord = (x,y)
                    if coord not in self.AL:
                        continue
                    if charInc(self.vertices[coord].value, v.value):
                        self.AL[v.coord].append(coord)

class Vertex:
    def __init__(self, value, x, y):
        self.value = value
        self.coord = (x,y)

#http://www.geeksforgeeks.org/find-length-of-the-longest-consecutive-path-in-a-character-matrix/
# assume multiple targets in matrix possible
# single source shortest paths; run on multiple sources
# utilize dp since we might be solving the same subproblem
# when running DFS on multiple sources
def longestCharPathInMatrix(matrix, target):
    g = Graph()
    dp = []
    dpInit(dp, len(matrix), len(matrix[0]))
    print dp

    #set up graph
    for x,row in enumerate(matrix):
        for y,element in enumerate(row):
            v = Vertex(element, x, y)
            g.addVertex(v)
    g.updateAL()

    best = 0
    for coord in g.vertices:
        v = g.vertices[coord]
        if v.value != target:
            continue
        temp = 0
        if dp[coord[0]][coord[1]] != 0:
            temp = dp[coord[0]][coord[1]]
        else:
            temp = DFS(target, coord, g)
            dp[coord[0]][coord[1]] = temp
        if temp > best:
            best = temp
    print best
    print dp
    # for i in g.AL:
    #     print i, g.AL[i]
    # for v in g.vertices:
    #     print v, g.vertices[v].value

def dpInit(dp, row, col):
    for i in range(row):
        dp.append([0 for i in range(col)])

# not really DFS... more like hybrid DFS/BFS since we don't use a
# queue, but that could be easily implemented
def DFS(start, coord, g):
    print coord
    stack = [(coord,1)]
    best = 1
    while len(stack) != 0:
        curr, depth = stack.pop()
        for x in range(curr[0]-1, curr[0]+2):
            for y in range(curr[1]-1, curr[1]+2):
                if (x,y) not in g.vertices:
                    continue
                if charInc(g.vertices[(x,y)].value, g.vertices[curr].value):
                    stack.append(((x,y),depth + 1))
                    if depth + 1 > best:
                        best = depth + 1
                    print x,y
    return best

def DFS_recurse(start, prev, g):
    pass

# a should be the target character (the bigger one)
def charInc(a,b):
    return ord(a) == ord(b)+1

if __name__ == '__main__':
    matrix = [["e", "c", "d"],["h", "b", "e"],["i", "g", "f"]]
    target = "e"
    longestCharPathInMatrix(matrix, target)
