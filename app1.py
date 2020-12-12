usersDict={} 
temp=[] #stores key and val from file, one line at a time
with open("data/users.txt","r") as f: #file -> dict, to use latter later
    line = f.readline()
    while line:  #read lines until nothing in the line (i.e. @eof)
        temp = line.split(": ") #now temp[0]==user name, temp[1]==its future dict
        usersDict[temp[0]]={} #now user has a dict

        temp[1]=temp[1].strip('\n')
        temp1=temp[1].split(', ') #splits the two future keys+vals of a dict
        tempC1=temp1[0].split(' ') #both of these lines split the key from val
        tempC2=temp1[1].split(' ')
        usersDict[temp[0]][tempC1[0]]=tempC1[1] #now inserting concerts into user dict
        usersDict[temp[0]][tempC2[0]]=tempC2[1]
        line = f.readline()
    f.close()
    print(usersDict)
