# Assignment 0

# 1. Find  Luddy Hall

Solution:

- Using BFS to find the shortest path from source to destination
- BFS always gives the optimal solution - shortest pat in this case as all edges in the graph are of equal weight.
- To avoid visiting paths again, I have maintained a matrix that checks if a node is previously visited.
- This matrix is same as the input\_board matrix, everything intially initialised to False. The moment a node is poped from the queue (fringe) and all its neighbours are added to the queue, it is marked as visited.
- Keeping track of the path:
  - I am using a matrix (pred) in the code that stores the parent/predecessor of each node in the map.
  - Intially, all the nodes are marked as (-1, -1). The parent of source node is kept as (-1,-1) and the parent to its adjacent nodes are marked as the current node.
- Distance:
  - Every time we append adjacent nodes to the fringe (queue), we append the distance as well. Distance = Distance(predecessor/parent) + 1
  - This way we are storing the distance from source to destination
- Printing the path:
  - Once the destination is reached, we try to print the node followed by its parent/predecessor and then recursively the parent of that node and so on.
  - This way we recursively call the parents from the &#39;pred&#39; matrix until the source is reached.
- Directions:
  - Once we get the path - list of indices from source to destination, we write a util function that gives direction of the source and its next move.
  - If we move a row upwards (row-1) from parent then its N (North), if we move towards right (column + 1) then its E (East). Similarly for West and South.

Why does the program often fail to find a solution?
  - fringe.pop() wasn't mentioned and the logic for BFS implementation wasn't coded. So the while loop was running on a infinite loop.

What parts were missing?
  - The logic to implement search algorithm for shortest path.
  - Popping from the fringe.
  - Tracking of the predecessors for keeping track of the directions (NSEW)
  
Five Abstractions:
- Initial state: The map/board with the person at source location.
- Goal state: The shortest path from source to destination. The person at destination – Luddy hall.
- Cost: The cost to find the shortest path from source to destination involves the person moving from source to all possible locations.
- Set of valid states: These are the set of all states where the person is not located at buildings. This involves the person located at every possible location on the map except at the ones where there is building.
- Successor: From any location on the map, all possible states where the person can move to in the board. By all moves I mean only the ones where the move is valid, that is, there is no building and the node is connected directly in one of the four directions. Simply put, successor of any node is the set of all of its adjacent (connected) valid (no building) nodes.

# 2. Hide and Seek

Solution:

- BFS search with keeping track of only valid and previously not visited positions.
- We start with initial board. No friends (F) on the map.
- To keep track of all visited nodes, we use a list that gives us info on if a board state is already considered and evaluated. We initialize a list of all visited states to empty.
- From each state, we find the successors with one friend (F) added to the map
- From each state, we find the successors with one friend (F) added to the map. This successor list consists of F added in all valid positions on the map.
- Check if the current state from its successor list is not visited.
- If not visited, check if the board is valid.
- If the board is valid, check if the goal is reached. If the goal is reached, return. Else, append the state to fringe.
- Append the state to visited list, to make sure we don&#39;t visit it again and go into an infinite list.
- Check if board/state is valid: isBoardValid()
  - For each of the friend 'F' on the board, check if he is blocked from seeing other friends.

Why does the program fails?
  - The logic to find if a state is valid was missing.
  - Implementation of the solution wasn't complete.

What parts are missing?
  - Function to check if a Friend can see others was missing
  - Logic to the search algorithm implementation was missing

Five Abstractions:
- Initial state: The map/board with the no friends.
- Goal state: To place all the friends on the map so that they can't see each other.
- Cost: Cost to place a friend on the board involves placing the friends on all possible locations and checking if the state on the map is valid or not.
- Set of valid states: These are the set of states where all one to 'n' friends are placed on the map at all possible locations.
- Successor of a state: Successor of a state is set of all states where a friend is added at all possible valid locations on the map.
