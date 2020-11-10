def csFindAllPathsFromAToB(graph):
    all_paths = []
    visited = set()
    helper(graph, 0, [], all_paths, visited)
    return all_paths
    # N = length of graph 
    #   graph has nodes 0 - n-1 (nodes are labeled 0, 1, ... N-1)
    #   graph[a] is a list of nodes that node a has an edge to (adjacency list)
    # find _all_ possible paths from 0 to N-1 --> "all" means we need a home for them 
    # we're given a DAG --> no loops
    # Input: graph = [
            # [1, 2],   # <-- graph[0]
            # [3],      # <-- graph[1]
            # [3],      # <-- graph[2]
            # [4],      # <-- graph[3]
            # []        # <-- graph[4]
            # ]
    # Output: array of arrays, inner array are the individual paths from 0 .. N-1
    # start = 0
def helper(graph, start, current_path, all_paths, visited):
    """
    start is an int representing the "label" of the node / index into graph
    graph is an array of arrays, where graph[a] is a list of nodes that node a has an edge to (adjacency list)
    """
    # all_paths = [[0, 1, 3], ]
    # cur_path = 0, 2
    # visited = 0, 1, 
    # neighbor:  2
        # helper(2): 
    # DFS --> let's do recursively
    # we need a home for _all_ the paths from `0` to `N-1`
    # somewhere need to keep track of visited
    # a) We don't need to keep track of visited because it's a DAG, so no cycles
    # b) We don't _want_ to keep track of visited because there can be multiple paths through 
    # the same node (e.g., test 2)
    # if start in visited:
    #     return
    # Things we need to do every iteration:  
    #   - "what are we trying to do?" --> build up the paths --> 
            # --> the current node is on a path, so let's add it 
            # --> we need some variable keeping track of the current path
    current_path.append(start)
    # if we use recursion, that means we need: 
    # 1) base case: if our current node == target (N-1)
    if start == len(graph) - 1:
            # --> add the current path to all paths
        all_paths.append([element for element in current_path])
        # pop off the last element for current_path (target) to reset it for the next path
        current_path.pop()
        return
    #    base case: if there are no more neighbors for the current node (start)
    if len(graph[start]) == 0:
        return  # there are no paths down this route that end in target
    # 2) move to recurse, moving closer to base case
    #   - omit visited
    #   - "increment" start node --> process one of its neighbors 
    # 3) things we need to do on every iteration: 
    #   - mark node as visited
    visited.add(start)
    #   - keep track of all neighbors --> make sure we loop over and call the recursive function on each of them
    for neighbor in graph[start]: 
        helper(graph, neighbor, current_path, all_paths, visited)
    # we've explored all of the current nodes neighbors, we're "done" with it
    # so we pop it off current_path
    current_path.pop()