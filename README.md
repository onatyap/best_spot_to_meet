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

Our first approach to this problem was to calculate the shortest paths for all pairs in the graph. The naive algorithm
to achieve this is to use a dynamic programming algorithm called Floyd Warshall. There are O(V^3) sub-problems and each
take constant time. It runs in O(V^3).

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

Our next approach is running Breadth First Search at the same time only from the nodes that each friend is located. 
At each iteration, we pop the next element from the queue for each friend and add that element to the array that we 
keep all visited nodes. The first node that is visited by all friends is our optimal node. If there are more than one
node that is visited by all friends at the same time, we decide the optimal node based on comparisons. The total time 
complexity of this algorithm is still O(q*n) - need to visit all nodes in the worst case. However, the number of visited 
nodes are generally lower than previous case since we return as soon as we find the optimal node.

## Tree Breadth First Search Algorithm

Finally, in order to obtain O(log(n)) search times between each friend nodes, we converted the given graph into a tree
structure. Before constructing the tree, first we need to find its root. This can be accomplished by finding the
center of the two most distant nodes in the graph. After having found the root, we construct the tree as follows: 
For each node, we add all the corresponding nodes from the adjacency list to its children list while we set their parent to this
particular node unless the corresponding node is the root itself. All nodes in the graph are kept in a container list
where any node can be accessed by its vertex index, so we do not need to go down the tree each time, hence the construction
takes O(n). The key aspect of our approach is augmenting this tree such that each node contains a field called **_subtree_** 
**_index_** which allows us to easily locate a node from its grandparents. Specifically, instead of running BFS to find
the path between two vertices, The algorithm assumes final tree height of log(n),
which allows the paths between each combination of friends in O(log(n)) time. After each path is discovered, the middle
node in the longest path is chosen as center, and then the optimal center location is selected based on the other paths'
placements. Since the tree structure takes O(n) time to build, and the rest runs in O(log(n)) time for each day,
the total time complexity of this algorithm is O(n + q*log(n)).

## Correctness of the Tree Breadth First Search Algorithm

### Lemma 1:

The center of a tree is the middle node of the two most distant nodes (the longest path) where the center (or root) means minimizing the maximum distance to all other nodes.

### Proof to Lemma 1:

We will prove the lemma by induction.

In the base case, let’s cover the trivial graphs where the number of nodes are ≤3. For V = 1, the center is trivial, it is the only node in the graph. For V = 2, the center is either one of the nodes. 

For V = 3, the center is the middle node of the two most distant nodes. In the tree below, we can see that choosing node C minimizes the maximum distance to all other nodes, i.e. A and B.
In the induction case, let’s assume that we have a tree whose longest path is from node A to node B (call it dAB) and node C is located in the middle of this path. Our claim is that the center node picked from the middle of the longest path in the tree minimizes the distances to all other nodes. If this claim holds when another node is added to the tree, we can conclude our proof.

We have 3 cases to observe in this step:

#### Case 1 (dAR ≥ dBR > dCR):
If dAR ≥ dBR > dCR, then C does not affect the longest path, as dAB > dCX for any node X in the tree. This holds because if there was a node such that dCX > dAB, then this path must go through the center which implies dCX = dCR + dRX. Knowing that dAR ≥ dBR > dCR; we can see that the distance turns out to be  dRX > dAR + dBR - dCR > dAR = dBR which is strictly larger than dAR and that contradicts with the initial assumption.

Thus, the center is preserved between the longest path in the tree.

#### Case 2 (dAR ≥ dBR = dCR):
If dAR ≥ dBR = dCR, we do not have to even consider C as not only does it leave the longest path unaffected but also it does not violate the given distance constraints.

#### Case 3 (dCR > dAR > dBR):
If dCR > dAR > dBR, the longest path changes to dCA if their first common ancestor is the root. The center is now located in the middle of this path, named R’ and satisfies one of the following conditions:
dCR’ = dAR’ ≥ dBR’ >...
dCR’ > dAR’ ≥ dBR’ >...
dAR’ > dCR’ ≥ dBR’ >...

By the definition of the center of the longest path of our algorithm, the new center R’ satisfies the minimization of distances to all other nodes as dCR is the new farthest node from the root and the provided constraints complete the proof.



#### Tree Breadth First Search: 


We will now discuss how the algorithm works. 

The preprocessing step involves constructing an augmented tree whose nodes have a field called subtree index which allows us to traverse faster in the graph.

In this step, we first generate an adjacency list from the input node list. For each node in this node list, we map the vertex to its neighbors in a Python dictionary. In order to construct the tree, we need to figure out the root of it. By Lemma 1, we can do that by finding the two most distant nodes in the tree. This is done by running two Breadth First Search in the graph, where the first BFS finds the most distant node to a randomly selected node and second finds the most distant to that one. Their center gives us the root, which is the foundation of our tree construction.

Starting from the root, we construct the tree by connecting the corresponding children and parent for each node. The key aspect of our algorithm is what we call the subtree index. This allows us to travel fast between the nodes in the tree, that is the worst case traverse takes O(height(tree)). For a node, the subtree index is constructed such that  ith index of this field corresponds to the grandparent’s child index where the grandparent’s height is i (starting from the root). A subtree index example is shown below. This whole process takes O(n) as we hold a node container list that we can access its ith element by indexing in constant time and connecting nodes and subtree index takes O(1) as well.
After having constructed the tree, we are now ready to find the center of our three friends.

By Lemma 1, we know that the center of 3 friends in the tree is the middle node of the most distant two friends. There can be edge cases where the length of the distance between these two friends are even such that the center can be closer to one of these friends, and we can decide which center to choose by minimizing the distance between each of the possible centers with the other friend.

Finding the most distant two friends requires us to run three guided traversals in the tree, that is from friend a to b, b to c, and c to a. In each traversal, we take advantage of the subtree index as follows. Let’s say from a source node say friend c (16 in the example below), we want to traverse all the way to the destination node friend a. First, we compare their subtree index to find their common ancestor (or predecessor) with maximum height and traverse there (1 in the example below), which takes O(height(tree)) worst case. Then, from this node, we go to the destination node (12 in the example below) which again takes O(height(tree)).



#### Future Works on the Algorithm:

As discussed previously, Lemma 1 allows us to choose the center node in the longest path that is among given friends in the tree. The determination of the longest path or its center does not depend on the number of friends that are located in the tree, hence the algorithm can be extended to support more friends.  

## How to run?
You can run our optimal solution using:
```python main.py [ExampleFilePath]```

To solve a specific example case with a specific algorithm (stores the result in its corresponding file in outputs)
```python main.py [ExampleFilePath] [AlgorithmName]```

To solve all example cases with a specific algorithm
```python main.py all-examples [AlgorithmName]```

To compare all solution cases with a specific input file
```python main.py all-solutions [ExampleFilePath]```

To run all example cases using all algorithms
```python main.py```
