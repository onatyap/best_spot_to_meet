# Best Spot to Meet

Best Spot to Meet
Yusuf, Ali and Berat are best friends, and they live in the beautiful city of Mersin, Turkey. They have decided to meet 
each other after the work, however, because of their jobs, they might end up their day in different parts of the city, 
and it is not efficient to choose the location of the meeting beforehand. They all are agreed on that the location of 
coffee must be such that it reduces the amount of distance each one should travel.

Mersin’s transportation network can be modeled as a Tree graph ( In graph theory, a Tree is an undirected graph in which
any two vertices are connected by exactly one path), and in each vertex of the tree, there is a coffee shop that the 
friends can meet. You also can consider that each edge has a same distance (e.g. the length of each edge is 1 km). Your
task here is to help them find the best spot for their meetings. It is important to note that they want to minimize 
the maximum distance travelled by each individual, and they do not want to minimize the total length of distance they 
need to travel.

## Floyd Warshall Algorithm

Our first approach to this problem was to calculate the shortest paths for all pairs in the graph. The naive algorithm to achieve this is
to use a dynamic programming algorithm called Floyd Warshall. There are O(V^3) sub-problems and each take constant time. It runs in O(V^3).

## Johnson's Algorithm

Similar to our first approach, the second approach also calculates the shortest paths for all pairs. However, this time
it performs Dijkstra's algorithm from each node to every other node. As we're using an array based priority queue in
this approach, the algorithm runs in O(n^3). If the algorithm was implemented by using a min-heap, it would've taken
O(n^2*log(n)) time.

## Dijkstra's Algorithm from Friend Locations

After observing Johnson's algorithm's performance, we decided to reduce the number of visited nodes by starting the
search from only the nodes that each friend is located. By this improvement, the algorithm works in O(q*n^2). 
If the algorithm was implemented by using a min-heap, it would've taken O(q*n*log(n)) time.

## Breadth First Search Algorithm

Since the weights in a provided graph are all constant (1), we realized that we did not need to run Dijkstra's 
algorithm. Instead, it would suffice to run breadth-first search from the locations that friends are located in and
keep track of the distances. This improvement in the algorithm takes O(q*n) time.

## Multi Breadth First Search Algorithm

Our next approach is running Breath First Search at the same time only from the nodes that each friend is located. 
At each iteration, we pop the next element from the queue for each friend and add that element to the array that we 
keep all visited nodes. The first node that is visited by all friends is our optimal node. If there are more than one
node that is visited by all friends at the same time, we decide the optimal node based on comparisons. The total time 
complexity of this algorithm is still O(q*n) - need to visit all nodes in the worst case. However, the number of visited 
nodes are generally lower than previous case since we return as soon as we find the optimal node.

## Tree Breadth First Search Algorithm

Finally, in order to obtain O(log(n)) search times between each friend nodes, we concerted the given graph to a tree
structure. The algorithm assumes final tree height of log(n), which allows the paths between each combination of friends
in O(log(n)) time. After each path is discovered, the center node in the longest path is selected, and then the optimal
center location is selected based on the other paths' placements. Since the tree structure takes O(n) time to build, and
the rest runs in O(log(n)) time for each day, the total time complexity of this algorithm is O(n + q*log(n)).

## How to run?
You can run our most optimal solution using:
To solve an example case with a specific algorithm
```python3 src/main.py [ExampleFilePath] [AlgorithmName]```

To solve all example cases with a specific algorithm
```python3 src/main.py all-examples [AlgorithmName]```