    #CancelALL
    if form.validate_on_submit(): #once submitted
        loadSeats() #can now use data's
        user = session.get('name')+session.get('lastname')            
        dateSelected = session.get('dateSelected')  #open selected concert on that day

        usersDict[user][dateSelected]="" #wipe all the seats of this user in this concert by clearing the val of its dict entry 
        updateUsers() 

        filename = "data/" + dateSelected + "/A.txt" #open each row on that day
        with open(filename,"w") as f:
            currData = dataA  #current row of info (dataA pulled from file already)
            #goes thru list, changing any of your seats to empty, writing all to file
            for i in range(len(currData)-1): #i=index  ....
                if currData[i] == user: #if that's your seat
                    currData[i] = "None"
                f.write(currData[i]) #whether a change or not, write it to a file
                f.write(" ")
            f.write(currData[i]) #last one. no space after this one.
            f.close()
        filename = "data/" + dateSelected + "/B.txt" #open each row on that day
        with open(filename,"w") as f:
            currData = dataB  #current row of info (dataB pulled from file already)
            #goes thru list, changing any of your seats to empty, writing all to file
            for i in range(len(currData)-1): #i=index  ....
                if currData[i] == user:
                    currData[i] = "None"
                f.write(currData[i]) #whether a change or not, write it to a file
                f.write(" ")
            f.write(currData[i]) #last one. no space after this one.
            f.close()
