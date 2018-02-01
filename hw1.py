"""
Hw1 bouns ex1: Graph dataset generator
Output the #vectice, #edges and nodes pair:actor+actor.

1/23/2018

lai man tang
yuan qin

"""

import sys
actor_dict = {} #dictionary for actor: key: actor; value: list of actors
movie_dict = {} #dictionary for movie: key: move; value: list of actors



def readfile(filename):

	with open(filename) as f:
		for line in f:
			actor_in_movie = line.strip().split("|")
			actor = actor_in_movie[0]
			movie = actor_in_movie[1]
			
			#add data in movie dict
			if movie not in movie_dict:
				list = []
				list.append(actor)
				movie_dict[movie] = list
			else:
				movie_dict[movie].append(actor)
				
		
	f.close()

#build actor dictionary
def builddict():	
	for movie in movie_dict:
		for i in range(0, len(movie_dict[movie])-1):
			for j in range(1, len(movie_dict[movie])):
				addtodict(movie_dict[movie][i],movie_dict[movie][j])
	
	
			
			
			
#output function 			
def output(outfile):
	
	edge = []
	visited = [] #keep visited actor list
	for key1 in actor_dict:
		for key2 in actor_dict[key1]:
		    # if key1-key2 pair not added, build the edge
			if key2 not in visited:
				s =  str(key1)+ '+'+str(key2)
				edge.append(s)
		visited.append(key1)
	
	#file output
	f = open(outfile,'w')
	f.write(str(len(actor_dict))+"\n")
	f.write(str(len(edge))+"\n")
	for e in edge:
		f.write(e+"\n")
	
	f.close()
	
	
	

# check two actor's dictionary, if no redunancy, add to actor dictionary
def addtodict(key1, key2):
	if key1 == key2 :
		return
	if key1 not in actor_dict:
		list =[]
		list.append(key2)
		actor_dict[key1] = list
	else :
		if key2 not in actor_dict[key1]:
			actor_dict[key1].append(key2)
	
	if key2 not in actor_dict:
		list =[]
		list.append(key1)
		actor_dict[key2] = list
	else :
		if key1 not in actor_dict[key2]:
			actor_dict[key2].append(key1)		
			
				
	
	
	
				


def main (argv):
	readfile(argv[1])
	builddict()
	output(argv[2])


if __name__ == "__main__":
	main(sys.argv)





