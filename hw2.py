
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
                print ("Node 0: %s\tNode 1: %s" % (nodes[0], nodes[1]) )
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
	neighbours_list = bfs_tree.neighbours(s)
	bacon.append(len(neighbours_list))
	count = 1;
	
	
	while(count < 6):
		for n in neighbours_list:
			
		len(list(bfs_tree.neighbours(curr))-1
		count++
	

    

def main(fn, s):
    g = read_graph(fn)
    
    #draw_graph(g)
    
    #run_bfs_using_nx(g,s)
    
    #run_dfs_using_nx(g,s)
    


if __name__ == "__main__":
    print (sys.argv) 
    if len(sys.argv) == 3:
        fn = sys.argv[1] # Filename
        s  = sys.argv[2] # Source node
        
        main(fn,s)
