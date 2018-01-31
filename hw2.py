
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
                # Format string example:
                #print ("Node 0: %s\tNode 1: %s" % (nodes[0], nodes[1]) )
                # Add edge to graph with integer IDs.
                #g.add_edge(int(nodes[0]),int(nodes[1]))
                g.add_edge(nodes[0],nodes[1])
            l+=1
               
    return g

def draw_graph(g):
    
    nx.draw_networkx(g)
    # Draw graph in separate window.
    plt.show() 

def run_bfs_using_nx(g, s):
    
    bfs_tree = nx.bfs_tree(g,s)
    draw_graph(bfs_tree)
    
def run_dfs_using_nx(g, s):
    
    dfs_tree = nx.dfs_tree(g,s)
    draw_graph(dfs_tree)

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
			next_neigh += list(bfs_tree.neighbors(n))
			bacon[count] += len(list(bfs_tree.neighbors(n)))
		neighbours_list = next_neigh 
		count += 1
	
	total = 0;
	for i in range(0,len(bacon)):
		total += bacon[i]
		print("{} {}".format(i, bacon[i]))
	print(g.number_of_nodes())
	print(total)
	print("other: {}".format(g.number_of_nodes() - total))
    

def main(fn, s):
    g = read_graph(fn)
    
    #draw_graph(g)
    
    #run_bfs_using_nx(g,s)
    
    #run_dfs_using_nx(g,s)
    Bacon(g,s)
    


if __name__ == "__main__":
    print (sys.argv) 
    if len(sys.argv) == 3:
        fn = sys.argv[1] # Filename
        s  = sys.argv[2] # Source node
        
        main(fn,s)
