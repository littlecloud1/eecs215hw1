"""
Hw1 bouns ex2: Caculate bacon nubmer using BFS
Output the #vectice, #edges and nodes pair:movie+actor.

1/23/2018

lai man tang
yuan qin

"""
import networkx as nx
import matplotlib.pyplot as plt
import sys


def read_graph(filename):
    l=0
    g = nx.Graph()
    # Open file and read line by line.
    with open(filename) as fp:
        for line in fp:
            if l>1:
                # Split lines by chosen character.
                nodes = line.strip().split('+') 
                # Add edge to graph with node's name.
                g.add_edge(nodes[0],nodes[1])
            l+=1
               
    return g

# this function doesn't called in this exercise	
def draw_graph(g):
    
    nx.draw_networkx(g)
    # Draw graph in separate window.
    plt.show() 

def Bacon(g, s):
	bfs_tree = nx.bfs_tree(g,s)
	bacon = [1]
	neighbours_list = list(bfs_tree.neighbors(s))
	bacon.append(len(neighbours_list))
	count = 2;
	
	while(count < 7):
		next_neigh =[]
		bacon.append(0)
		for n in neighbours_list:
			#accumulate the #neighbors in each level	
			next_neigh += list(bfs_tree.neighbors(n))
			bacon[count] += len(list(bfs_tree.neighbors(n)))
		neighbours_list = next_neigh 
		count += 1
		
    #Output on screen
	print("Bacon number  Frequency")
	total = 0;
	for i in range(0,len(bacon)):
		total += bacon[i]
		print("{} {}".format(i, bacon[i]))
	print("Unreachable {}".format(g.number_of_nodes() - total))
    

def main(fn, s):
    g = read_graph(fn)
    Bacon(g,s)
    


if __name__ == "__main__":
    print (sys.argv) 
    if len(sys.argv) == 3:
        fn = sys.argv[1] # Filename
        s  = sys.argv[2] # Source node
        
        main(fn,s)
