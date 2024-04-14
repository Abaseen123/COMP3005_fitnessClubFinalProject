import psycopg2
loggedUser = 'NULL'
perms = 'NULL'
id = 0


# Cancel Solo Booking Handler
def cancelSolo():
    try:
        print()

        # Fetch all available sessions
        query = "SELECT SOLO_SESSION.trainer_id, SOLO_SESSION.member_id, SOLO_SESSION.dayofweek, SOLO_SESSION.starttime, SOLO_SESSION.endtime, TRAINERS.first_name, TRAINERS.last_name \
                 FROM SOLO_SESSION INNER JOIN TRAINERS ON SOLO_SESSION.trainer_id = TRAINERS.trainer_id\
                 WHERE SOLO_SESSION.member_id = " + str(id) + ";"
        cursor.execute(query)
        rows = cursor.fetchall()
        rownum = 0

        # Return nothing if no sessions found
        if (len(rows) == 0):
            print("No Solo Sessions Booked")
            return
        
        # Display Information of all available sessions to User
        for tup in rows:
            rownum += 1
            print("Session #:", str(rownum) + "\n   Trainer: " + str(tup[5]) + " " + str(tup[6]))
            print("   Day: " + str(tup[2]))
            print("   Start Time: " + str(tup[3]))
            print("   End Time: " + str(tup[4]) + "\n")    

        # Prompt user to cancel session, checking bounds on the inputs
        option = input("Enter the Session Number you would like to cancel: ")
        while (int(option) < 1 or int(option) > rownum or not option.isnumeric()):
            print("ERROR: Invalid Session Number")
            option = input("Re-Enter the Session Number you would like to cancel: ")
        
        # Update the session to remove the user from the table
        query = "UPDATE SOLO_SESSION\
                 SET member_id = 0, payedoff = NULL" + " \
                 WHERE trainer_id = " + str(rows[int(option)-1][0]) +" AND dayofweek = '"+ str(rows[int(option)-1][2]) + "' AND starttime = '" + str(rows[int(option)-1][3]) + "' AND endtime = '" + str(rows[int(option)-1][4]) + "';"
        cursor.execute(query)
        print("Solo Session Deleted.")
    
    except:
        # If any errors occur, display error
        print("ERROR: Could not cancel session")



# Cancel Group Booking Handler
def cancelGroup():
    try:
        print()

        # Fetch all available sessions
        query = "SELECT GROUP_SESSION.trainer_id, GROUP_SESSION.member_id, GROUP_SESSION.dayofweek, GROUP_SESSION.starttime, GROUP_SESSION.endtime, GROUP_SESSION.room_no, TRAINERS.first_name, TRAINERS.last_name \
                FROM GROUP_SESSION INNER JOIN TRAINERS ON GROUP_SESSION.trainer_id = TRAINERS.trainer_id\
                WHERE GROUP_SESSION.member_id = " + str(id) + ";"
        cursor.execute(query)
        rows = cursor.fetchall()
        rownum = 0
        
        # Return nothing if no sessions found
        if (len(rows) == 0):
            print("No Group Sessions Booked")
            return
        
        # Display Information of all available sessions to User
        for tup in rows:
            rownum += 1
            print("Session #:", str(rownum) + "\n   Trainer: " + str(tup[6]) + " " + str(tup[7]))
            print("   Day: " + str(tup[2]))
            print("   Start Time: " + str(tup[3]))
            print("   End Time: " + str(tup[4]) + "\n")    

        # Prompt user to book session, checking bounds on the inputs
        option = input("Enter the Session Number you would like to cancel: ")
        while (int(option) < 1 or int(option) > rownum or not option.isnumeric()):
            print("ERROR: Invalid Session Number")
            option = input("Re-Enter the Session Number you would like to cancel: ")
        
        # Update the table to remove the user from the booking
        query = "DELETE FROM GROUP_SESSION \
                WHERE member_id = " + str(id) + " AND trainer_id = " + str(rows[int(option)-1][0]) +" AND dayofweek = '"+ str(rows[int(option)-1][2]) + "' AND starttime = '" + str(rows[int(option)-1][3]) + "' AND endtime = '" + str(rows[int(option)-1][4]) + "';"
        cursor.execute(query)
        print("Group Session Deleted.")
    
    except:
        # If any errors occur, display error
        print("ERROR: Could not cancel session")



# Booking Solo Session Handler
def bookSolo():
    try:
        print()

        # Fetch all available sessions
        query = "SELECT SOLO_SESSION.trainer_id, SOLO_SESSION.member_id, SOLO_SESSION.dayofweek, SOLO_SESSION.starttime, SOLO_SESSION.endtime, TRAINERS.first_name, TRAINERS.last_name \
                 FROM SOLO_SESSION INNER JOIN TRAINERS ON SOLO_SESSION.trainer_id = TRAINERS.trainer_id\
                 WHERE member_id = 0;"
        cursor.execute(query)
        rows = cursor.fetchall()
        rownum = 0

        # Return nothing if no sessions found
        if (len(rows) == 0):
            print("No Solo Sessions Timeslots Available")
            return
        
        # Display Information of all available sessions to User
        for tup in rows:
            rownum += 1
            print("Session #:", str(rownum) + "\n   Trainer: " + tup[5] + " " + tup[6])
            print("   Day: " + tup[2])
            print("   Start Time: " + str(tup[3]))
            print("   End Time: " + str(tup[4]) + "\n")
        
        # Prompt user to book session, checking bounds on the inputs
        option = input("Enter the Session Number you would like to book: ")
        while (int(option) < 1 or int(option) > rownum or not option.isnumeric()):
            print("ERROR: Invalid Session Number")
            option = input("Re-Enter the Session Number you would like to book: ")

        # Update the session to have the user book it
        query = "UPDATE SOLO_SESSION\
                 SET member_id = " + str(id) + ", payedoff = FALSE" + " \
                 WHERE trainer_id = " + str(rows[int(option)-1][0]) +" AND dayofweek = '"+ str(rows[int(option)-1][2]) + "' AND starttime = '" + str(rows[int(option)-1][3]) + "';"
        cursor.execute(query)
        print("Solo Session Booked.")
    
    except:
        # If any errors occur, display error
        print("ERROR: Could not book session")



# Group Booking Handler
def bookGroup():
    try:
        print()

        # Fetch all available sessions
        query = "SELECT GROUP_SESSION.trainer_id, GROUP_SESSION.member_id, GROUP_SESSION.dayofweek, GROUP_SESSION.starttime, GROUP_SESSION.endtime, GROUP_SESSION.room_no, TRAINERS.first_name, TRAINERS.last_name \
                FROM GROUP_SESSION INNER JOIN TRAINERS ON GROUP_SESSION.trainer_id = TRAINERS.trainer_id\
                WHERE member_id = 0;"
        cursor.execute(query)
        rows = cursor.fetchall()
        rownum = 0

        # Return nothing if no sessions found
        if (len(rows) == 0):
            print("No Group Sessions Timeslots Available")
            return

        # Display Information of all available sessions to User
        for tup in rows:
            rownum += 1
            print("Session #:", str(rownum) + "\n   Trainer: " + str(tup[6]) + " " + str(tup[7]))
            print("   Day: " + str(tup[2]))
            print("   Start Time: " + str(tup[3]))
            print("   End Time: " + str(tup[4]) + "\n")

        # Prompt user to book session, checking bounds on the inputs
        option = input("Enter the Session Number you would like to book: ")
        while (int(option) < 1 or int(option) > rownum or not option.isnumeric()):
            print("ERROR: Invalid Session Number\n")
            option = input("Re-Enter the Session Number you would like to book: ")

        # Update the table to have the user book the session
        query = "INSERT INTO GROUP_SESSION (trainer_id, member_id, dayofweek, starttime, endtime, room_no, payedoff) \
                VALUES (" + str(rows[int(option)-1][0]) + ", " + str(id) + ", '" + str(rows[int(option)-1][2]) + "', '" + str(rows[int(option)-1][3]) + "', '" + str(rows[int(option)-1][4]) + "', " + str(rows[int(option)-1][5]) + ", FALSE);"
        cursor.execute(query)
        print("Group Session Booked.")
    
    except:
        # If any errors occur, display error
        print("ERROR: Could not book session")



# Update Health Metrics Handler
def updateHealthMetrics(height, weight):
    try:
        # Set up queries to update weight
        query = "UPDATE MEMBERS\
                 SET height = " + height + ", targweight = " + weight + " \
                 WHERE username = '" + loggedUser +"';"
        
        # Execute queries
        cursor.execute(query)
        print("Targetted Weight Updated")
    
    except:
        # If any errors occur, display error
        print("ERROR: Could not update")



# Update Weight Handler 
def updateWeight(weight):
    try:
        # Set up queries to update weight
        query = "UPDATE MEMBERS\
                 SET targweight = " + weight + " \
                 WHERE username = '" + loggedUser +"';"
        
        # Execute queries
        cursor.execute(query)
        print("Targetted Weight Updated")
    
    except:
        # If any errors occur, display error
        print("ERROR: Could not update")



# User Registration Handler
def addMember(usr, pwd, fname, lname, card, height, currweight, targweight):
    try:
        # Set up queries to register new MEMBER and new ACCOUNT
        query = "INSERT INTO MEMBERS (first_name, last_name, card_no, height, currweight, targweight, username) \
                VALUES ('" + fname + "', '" + lname + "', " + card + ", " + height + ", " + currweight + ", " + targweight + ", '" + usr + "')"
        query2 = "INSERT INTO ACCOUNTS (username, pass, perms) \
                VALUES ('" + usr + "', '" + pwd + "', 'Members')"
        
        # Execute queries
        cursor.execute(query)
        cursor.execute(query2)
        print("User Registered\n")
    
    except:
        # If any errors occur, display error
        print("ERROR: Could not register. Perhaps Username is already taken?")



# Display Routines for User Handler
def displayRoutines():
    try:
        print()

        # Set up queries to fetch all Routine Information from Solo Sessions
        query = "SELECT SOLO_SESSION.trainer_id, SOLO_SESSION.member_id, SOLO_SESSION.dayofweek, SOLO_SESSION.starttime, SOLO_SESSION.endtime, TRAINERS.first_name, TRAINERS.last_name, TRAINERS.rtine\
                FROM SOLO_SESSION INNER JOIN TRAINERS ON SOLO_SESSION.trainer_id = TRAINERS.trainer_id\
                WHERE SOLO_SESSION.member_id = " + str(id) + ";"
        
        # Execute Query
        cursor.execute(query)
        rows = cursor.fetchall()
        len1 = len(rows)

        # If Query returns a value, Display Information of Solo Sessions of all routines to User
        if (not len1 == 0):
            for tup in rows:
                print("   Trainer: " + str(tup[5]) + " " + str(tup[6]))
                print("   Day: " + str(tup[2]))
                print("   Start Time: " + str(tup[3]))
                print("   End Time: " + str(tup[4]))
                print("   Routine: " + str(tup[7]) + "\n")

        # Set up queries to fetch all Routine Information from Group Sessions
        query = "SELECT GROUP_SESSION.trainer_id, GROUP_SESSION.member_id, GROUP_SESSION.dayofweek, GROUP_SESSION.starttime, GROUP_SESSION.endtime, TRAINERS.first_name, TRAINERS.last_name, TRAINERS.rtine\
                FROM GROUP_SESSION INNER JOIN TRAINERS ON GROUP_SESSION.trainer_id = TRAINERS.trainer_id\
                WHERE GROUP_SESSION.member_id = " + str(id) + ";"
        
        # Execute Query
        cursor.execute(query)
        rows = cursor.fetchall()
        len2 = len(rows)

        # Return nothing if no routines found
        if (len1 == 0 and len2 == 0):
            print("No Routines Set. Book sessions to get routines. ")
            return
        
        # Display Information of Group Sessions of all routines to User
        for tup in rows:
            print("   Trainer: " + str(tup[5]) + " " + str(tup[6]))
            print("   Day: " + str(tup[2]))
            print("   Start Time: " + str(tup[3]))
            print("   End Time: " + str(tup[4]))
            print("   Routine: " + str(tup[7]) + "\n")
    
    except:
        # If any errors occur, display error
        print("ERROR: Couldn't fetch routines")



# Display User Fitness Achievements Handler
def fitnessProgress():
    try:
        print()

        # Set up query to get fitness values for users
        query = "SELECT currweight, targweight\
                FROM MEMBERS\
                WHERE member_id = " + str(id) + ";"
        
        # Execute Queries
        cursor.execute(query)
        rows = cursor.fetchall()

        # Display How far off User is from their desired weight, and whether they need to gain or lose weight
        difference = rows[0][0] - rows[0][1]
        if (difference < 0):
            diff = "gain"
        elif (difference > 0):
            diff = "lose"
        else:
            print("Congratulations, you have met your goal! Perhaps try setting a new one?\n")
        print("You are", str(abs(difference)), "KGs away from your goal, you would need to", diff, "weight\n")

    except:
        # If any error occurs, display error
        print("ERROR: Could not find fitness progress")



# Display Health Metrics Handler
def healthStats():
    try:
        print()

        # Set up query to get Health Metrics information for User
        query = "SELECT height, currweight, targweight\
                FROM MEMBERS\
                WHERE member_id = " + str(id) + ";"
        
        # Execute Queries
        cursor.execute(query)
        rows = cursor.fetchall()

        # Print all Health Metrics for User
        print("   Height (in CMs):", str(rows[0][0]))
        print("   Current Weight (in KGs):", str(rows[0][1]))
        print("   Targetted Weight (in KGs):", str(rows[0][2]))

    except:
        # If error occurs, display message
        print("ERROR: Could not find health statistics")



# Search Member by Name for Trainers Handler
def searchMember():
    try:
        print()

        # Gather user input to run queries on
        fname = input ("\nEnter Member First Name: ")
        lname = input ("Enter Member Last Name: ")

        # Set up query with user input to parse relations
        query = "SELECT *\
                FROM MEMBERS\
                WHERE first_name = '" + fname.lower() + "' AND last_name = '" + lname.lower() + "';"
        
        # Execute Queries
        cursor.execute(query)
        rows = cursor.fetchall()

        # Return nothing if no members found
        if (len(rows) == 0):
            print("No members match this name.")
            return

        # Display Information of all available User Information to Trainer
        for tup in rows:
            print("   Name: " + str(tup[1]) + " " + str(tup[2]))
            print("   Card#: " + str(tup[3]))
            print("   Height: " + str(tup[4]))
            print("   Current Weight: " + str(tup[5]))
            print("   Target Weight: " + str(tup[6]) + "\n")
    
    except:
        # If error occurs, display error 
        print("ERROR: Could not search member")



# Add Group Availability to Trainer Handler
def addGroup():
    try:
        print()

        # Gather user input for Day of Week 
        day = input("What Day would you like to set availability? (Enter sun, mon, tue, wed, thu, fri or sat): ")
        while (day.lower() not in {"sun", "mon", "tue", "wed", "thu", "fri", "sat"}):
            print("ERROR: Invalid Day")
            day = input("Re-Enter What Day would you like to set availability? (Enter sun, mon, tue, wed, thu, fri or sat): ")

        if (day.lower() == "sun"):
            day = "Sunday"
        elif (day.lower() == "mon"):
            day = "Monday"
        elif (day.lower() == "tue"):
            day = "Tuesday"
        elif (day.lower() == "wed"):
            day = "Wednesday"
        elif (day.lower() == "thu"):
            day = "Thursday"
        elif (day.lower() == "fri"):
            day = "Friday"
        elif (day.lower() == "sat"):
            day = "Saturday"
        
        # Gather user input for Start Hour of new Group Session
        starthour = input("Enter the start hour of the new session (2 digits, In 24h format): ")
        while (not len(starthour) == 2 or not starthour.isnumeric() and (int(starthour) < 0 or int(starthour) > 23)):
            print("ERROR: Invalid Hour")
            starthour = input("Re-Enter the start hour of the new session (2 digits, In 24h format): ")

        # Gather user input for Start Minute of new Group Session
        startmin = input("Enter the start minute of the new session (2 digits, In 24h format): ")
        while (not len(startmin) == 2 or not startmin.isnumeric() and (int(startmin) < 0 or int(startmin) > 59)):
            print("ERROR: Invalid Minute")
            startmin = input("Re-Enter the start hour of the new session (2 digits, In 24h format): ")

        # Gather user input for End Hour of new Group Session
        endhour = input("Enter the end hour of the new session (2 digits, In 24h format): ")
        while (not len(endhour) == 2 or not endhour.isnumeric() and (int(endhour) < int(starthour) or int(endhour) > 23)):
            print("ERROR: Invalid Hour")
            endhour = input("Re-Enter the end hour of the new session (2 digits, In 24h format): ")

        # Gather user input for End Minute of new Group Session
        endmin = input("Enter the end minute of the new session (2 digits, In 24h format): ")
        while (not len(endmin) == 2 or not endmin.isnumeric() and (int(endmin) < 0 or int(endmin) > 59)):
            print("ERROR: Invalid Minute")
            endmin = input("Re-Enter the end minute of the new session (2 digits, In 24h format): ")
        
        # Concatenate and Format Hours/Minutes into one string
        start = starthour + ":" + startmin + ":00"
        end = endhour + ":" + endmin + ":00"

        # Gather Room # for Session
        room = input("Enter a Room # (Between 200-205): ")
        while (not room.isnumeric() or (int(room) < 200 or int(room) > 205)):
            print("ERROR: Invalid Room #")
            room = input("Re-Enter a Room # (Between 200-205): ")

        # Set up query to extract all Trainer Solo Timeslots for the Inputted Day to compare/avoid scheduling confilctions
        query = "SELECT SOLO_SESSION.trainer_id, SOLO_SESSION.dayofweek, SOLO_SESSION.starttime, SOLO_SESSION.endtime\
                FROM SOLO_SESSION\
                WHERE SOLO_SESSION.trainer_id = " + str(id) + " AND SOLO_SESSION.dayofweek = '" + day + "';"
        
        # Execute Query
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Compare User Inputted Start/End Times with all Trainer's Start/End Times of Solo Sessions to avoid scheduling conflictions
        for tup in rows:
            if (start == str(tup[2]) or end == str(tup[3]) or ((int(end.replace(':', '')) > int(str(tup[2]).replace(':', ''))) and (int(end.replace(':', '')) < int(str(tup[3]).replace(':', '')))) or ((int(start.replace(':', '')) > int(str(tup[2]).replace(':', ''))) and (int(start.replace(':', '')) < int(str(tup[3]).replace(':', '')))) or (((int(start.replace(':', ''))) < int(str(tup[2]).replace(':', ''))) and ((int(end.replace(':', ''))) > int(str(tup[3]).replace(':', '')))) ):
                print("ERROR: Conflicting Time Slot with Solo Session")
                return False

        # Set up query to extract all Trainer Group Timeslots for the Inputted Day to compare/avoid scheduling confilctions
        query = "SELECT GROUP_SESSION.trainer_id, GROUP_SESSION.dayofweek, GROUP_SESSION.starttime, GROUP_SESSION.endtime\
                FROM GROUP_SESSION\
                WHERE GROUP_SESSION.trainer_id = " + str(id) + " AND GROUP_SESSION.dayofweek = '" + day + "';"
        
        # Execute Query
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Compare User Inputted Start/End Times with all Trainer's Start/End Times of Group Sessions to avoid scheduling conflictions
        for tup in rows:
            if (start == str(tup[2]) or end == str(tup[3]) or ((int(end.replace(':', '')) > int(str(tup[2]).replace(':', ''))) and (int(end.replace(':', '')) < int(str(tup[3]).replace(':', '')))) or ((int(start.replace(':', '')) > int(str(tup[2]).replace(':', ''))) and (int(start.replace(':', '')) < int(str(tup[3]).replace(':', '')))) or (((int(start.replace(':', ''))) < int(str(tup[2]).replace(':', ''))) and ((int(end.replace(':', ''))) > int(str(tup[3]).replace(':', '')))) ):
                print("ERROR: Conflicting Time Slot with Group Session")
                return False
        
        # If no time conflicts occur, update relation to add new group session availability
        query = "INSERT INTO GROUP_SESSION (trainer_id, member_id, dayofweek, starttime, endtime, room_no, payedoff)\
                VALUES\
                (" + str(id) + ", 0, '" + day + "', '" + start + "', '" + end + "', " + str(room) + ", NULL)"
        cursor.execute(query)
        
        print("Group Availability Updated.")
    
    except:
        # If error occurs, display error
        print("ERROR: Could not add new group timeslot")



# Trainer Remove Group Session Handler
def removeGroup():
    try:
        print()

        # Set up Query to parse all trainer's group sessions  
        query = "SELECT GROUP_SESSION.trainer_id, GROUP_SESSION.member_id, GROUP_SESSION.dayofweek, GROUP_SESSION.starttime, GROUP_SESSION.endtime\
                FROM GROUP_SESSION\
                WHERE member_id = 0 AND trainer_id = " + str(id) + ";"
        
        # Execute Query
        cursor.execute(query)
        rows = cursor.fetchall()
        rownum = 0

        # Return nothing if no sessions found
        if (len(rows) == 0):
            print("No Sessions Available")
            return False
            
        # Display Information of all available sessions to User
        for tup in rows:
            rownum += 1
            print("Session #:", str(rownum))
            print("   Day: " + str(tup[2]))
            print("   Start Time: " + str(tup[3]))
            print("   End Time: " + str(tup[4]) + "\n")    
        
        # Prompt user to remove session, checking bounds on the inputs
        option = input("Enter the Session Number you would like to remove: ")
        while (int(option) < 1 or int(option) > rownum or not option.isnumeric()):
            print("ERROR: Invalid Session Number")
            option = input("Re-Enter the Session Number you would like to remove: ")

        # If all goes well, set up query to remove availability
        query = "DELETE FROM GROUP_SESSION\
                WHERE trainer_id = " + str(rows[int(option)-1][0]) +" AND dayofweek = '"+ str(rows[int(option)-1][2]) + "' AND starttime = '" + str(rows[int(option)-1][3]) + "' AND endtime = '" + str(rows[int(option)-1][4]) + "';"
        cursor.execute(query)
        print("Group Availability Updated.")
        return True
    
    except:
        # If error occurs, display error
        print("ERROR: Could not remove Group Session")



# Add Solo Availability to Trainer Handler
def addSolo():
    try:
        print()

        # Gather user input for Day of Week
        day = input("What Day would you like to set availability? (Enter sun, mon, tue, wed, thu, fri or sat): ")
        while (day.lower() not in {"sun", "mon", "tue", "wed", "thu", "fri", "sat"}):
            print("ERROR: Invalid Day")
            day = input("Re-Enter What Day would you like to set availability? (Enter sun, mon, tue, wed, thu, fri or sat): ")

        if (day.lower() == "sun"):
            day = "Sunday"
        elif (day.lower() == "mon"):
            day = "Monday"
        elif (day.lower() == "tue"):
            day = "Tuesday"
        elif (day.lower() == "wed"):
            day = "Wednesday"
        elif (day.lower() == "thu"):
            day = "Thursday"
        elif (day.lower() == "fri"):
            day = "Friday"
        elif (day.lower() == "sat"):
            day = "Saturday"
        
        # Gather user input for Start Hour of new Solo Session
        starthour = input("Enter the start hour of the new session (2 digits, In 24h format): ")
        while (not len(starthour) == 2 or not starthour.isnumeric() and (int(starthour) < 0 or int(starthour) > 23)):
            print("ERROR: Invalid Hour")
            starthour = input("Re-Enter the start hour of the new session (2 digits, In 24h format): ")

        # Gather user input for Start Minute of new Solo Session
        startmin = input("Enter the start minute of the new session (2 digits, In 24h format): ")
        while (not len(startmin) == 2 or not startmin.isnumeric() and (int(startmin) < 0 or int(startmin) > 59)):
            print("ERROR: Invalid Minute")
            startmin = input("Re-Enter the start hour of the new session (2 digits, In 24h format): ")

        # Gather user input for End Hour of new Solo Session
        endhour = input("Enter the end hour of the new session (2 digits, In 24h format): ")
        while (not len(endhour) == 2 or not endhour.isnumeric() and (int(endhour) < int(starthour) or int(endhour) > 23)):
            print("ERROR: Invalid Hour")
            endhour = input("Re-Enter the end hour of the new session (2 digits, In 24h format): ")

        # Gather user input for End Minute of new Solo Session
        endmin = input("Enter the end minute of the new session (2 digits, In 24h format): ")
        while (not len(endmin) == 2 or not endmin.isnumeric() and (int(endmin) < 0 or int(endmin) > 59)):
            print("ERROR: Invalid Minute")
            endmin = input("Re-Enter the end minute of the new session (2 digits, In 24h format): ")
        
        # Concatenate and Format Hours/Minutes into one string
        start = starthour + ":" + startmin + ":00"
        end = endhour + ":" + endmin + ":00"

        # Gather Room # for Session
        room = input("Enter a Room # (Between 200-205): ")
        while (not room.isnumeric() or (int(room) < 200 or int(room) > 205)):
            print("ERROR: Invalid Room #")
            room = input("Re-Enter a Room # (Between 200-205): ")

        # Set up query to extract all Trainer Solo Timeslots for the Inputted Day to compare/avoid scheduling confilctions
        query = "SELECT SOLO_SESSION.trainer_id, SOLO_SESSION.dayofweek, SOLO_SESSION.starttime, SOLO_SESSION.endtime\
                FROM SOLO_SESSION\
                WHERE SOLO_SESSION.trainer_id = " + str(id) + " AND SOLO_SESSION.dayofweek = '" + day + "';"
        
        # Execute Query
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Compare User Inputted Start/End Times with all Trainer's Start/End Times of Solo Sessions to avoid scheduling conflictions
        for tup in rows:
            if (start == str(tup[2]) or end == str(tup[3]) or ((int(end.replace(':', '')) > int(str(tup[2]).replace(':', ''))) and (int(end.replace(':', '')) < int(str(tup[3]).replace(':', '')))) or ((int(start.replace(':', '')) > int(str(tup[2]).replace(':', ''))) and (int(start.replace(':', '')) < int(str(tup[3]).replace(':', '')))) or (((int(start.replace(':', ''))) < int(str(tup[2]).replace(':', ''))) and ((int(end.replace(':', ''))) > int(str(tup[3]).replace(':', '')))) ):
                print("ERROR: Conflicting Time Slot with Solo Session")
                return False
        
        # Set up query to extract all Trainer Group Timeslots for the Inputted Day to compare/avoid scheduling confilctions
        query = "SELECT GROUP_SESSION.trainer_id, GROUP_SESSION.dayofweek, GROUP_SESSION.starttime, GROUP_SESSION.endtime\
                FROM GROUP_SESSION\
                WHERE GROUP_SESSION.trainer_id = " + str(id) + " AND GROUP_SESSION.dayofweek = '" + day + "';"
        
        # Execute Query
        cursor.execute(query)
        rows = cursor.fetchall()
        
        # Compare User Inputted Start/End Times with all Trainer's Start/End Times of Group Sessions to avoid scheduling conflictions
        for tup in rows:
            if (start == str(tup[2]) or end == str(tup[3]) or ((int(end.replace(':', '')) > int(str(tup[2]).replace(':', ''))) and (int(end.replace(':', '')) < int(str(tup[3]).replace(':', '')))) or ((int(start.replace(':', '')) > int(str(tup[2]).replace(':', ''))) and (int(start.replace(':', '')) < int(str(tup[3]).replace(':', '')))) or (((int(start.replace(':', ''))) < int(str(tup[2]).replace(':', ''))) and ((int(end.replace(':', ''))) > int(str(tup[3]).replace(':', '')))) ):
                print("ERROR: Conflicting Time Slot with Group Session")
                return False
        
        # If no time conflicts occur, update relation to add new solo session availability
        query = "INSERT INTO SOLO_SESSION (trainer_id, member_id, dayofweek, starttime, endtime, room_no, payedoff)\
                VALUES\
                (" + str(id) + ", 0, '" + day + "', '" + start + "', '" + end + "', " + str(room) + ", NULL)"
        cursor.execute(query)
        
        print("Solo Availability Updated.")
    
    except:
        # If error occurs, display error
        print("ERROR: Could not add new solo timeslot")



# Trainer Remove Solo Session Handler
def removeSolo():
    try:
        print()

        # Set up Query to parse all trainer's solo sessions 
        query = "SELECT SOLO_SESSION.trainer_id, SOLO_SESSION.member_id, SOLO_SESSION.dayofweek, SOLO_SESSION.starttime, SOLO_SESSION.endtime\
                FROM SOLO_SESSION\
                WHERE trainer_id = " + str(id) + ";"
        
        # Execute Query
        cursor.execute(query)
        rows = cursor.fetchall()
        rownum = 0

        # Return nothing if no sessions found
        if (len(rows) == 0):
            print("No Sessions Available")
            return False
            
        # Display Information of all available sessions to User
        for tup in rows:
            rownum += 1
            print("Session #:", str(rownum))
            print("   Day: " + str(tup[2]))
            print("   Start Time: " + str(tup[3]))
            print("   End Time: " + str(tup[4]) + "\n")    
        
        # Prompt user to remove session, checking bounds on the inputs
        option = input("Enter the Session Number you would like to remove: ")
        while (int(option) < 1 or int(option) > rownum or not option.isnumeric()):
            print("ERROR: Invalid Session Number")
            option = input("Re-Enter the Session Number you would like to remove: ")

         # If all goes well, set up query to remove availability
        query = "DELETE FROM SOLO_SESSION\
                WHERE trainer_id = " + str(rows[int(option)-1][0]) +" AND dayofweek = '"+ str(rows[int(option)-1][2]) + "' AND starttime = '" + str(rows[int(option)-1][3]) + "' AND endtime = '" + str(rows[int(option)-1][4]) + "';"
        cursor.execute(query)

        print("Solo Availability Updated.")
        return True
    
    except:
        # If error occurs, display error
        print("ERROR: Could not remove Solo Session")
    


# Update Personal Information Handler
def updatePersonalInfo(fname, lname, card):
    try:
        # Set up queries to update member information
        query = "UPDATE MEMBERS\
                SET first_name = '" + fname + "', last_name = '" + lname + "', card_no = " + card + " \
                WHERE username = '" + loggedUser +"';"
        
        # Execute queries
        cursor.execute(query)
        print("Personal Information Updated")
    
    except:
        # If any errors occur, display error
        print("ERROR: Could not update")



# User Login Handling
def login(user, passwd):
    global loggedUser
    global perms
    global id

    # Checking for user/pass combination
    try:
        cursor.execute("SELECT * FROM ACCOUNTS WHERE username = '" + user + "' AND pass = '" + passwd +"'")
        rows = cursor.fetchall()
        for tup in rows:

            # If match is found, then store user information for future authentication
            if (tup[0] == user and tup[1] == passwd):

                # Store username and permissions
                loggedUser = user
                perms = tup[2]
                print("Logged in as", loggedUser)

                if (perms == 'Members'):
                    # Store member id
                    cursor.execute("SELECT member_id FROM MEMBERS WHERE username = '" + loggedUser + "';")
                    rows = cursor.fetchall()
                    id = rows[0][0]

                elif (perms == 'Trainers'):
                    # Store member id
                    cursor.execute("SELECT trainer_id FROM TRAINERS WHERE username = '" + loggedUser + "';")
                    rows = cursor.fetchall()
                    id = rows[0][0]

                return True
            
        # Otherwise, return error
        print("ERROR: Incorrect Username or Password")
        return False
    
    except:
        # If any errors occur, display error
        print("ERROR: Could not Login")
        return False

def bookRoom():
    try:
        room_no = input("Enter the room number: ")
        day = input("Enter the day (e.g., 'Monday'): ")
        start_time = input("Enter the start time (HH:MM): ")
        end_time = input("Enter the end time (HH:MM): ")
        purpose = input("Enter the purpose of the booking: ")

        # Check if the room is available
        query = f"SELECT * FROM ROOM_BOOKINGS WHERE room_no = {room_no} AND day = '{day}' AND NOT (end_time <= '{start_time}' OR start_time >= '{end_time}')"
        cursor.execute(query)
        if cursor.fetchone():
            print("Room is not available for the specified time.")
            return
        # Book the room
        query = f"INSERT INTO ROOM_BOOKINGS (room_no, day, start_time, end_time, purpose) VALUES ({room_no}, '{day}', '{start_time}', '{end_time}', '{purpose}')"
        cursor.execute(query)
        print("Room booked successfully.")
    except Exception as e:
        print("Error booking room:", e)

def viewRoomBookings():
    query = "SELECT booking_id, room_no, day, start_time, end_time, purpose FROM ROOM_BOOKINGS"
    cursor.execute(query)
    rooms = cursor.fetchall()
    rownum=0
    print("All current bookings:" + "\n")
    print("======================")
    for tup in rooms:
        rownum += 1
        print(" Booking Id:", str(tup[0])) 
        print(" Room Number:" + str(tup[1])) 
        print(" Day:" + str(tup[2]))
        print(" StartTime:" + str(tup[3]))
        print(" EndTime:" + str(tup[4])) 
        print(" Purpose:" + str(tup[5]))
        print("======================")

def deleteRoomBooking():
    query = "SELECT booking_id, room_no, day, start_time, end_time, purpose FROM ROOM_BOOKINGS"
    cursor.execute(query)
    rooms = cursor.fetchall()
    rownum=0
    print("All current bookings:" + "\n")
    print("======================")
    for tup in rooms:
        rownum += 1
        print(" Booking Id:", str(tup[0])) 
        print(" Room Number:" + str(tup[1])) 
        print(" Day:" + str(tup[2]))
        print(" StartTime:" + str(tup[3]))
        print(" EndTime:" + str(tup[4])) 
        print(" Purpose:" + str(tup[5]))
        print("======================")
# Prompt user to book session, checking bounds on the inputs
    option = input("Enter the Booking you would like to cancel by typing the ID: ")
    # Update the table to remove the user from the booking
    cursor.execute('''DELETE FROM ROOM_BOOKINGS WHERE booking_id=%s''', (option))
    print("Group Session Deleted.")

def equipmentMonitoring(equipment):
    print()
    if (equipment=='1'):
        equipment = "treadmill"
    if (equipment=='2'):
        equipment = "benchpress"
    if (equipment=='3'):
        equipment = "squatrack"
    if (equipment=='4'):
        equipment = "ellyptical"
    query = f"SELECT num FROM ROOMS WHERE {equipment} = TRUE;"
    try:
        cursor.execute(query)
        rooms = cursor.fetchall()
        if rooms:
            print(f"Rooms with a {equipment} availible:")
            for room in rooms:
                print(room[0])
        else:
            print(f"No rooms found with a {equipment} available.")
    except Exception as e:
        print("An error occurred:", e)
        
def payOffSolo():
    print("Which solo session would you like to charge for (type the session #)?\n")
    query = "SELECT trainer_id, member_id, dayofweek, starttime, endtime FROM SOLO_SESSION WHERE payedoff = FALSE OR payedoff IS NULL;"

    try:
        cursor.execute(query)
        sessions = cursor.fetchall()
        if sessions:
            print("Unpaid Solo Sessions:")
            print("======================")
            for index, session in enumerate(sessions):
                print(f" Session #{index + 1}:")
                print(f" Trainer ID: {session[0]}")
                print(f" Member ID: {session[1]}")
                print(f" Day: {session[2]}")
                print(f" Start Time: {session[3]}")
                print(f" End Time: {session[4]}")
                print("======================")

            option = int(input("Enter the session number you would like to charge for: ")) - 1
            if 0 <= option < len(sessions):
                selected_session = sessions[option]
                query = "UPDATE SOLO_SESSION\
                         SET payedoff = TRUE" + " \
                         WHERE trainer_id = " + str(sessions[int(option)-1][0]) +" AND dayofweek = '"+ str(sessions[int(option)-1][2]) + "' AND starttime = '" + str(sessions[int(option)-1][3]) + "' AND endtime = '" + str(sessions[int(option)-1][4]) + "';" #AND payedoff=false
                cursor.execute(query)
                print("Session marked as paid successfully.")
            else:
                print("Invalid session number entered.")
        else:
            print("No unpaid solo sessions found.")
    except Exception as e:
        print("An error occurred:", e)

def payOffGroup():
    print("Which group session would you like to charge for (type the session #)?\n")
    query = "SELECT trainer_id, member_id, dayofweek, starttime, endtime FROM GROUP_SESSION WHERE payedoff = FALSE OR payedoff IS NULL;"

    try:
        cursor.execute(query)
        sessions = cursor.fetchall()
        if sessions:
            print("Unpaid Group Sessions:")
            print("======================")
            for index, session in enumerate(sessions):
                print(f" Session #{index + 1}:")
                print(f" Trainer ID: {session[0]}")
                print(f" Member ID: {session[1]}")
                print(f" Day: {session[2]}")
                print(f" Start Time: {session[3]}")
                print(f" End Time: {session[4]}")
                print("======================")

            option = int(input("Enter the session number you would like to charge for: ")) - 1
            if 0 <= option < len(sessions):
                selected_session = sessions[option]
                query = "UPDATE GROUP_SESSION\
                         SET payedoff = TRUE" + " \
                         WHERE trainer_id = " + str(sessions[int(option)-1][0]) +" AND dayofweek = '"+ str(sessions[int(option)-1][2]) + "' AND starttime = '" + str(sessions[int(option)-1][3]) + "' AND endtime = '" + str(sessions[int(option)-1][4]) + "';" #need to fix this asap have to add the payedoff=false
                cursor.execute(query)
                print("Session marked as paid successfully.")
            else:
                print("Invalid session number entered.")
        else:
            print("No unpaid group sessions found.")
    except Exception as e:
        print("An error occurred:", e)

def addTrainer():
    fname = input("What is the trainer's first name: ")
    lname = input("What is the trainer's last name: ")
    rtine = input("What is the trainer's routine: ")
    usr = input("What is the trainer's username: ")
    pwd = '12345'
    query = "INSERT INTO TRAINERS (first_name, last_name, rtine, username) VALUES (%s, %s, %s, %s)"
    query2 = "INSERT INTO ACCOUNTS (username, pass, perms) VALUES (%s, %s, %s)"

    try:
        # Execute the first query to insert the trainer
        cursor.execute(query, (fname, lname, rtine, usr))
        print("Trainer registered in TRAINERS table.")

        # Execute the second query to insert the account details
        cursor.execute(query2, (usr, pwd, 'Trainers'))
        print("Trainer's account created in ACCOUNTS table.")

        # Commit the changes to the database
        cursor.connection.commit()
        print("All changes committed to the database.")

    except Exception as e:
        # If there is any error, rollback the transaction
        cursor.connection.rollback()
        print("Transaction rolled back due to an error:", e)
    

def viewSessions():
    print("GROUP SESSIONS: ")
    query = "SELECT trainer_id, member_id, dayofweek, starttime, endtime FROM GROUP_SESSION;"
    cursor.execute(query)
    sessions = cursor.fetchall()
    if sessions:
        print("Group Sessions:")
        print("======================")
        for index, session in enumerate(sessions):
            print(f" Session #{index + 1}:")
            print(f" Trainer ID: {session[0]}")
            print(f" Member ID: {session[1]}")
            print(f" Day: {session[2]}")
            print(f" Start Time: {session[3]}")
            print(f" End Time: {session[4]}")
            print("======================")

    print("SOLO SESSIONS: ")
    query = "SELECT trainer_id, member_id, dayofweek, starttime, endtime FROM SOLO_SESSION;"
    cursor.execute(query)
    sessions = cursor.fetchall()
    if sessions:
        print("Solo Sessions:")
        print("======================")
        for index, session in enumerate(sessions):
            print(f" Session #{index + 1}:")
            print(f" Trainer ID: {session[0]}")
            print(f" Member ID: {session[1]}")
            print(f" Day: {session[2]}")
            print(f" Start Time: {session[3]}")
            print(f" End Time: {session[4]}")
            print("======================")

# Main Code
def main():

    # Prompt primary loop
    while(1):

        # Ask user to login/register
        print("\nWhat would you like to do? (Enter 0, 1 or 2)\n    1. Login\n    2. Register New Member\n    0. Exit\n")
        option = input()

        # Quit if entered 0
        if(option == '0'):
            print("Saving and quitting...\n")
            break
        
        # Otherwise, prompt username and password to login (0 to quit)
        while(option == '1'):
            username = input("\nUsername (Enter 0 to quit): ")
            if (username == '0'):
                break
            password = input("Password (Enter 0 to quit): ")
            if (password == '0'):
                break
            log = login(username, password)
            
            # If login successful, then continue to prompt user depending on permissions
            while(log):

                # Display menu for Members
                if(perms == 'Members'):
                    print("\nWhat would you like to do? (Enter 0, 1, 2 or 3)\n    1. Profile Management\n    2. Display Dashboard\n    3. Schedule Class\n    0. Logout\n")
                    option = input()
                    
                    # Logout if user prompts 0
                    if(option == '0'):
                        break

                    # Display menu to update
                    elif(option == '1'):
                        print("\nWhat would you like to Update? (Enter 0, 1, 2 or 3)\n    1. Personal Information\n    2. Targetted Weight\n    3. Health Statistics\n    0. Exit\n")
                        option = input()

                        # Exit if user prompts 0
                        if(option == '0'):
                            continue
                        
                        # If user chooses to update personal information, prompt for new fields
                        elif(option == '1'):
                            fname = input("Enter new first name: ")
                            lname = input("Enter new last name: ")
                            card = input("Enter new card number (9 digits, only integers): ")

                            # Card# has to be less than 9 digits as some inputs exceed max field for integers
                            while (not len(card) == 9 or (not card.isnumeric())):
                                card = input("Re-Enter card number (9 digits, only integers): ")

                            updatePersonalInfo(fname.lower(), lname.lower(), card)
                        
                        # If user chooses to update health goal, prompt for new fields
                        elif(option == '2'):

                            # Weight has to be integer inputs only
                            weight = input("Enter new targetted weight (in KGs, only integers): ")
                            while (not weight.isnumeric()):
                                weight = input("Re-Enter weight (in KGs, only integers): ")

                            updateWeight(weight)
                        
                        # If user chooses to update health metrics, prompt for new fields
                        elif(option == '3'):

                            # Weight has to be integer inputs only
                            height = input("Enter new current height (in CMs, only integers): ")
                            while (not height.isnumeric()):
                                height = input("Re-Enter height (in CMs, only integers): ")
                            
                            # Weight has to be integer inputs only
                            weight = input("Enter new current weight (in KGs, only integers): ")
                            while (not weight.isnumeric()):
                                weight = input("Re-Enter weight (in KGs, only integers): ")                            
                                
                            updateHealthMetrics(height, weight)

                    # Display Dashboard Menu
                    elif (option == '2'):
                        print("\nWhat would you like to do? (Enter 0, 1, 2 or 3)\n    1. Displaying Exercise Routines\n    2. Fitness Progress\n    3. Health Statistics\n    0. Exit\n")
                        option = input()

                        # If user requests, return to previous menu
                        if (option == '0'):
                            continue

                        # Display trainer assigned routines
                        if (option == '1'):
                            displayRoutines()    

                        # Display fitness achievements
                        if (option == '2'):
                            fitnessProgress()  

                        # Display health statistics
                        if (option == '3'):
                            healthStats()  

                    # Display Scheduling Menu
                    elif (option == '3'):
                        print("\nWhat would you like to do? (Enter 0, 1, 2 or 3)\n    1. Book Session\n    2. Cancel Session\n    3. Reschedule Session\n    0. Exit")
                        option = input()

                        # If user requests, return to previous menu
                        if (option == '0'):
                            continue
                        
                        # Prompt user to book new session
                        elif (option == '1'):
                            print("\nWhat Type of Session would you like to book? (Enter 0, 1 or 2)\n    1. Solo Session\n    2. Group Session\n    0. Exit\n")
                            newOption = input()

                            # Return to previous menu
                            if (newOption == '0'):
                                continue
                            
                            # Book new Solo Session
                            elif (newOption == '1'):
                                bookSolo()
                            
                            # Book new Group Session
                            elif (newOption == '2'):
                                bookGroup()

                        # Prompt user to cancel session
                        elif (option == '2'):
                            print("\nWhat Type of Session would you like to cancel? (Enter 0, 1 or 2)\n    1. Solo Session\n    2. Group Session\n    0. Exit\n")
                            newOption = input()

                            # Return to previous menu
                            if (newOption == '0'):
                                continue
                            
                            # Cancel Solo Session
                            elif (newOption == '1'):
                                cancelSolo()

                            # Cancel Group Session
                            elif (newOption == '2'):
                                cancelGroup()

                        # Prompt user to reschedule session
                        elif (option == '3'):
                            print("\nWhat Type of Session would you like to reschedule? (Enter 0, 1 or 2)\n    1. Solo Session\n    2. Group Session\n    0. Exit\n")
                            newOption = input()

                            # Return to previous menu
                            if (newOption == '0'):
                                continue
                            
                            # Reschedule Solo Session
                            elif (newOption == '1'):
                                cancelSolo()
                                bookSolo()

                            # Reschedule Group Session
                            elif (newOption == '2'):
                                cancelGroup()
                                bookGroup()

                # Display menu for Trainers
                elif(perms == 'Trainers'):
                    print("\nWhat would you like to do? (Enter 0, 1 or 2)\n    1. Schedule Management\n    2. Member Search\n    0. Exit\n")
                    option = input()

                    # Return to previous menu
                    if(option == '0'):
                        break
                    
                    # Manage Schedule for Trainer
                    if(option == '1'):
                        print("\nHow would you like to modify your availability? (Enter 0, 1, 2 or 3)\n    1. Add Timeslot\n    2. Remove Timeslot\n    3. Reschedule Timeslot\n    0. Exit\n")
                        option = input()

                        # Return to previous menu
                        if (option == '0'):
                            continue

                        # Prompt user to add Solo or Group session
                        elif (option == '1'):
                            print("\nWould you like to add a Solo Session or a Group Session? (Enter 0, 1 or 2)\n    1. Solo Session\n    2. Group Session\n    0. Exit\n")
                            option = input()

                            # Return to previous menu
                            if (option == '0'):
                                continue

                            # Add Solo Session
                            if (option == '1'):
                                addSolo()

                            # Add Group Session
                            if (option == '2'):
                                addGroup()

                        # Prompt user to remove Solo or Group session
                        elif (option == '2'):
                            print("\nWould you like to remove a Solo Session or a Group Session? (Enter 0, 1 or 2)\n    1. Solo Session\n    2. Group Session\n    0. Exit\n")
                            option = input()

                            # Return to previous menu
                            if (option == '0'):
                                continue
                            
                            # Remove Solo Session
                            if (option == '1'):
                                removeSolo()

                            # Remove Group Session
                            if (option == '2'):
                                removeGroup()
                        
                        # Prompt user to reschedule Solo or Group session
                        elif (option == '3'):
                            print("\nWould you like to reschedule a Solo Session or a Group Session? (Enter 0, 1 or 2)\n    1. Solo Session\n    2. Group Session\n    0. Exit\n")
                            option = input()

                            # Return to previous menu
                            if (option == '0'):
                                continue

                            # Reschedule Solo Session (If session exists to reschedule)
                            if (option == '1'):
                                check = removeSolo()
                                if (check):
                                    addSolo()
                                
                            # Reschedule Group Session (If session exists to reschedule)
                            if (option == '2'):
                                check = removeGroup()
                                if (check):
                                    addGroup()

                    # Search Member by Name
                    elif(option == '2'):
                        searchMember()

                    
                # Display menu for Admin
                elif(perms == "Admin"):

                    print("\nWhat would you like to do? (Enter 0, 1, 2, 3, or 4)\n    1. Room Booking Management\n    2. Equipment Monitoring\n    3. Update Classes\n    4. Payment Processing\n    0. Exit\n")
                    option = input()
                    if(option == '0'):
                        break
                    elif(option == '1'):
                        print("\nWould you like to add a room booking, delete a room booking, or check all the bookings currently in the system? (Enter 0, 1, 2, or 3)\n    1. Add Booking\n    2. Delete Booking\n    3. View Bookings\n    0. Exit\n")
                        option = input()

                            # Return to previous menu
                        if (option == '0'):
                            continue

                            # Reschedule Solo Session (If session exists to reschedule)
                        if (option == '1'):
                            bookRoom()
                        if (option == '2'):
                            deleteRoomBooking()
                        if (option == '3'):
                            viewRoomBookings()
                    
                    elif(option == '2'):
                        print("\nWhich piece of equipment status would you like to check? (Enter 0, 1, 2, 3, or 4)\n   1. Treadmill\n    2. Benchpress\n    3. Squatrack\n    4. Ellyptical\n    0. Exit\n")
                        option = input()
                        equipmentMonitoring(option)

                    elif(option == '3'):
                        print("\nChoose which function pertaining to a certain class/session feature you'd like to perform?\n    1. Add a Trainer\n    2. View all available sessions\n    0. Exit")
                        option = input()
                        if(option=="1"):
                            addTrainer()
                        elif(option=="2"):
                            viewSessions()
                        elif(option=="3"):
                            continue
                            

                    elif(option == '4'):
                        print("\nWhich type of sessions would you like to charge for? \n    1. Solo\n    2. Group\n    0. Exit")
                        option = input()
                        if (option == '1'):
                            payOffSolo()
                        if (option == '2'):
                            payOffGroup()
                        if (option == '0'):
                            continue
        
        # If entered 2, prompt for user information
        if (option == '2'):
            usr = input("Enter Username: ")
            pwd = input("Enter Password: ")
            fname = input("Enter First Name: ")
            lname = input("Enter Last Name: ")

            # Card# has to be less than 9 digits as some inputs exceed max field for integers
            card = input("Enter Credit Card # (9 digits, only integers): ")
            while (not len(card) == 9 or (not card.isnumeric())):
                card = input("Re-Enter Credit Card # (9 digits, only integers): ")
            
            # Height has to be integer inputs only
            height = input("Enter Height (in CMs, only integers): ")
            while (not height.isnumeric()):
                height = input("Re-Enter Height (in CMs, only integers): ")
            
            # Current Weight has to be integer inputs only
            currweight = input("Enter Current Weight (in KGs, only integers): ")
            while (not currweight.isnumeric()):
                currweight = input("Re-Enter Current Weight (in KGs, only integers): ")

            # Target Weight has to be integer inputs only
            trgweight = input("Enter Target Weight (in KGs, only integers): ")
            while (not trgweight.isnumeric()):
                trgweight = input("Re-Enter Target Weight (in KGs, only integers): ")

            # Add member to table
            addMember(usr, pwd, fname.lower(), lname.lower(), card, height, currweight, trgweight)

    # Closing connections
    connect.commit()
    connect.close()



# Error checking
try:
      # Connecting to database  #CHANGE THE PASSWORD BASED ON UR DATABASE AND THE DATABASE NAME
      connect = psycopg2.connect(database = "fitness", user = "postgres", password = "Abaseen1", host = "127.0.0.1", port = "5432")
      cursor = connect.cursor()

      # Run program
      main()

except:
      # Report error to user
      print("Quitting...\n")