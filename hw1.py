
actor_dict = {}
movie_dict = {}




def readfile(filename):

	with open(filename) as f:
		for line in f:
			actor_in_movie = line.strip().split("|")
			actor = actor_in_movie[0]
			movie = actor_in_movie[1]
						
			if movie not in movie_dict:
				list = []
				list.append(actor)
				movie_dict[movie] = list
			else:
				movie_dict[movie].append(actor)
	f.close()
	
def builddict():	
	for movie in movie_dict:
		for i in range(0, len(movie_dict[movie])-1):
			for j in range(1, len(movie_dict[movie])):
				addtodict(movie_dict[movie][i],movie_dict[movie][j])
	
	
			
			
			
			
def output(outfile):
	
	edge = []
	visited = []
	for key1 in actor_dict:
		for key2 in actor_dict[key1]:
			if key2 not in visited:
				s =  '"'+key1+'"' + ' ' + '"'+ key2+'"'
				edge.append(s)
		visited.append(key1)
	
	f = open(outfile,'w')
	f.write(str(len(actor_dict))+"\n")
	f.write(str(len(edge))+"\n")
	for e in edge:
		f.write(e+"\n")
	
	f.close()
	
	
	

	
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
			
				
	
	
	
				


def main ():
	readfile("imdb.small.txt")
	builddict()
	output("imdb.small_graph.txt")


if __name__ == "__main__":
	main()





