def load_ratings(filename):
    tuplelist=[]  
    try:
        with open("movie_ratings.txt","r") as readfile:
            newlist=readfile.readlines()
            for elements in newlist:
                sentance=elements.strip().split(",")
                tuplelist.append(sentance[0],int(sentance[1]))
    except: 
        print("File not found")     
