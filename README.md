# Best Spot to Meet

Best Spot to Meet
Yusuf, Ali and Berat are best friends, and they live in the beautiful city of Mersin, Turkey. They have decided to meet each other after the work, however, because of their jobs, they might end up their day in different parts of the city, and it is not efficient to choose the location of the meeting beforehand. They all are agreed on that the location of coffee must be such that it reduces the amount of distance each one should travel.


Mersin’s transportation network can be modeled as a Tree graph ( In graph theory, a Tree is an undirected graph in which any two vertices are connected by exactly one path), and in each vertices of the tree, there is a coffee shop that the friends can meet. You also can consider that each edge has a same distance (e.g. the length of each edge is 1 km). Your task here is to help them to find the best spot for their meetings. It is important to note that they want to minimize the maximum distance travelled by each individual, and they do not want to minimize the total length of distance they need to travel.

## Floyd Warshall Algorithm

Our first approach to this problem was to calculate the shortest paths for all pairs in the graph. The naive algorithm to achieve this is
to use a dynamic programming algorithm called Floyd Warshall. There are O(V^3) sub-problems and each take constant time. It runs in O(V^3).

## Johnson's Algorithm



## Dijkstra's Algorithm



## Breadth First Search Algorithm