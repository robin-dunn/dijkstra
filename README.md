# Citymapper Router Challenge - Robin Dunn

## Compile and run

Run the bash script ./run.sh passing the node IDs as command line arguments e.g.:

./run.sh 314185938 1320557460

This calls a python script to calculate the shortest distance between the nodes.

## Design decisions

For simplicity in this implementation I've used an adjacency dictionary (see Network.py)
to store the distance costs for the neighbors of each node.  

The data structure will likely use a large amount of memory if the network graph is large,
this is because a NodeInfo object is allocated for each adjacency item.  A more memory
efficient way to store the adjacencies would be to write them to a memory-mapped file
and implement a method to read from this.

## References

Some of the code in this solution has been adapted from the following Medium article by Adrienne Johnson:

https://medium.com/@adriennetjohnson/a-walkthrough-of-dijkstras-algorithm-in-javascript-e94b74192026