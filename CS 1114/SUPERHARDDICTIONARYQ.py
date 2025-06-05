with open("nyu_students.csv","r") as readfile:
    biglist={}
    captiondict={}
    
    header=readfile.readline()
    header=header.strip()
    headlist=header.split(",")
    # print(headlist)
    
    for lines in readfile:
        newline=lines
        newline=newline.strip()
        newlinelist=newline.split(',')
        newdict={}
        for i in range(1,len(headlist)):
            newdict[headlist[i]]=newlinelist[i]
        biglist[newlinelist[0]]=newdict

print(len(biglist))
        
