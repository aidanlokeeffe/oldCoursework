#  File: TopoSort.py

#  Description:

#  Student Name: Alexander Barajas

#  Student UT EID: ab65299

#  Partner Name: Aidan O'Keeffe

#  Partner UT EID: alo77

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:


class Stack(object):
  # Constructor
  def __init__(self):
    self.stack = []

  # Place item to top of stack
  def push(self, item):
    self.stack.append(item)

  # Remove item from top of stack
  def pop(self):
    return self.stack.pop()

  # View item on top of stack
  def peek(self):
    return self.stack[len(self.stack) - 1]

  # Checks if stack is empty
  def isEmpty(self):
    return len(self.stack) == 0

  # Returns number of elements in stack
  def size(self):
    return (len(self.stack))

  # Returns string representation for stack
  def __str__(self):
    return str(self.stack)


class Queue(object):
  # Constructor
  def __init__(self):
    self.queue = []

  # Place item at back of queue
  def enqueue(self, item):
    self.queue.append (item)

  # Remove item from front of queue
  def dequeue(self):
    return (self.queue.pop(0))

  def peequeue(self):
    return (self.queue[0])

  # Checks if stack is empty
  def isEmpty(self):
    return (len (self.queue) == 0)

  # Returns number of elements in stack
  def size(self):
    return len (self.queue)

  # Returns string representation for stack
  def __str__(self):
    return str(self.queue)


class Vertex(object):
  # Constructor
  def __init__(self, label):
    self.label = label
    self.visited = False

  # Determines if vertex has been visited
  def wasVisited(self):
    return self.visited

  # Returns vertex's label
  def getLabel(self):
    return self.label

  # Returns string representation of vertex
  def __str__(self):
    return str(self.label)

  # Returns string representation of vertex for printing in arrays
  def __repr__(self):
    return str(self)

class Graph(object):
  # Constructor
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []

  # Check if vertex with label exists in graph
  def hasVertex(self, label):
    nVert = len(self.Vertices)

    for i in range(nVert):
      if label == (self.Vertices[i]).label:  # Then vertex in question exists
        return True
    # Otherwise, vertex in quesiton does not exist
    return False

  # Returns index of vertex with given label, returns -1 if vertex does not exist
  def getIndex(self, label):
    nVert = len(self.Vertices)

    for i in range (nVert):
      if (self.Vertices[i]).label == label:  # Then vertex exists
        return i
    # Otherwise, vertex in question does not exist
    return -1

  # Inserts vertex with given label to graph
  def addVertex(self, label):
    if not self.hasVertex (label):  # The vertex of given label may be inserted
      self.Vertices.append(Vertex(label))

      # Add new zero column in adjacency matrix for new vertex
      nVert = len(self.Vertices)

      for i in range(nVert - 1):
        (self.adjMat[i]).append(0)

      # Add new zero row in adjacency matrix for new vertex
      newRow = []
      for i in range(nVert):
        newRow.append(0)
      self.adjMat.append(newRow)

  # Add weighted, directed edge to graph
  def addDirectedEdge(self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # Add weighted, undirected edge to graph
  def addUndirectedEdge(self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # Returns unvisited vertex index i adjacent to vertex v
  def getAdjUnvisitedVertex(self, v):
    nVert = len(self.Vertices)

    for i in range(nVert):
      # If true, then vertex i is adjacent to v and vertex i is unvisited
      if self.adjMat[v][i] > 0 and not (self.Vertices[i]).wasVisited(): 
        return i
    # Otherwise, there are no adjacent vertices
    return -1

  # Performs depth-first-search on graph
  def dfs(self, v):
    # Create stack needed for algorithm
    theStack = Stack()

    # Visit vertex v visited, push v on the stack
    (self.Vertices[v]).visited = True
    print(self.Vertices [v])
    theStack.push(v)

    # Visit other vertices according to depth
    while (not theStack.isEmpty()):  # There are still unvisited vertices
      # Find an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex(theStack.peek())
      if u == -1:  # Then no unvisited vertices are adjacent to stack head
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print(self.Vertices[u])
        theStack.push(u)

    # All vertices are visited; reset every vertex's visited flag
    nVert = len(self.Vertices)
    for i in range(nVert):
      (self.Vertices[i]).visited = False

  # Performs breadth-first-search on graph
  def bfs(self, v):
    # Create queue needed for algorithm, initialize current to vertex v
    theQueue = Queue()
    current = self.Vertices[v]

    # Visit and enqueue current
    current.visited = True 
    print(current)

    # Visit other vertices according to depth
    entering_loop = True
    curr_idx = self.getIndex(current.label)
    while not theQueue.isEmpty() or entering_loop:  # There may be unvisited vertices
      if entering_loop:
        entering_loop = False

      freeIndex = self.getAdjUnvisitedVertex(curr_idx)
      if freeIndex == -1:
        current = theQueue.dequeue()
        curr_idx = self.getIndex(current.label)
      else:
        foundNode = self.Vertices[freeIndex]
        print(foundNode)
        foundNode.visited = True
        theQueue.enqueue(foundNode)

    # Reset all vertices to unvisited
    for vertex in self.Vertices:
      vertex.visited = False

  # Returns index from vertex with given label
  def getIndex(self, label):
    # Parse Vertices for vertex with given label
    nVert = len(self.Vertices)

    for i in range(nVert):
      if self.Vertices[i].label == label:  # Then vertex in question is found
        return i 
    return -1

  # Returns edge weight between two vertices
  def getEdgeWeight(self, fromVertexLabel, toVertexLabel):
    fromIndex = self.getIndex(fromVertexLabel)
    toIndex = self.getIndex(toVertexLabel)
    return self.adjMat[fromIndex][toIndex]

  # Returns list of all vertices adjacent to given vertex
  def getNeighbors(self, vertexLabel):
    out_list = []
    vertexIndex = self.getIndex(vertexLabel)

    # If true, there are adjacent unvisited vertices
    while self.getAdjUnvisitedVertex(vertexIndex) != -1:
      # getAdjUnvisitedVertex returns adjacent indices, 
      # so use that to find adjacent vertices
      adjIndex = self.getAdjUnvisitedVertex(vertexIndex)
      adjVertex = self.Vertices[adjIndex]
      adjVertex.visited = True
      out_list.append(adjVertex)

    # Output list is complete; reset all visited flags to False
    for v in out_list:
      v.visited = False
    return out_list

  # Returns a copy of the vertex list
  def getVertices(self):
    return self.Vertices[:]

  # Deletes an edge from adjacency matrix
  def deleteEdge(self, fromVertexLabel, toVertexLabel):
    i, j = self.getIndex(fromVertexLabel), self.getIndex(toVertexLabel)
    self.adjMat[i][j], self.adjMat[j][i] = 0, 0

  # Deletes a vertex from vertex list, deletes all edges from and to it in adjMat
  def deleteVertex(self, vertexLabel):
    delIdx = self.getIndex(vertexLabel)

    # Delete row for given vertex
    del self.adjMat[delIdx]

    # Delete column for given vertex
    for i in range(len(self.adjMat)):
      del self.adjMat[i][delIdx]

    del self.Vertices[delIdx]

  # Recursive helper function for hasCycle
  def cycle_helper(self, v_label):
    visited.push(v_label)
    rec_stack.push(v_label)

    for neigh in self.getNeighbors(v_label):
      if neigh.label not in visited.stack:
        if self.cycle_helper(neigh.label):
          return True
      elif neigh.label in rec_stack.stack:
        return True

    rec_stack.pop()
    return False

  # Determine if directed graph has a cycle
  def hasCycle(self):
    global visited
    visited = Stack()
    global rec_stack
    rec_stack = Stack()

    for v in self.Vertices:
      if v.label not in visited.stack:
        if self.cycle_helper(v.label) == True:
          return True
    return False

  # Returns array of vertices after topological sort
  def toposort(self):
    out_list = []
    if self.hasCycle(): return out_list; # because toposort undefined 
    
    while any(not v.visited for v in self.Vertices):
      # Find unvisited vertex
      for v in self.Vertices:
        if v.visited == False:
          current = v
      while (self.getAdjUnvisitedVertex(self.getIndex(current.label))) != -1:
        current = self.Vertices[self.getAdjUnvisitedVertex(self.getIndex(current.label))]
      if current.label != "": out_list.insert(0, current.label);
      current.visited = True

    # Unvisit all vertices
    for v in self.Vertices:
      v.visited = False

    return out_list
      







def main():
# Create graph object
  graph = Graph()

  # Open input file for reading
  inFile = open("./topo2.txt", "r")

  # Read in vertices, insert them into graph
  numVertices = int(inFile.readline().strip())
  print(numVertices)
  print()

  for i in range((numVertices * 4) // 2):
    vertex = inFile.readline().strip()
    if vertex != "":
      print(vertex)
    graph.addVertex(vertex)
  print()

  # Read in edges, insert them into graph
  inFile.readline()
  numEdges = int(inFile.readline().strip())
  print(numEdges)
  print()

  for i in range((numEdges * 4) // 2):
    edge = inFile.readline().strip()
    if edge != "":
      print(edge)
      edge = edge.split()

      # Define parameters for addDirectedEdge()
      start = graph.getIndex(edge[0])
      finish = graph.getIndex(edge[1])
      weight = 1

      # Add edge
      graph.addDirectedEdge(start, finish, weight)

  print(graph.hasCycle())
  print(graph.toposort())



main()

