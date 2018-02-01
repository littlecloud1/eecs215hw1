# -*- coding: utf-8 -*-
"""
Hw1 bouns ex3.
use a bipartite graph to represent the relationship with
the movies and actor.

1/23/2018

lai man tang
yuan qin

"""


import networkx as nx
import matplotlib.pyplot as plt
import sys

actorlist = []
def read_graph(filename):
    l = 0
    g = nx.Graph()
    # Open file and read line by line.
    with open(filename) as fp:
        for line in fp:
            if l > 1:
                # Split lines by chosen character.
                nodes = line.strip().split('+')
                # Add edge to graph with node's name.
                g.add_edge(nodes[0], nodes[1])
                if nodes[1] not in actorlist:
                    actorlist.append(nodes[1])
            l += 1

    return g


def Bacon(g, s):
    bfs_tree = nx.bfs_tree(g, s)
    bacon = []
    for i in range(7):
        bacon.append(0)
    bacon[0] = 1


    count = 1
    currlayer = []
    while(count < 7):
        # print(count)

        if count == 1:
            next_neighbor = list(bfs_tree.neighbors(s))
        else:
		    #skip the movie nodes
            for y in currlayer:
                next_neighbor += bfs_tree.neighbors(y)
            currlayer = []
		#accumulate the #neighbors in each level	
        for x in next_neighbor:
            currlayer += list(bfs_tree.neighbors(x))
            bacon[count] += len(list(bfs_tree.neighbors(x)))
        count += 1
        next_neighbor = []


    #Output on screen
    print("Bacon number  Frequency")
    total = 0;
    for i in range(0, len(bacon)):
        total += bacon[i]
        print("{} {}".format(i, bacon[i]))
    print("Unreachable {}".format(len(actorlist) - total))


def main(fn, s):
    g = read_graph(fn)
    Bacon(g, s)


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) == 3:
        fn = sys.argv[1]  # Filename
        s = sys.argv[2]  # Source node

        main(fn, s)
