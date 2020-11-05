"""
UNDERSTAND: 
given a DAG, that contains N nodes, write a functionality that can find all the possible paths
from 0 to N - 1, and returns the path in any order

N = length of the graph 
    - graph has nodes 0 >> n-1 
    - graph[a] is a list of nodes that tells node A has an edge to Node B (adjacency list)

input: 

graph = [
    [1, 2],     << graph[0]
    [3],        << graph[1]
    [3],        << graph[2]        
    [4],        << graph[3]
    []          << graph[4]
]

this is an adjacency list for the following: 

0 -- 1
|    |
2 -- 3
     |
     4

PLAN: 
Output should be an array of array, where inner array are the individual paths from 0 ... N-1

start = 0
visited = []

implement recursion: 
    1.) define base case 
        - base case: if the current_node == target (N-1)
        - base case: if there are no new neighbors 

    2.) move to recurse, and move closer to the base case 
        - if the node has been visited, omit it 
        - incremenet the starting node ++ process one of its neighbors 

    3. book keeping: 
        - mark node as visited 
        - add the connected nodes to the call stack 
            - loop over and call recursive function on each item in the call stack 
    
    4. requested tasks 
        - the current node is on the path, so it needs to be added to the sub array 
            - this will require that we have something to keep track of this 

"""

def util__book_keeping(graph, start, current_path, all_paths):

    current_path.append(start)

    if start in visited:
        return 


    if start == len(graph) - 1:
        # creating copy of the current path item to not mutate the OG 
        all_paths.append([element for element in current_path])
        current_path.pop()
        return

    # checking if the starting node given has any connected node
    if len(graph[start]) == 0:
        return [] 
    
    visited.add(start)
  
    for next_node in graph[start]:
        util__book_keeping(graph, next_node, current_path, all_paths, visited)
    
    current_path.pop()


def AtoBLife(graph)
    all_paths = []
    visited = set()
    util__book_keeping(graph, 0, [], all_paths, visited)
    return all_paths



# ! Online version 

from collections import defaultdict 
   
# This class represents a directed graph  
# using adjacency list representation 
class Graph: 
   
    def __init__(self, vertices): 
        # No. of vertices 
        self.V = vertices  
          
        # default dictionary to store graph 
        self.graph = defaultdict(list)  
   
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
   
    '''A recursive function to print all paths from 'a' to 'b'. 
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''
    def printAllPathsUtil(self, current, target, visited, path): 
  
        # Mark the current node as visited and store in path 
        visited[current]= True
        path.append(current) 
  
        # If current vertex is same as destination, then print 
        # current path[] 
        if current == target: 
            # add the path to larger array
            print path 
        else: 
            # If current vertex is not target 
            # Recur for all the vertices adjacent to this vertex 
            for i in self.graph[current]: 
                if visited[i]== False: 
                    self.printAllPathsUtil(i, target, visited, path) 
                      
        # Remove current vertex from path[] and mark it as unvisited 
        path.pop() 
        visited[current]= False
   
   
    # Prints all paths from 's' to 'd' 
    def printAllPaths(self, current, target): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 
  
        # Create an array to store paths 
        path = [] 
  
        # Call the recursive helper function to print all paths 
        self.printAllPathsUtil(current, target, visited, path) 
   
   
   
# Create a graph given in the above diagram 
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(0, 3) 
g.addEdge(2, 0) 
g.addEdge(2, 1) 
g.addEdge(1, 3) 
   
s = 2 ; d = 3
print ("Following are all different paths from % d to % d :" %(s, d)) 
g.printAllPaths(s, d) 

def csFindAllPathsFromAToB(graph):
    all_paths = []
    visited = set()
    helper(graph, 0, [], all_paths, visited)
    return all_paths

    # start = 0
def helper(graph, start, current_path, all_paths, visited):
    
    current_path.append(start)

    if start == len(graph) - 1:
            # --> add the current path to all paths
        all_paths.append([element for element in current_path])
        # pop off the last element for current_path (target) to reset it for the next path
        current_path.pop()
        return
   
    #    base case: if there are no more neighbors for the current node (start)
    if len(graph[start]) == 0:
        return  # there are no paths down this route that end in target
  
    visited.add(start)
    #   - keep track of all neighbors --> make sure we loop over and call the recursive function on each of them
    for neighbor in graph[start]: 
        helper(graph, neighbor, current_path, all_paths, visited)
   
    current_path.pop()