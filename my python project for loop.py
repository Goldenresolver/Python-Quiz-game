#10-31-19
# A program that is a quiz game
#Declcare and intialize variables
#intro
# read in the quiz questions
#create an accumulation variable
#define main
 
 
def main():
    # Intialize and declare variables
    uName=""
    score=0
    totalpoints=0
    #Intro
    print("Welcome to the Disney Trivia Quiz game!\n")
    print("There are a total of eleven questions worth 100 points each!\n")
    
    # Created the txt file with the questions and answers
    #Read in the txt file
    path="disney.txt"
    disney_file=open(path,"r")

    for data in disney_file:
        print(data)

  
    disney_file.close()
 # Create variables for input choices
 # Attach these choices to their respective list which
 #contain the read in files line by line, which also contains the questions and choices
    question= 0
    option1 = 1
    option2 = 2
    option3 = 3
    option4 = 4
    answer = 5
    totalpoints = 0
    # proceed to display to user the series of questions to questions 1 thru 11
    #ask user questions
    #first question ********************************************************
    print([question],[option1],[option2],[option3],[option4],)

    #prompt user for answer choice from 1 to 11
    user = input("Please enter a choice:")
    
    

    # Use a conditonal statment to determine if user answers correctly to questions 1 thru 11
    if user ==list_1[answer].strip("\n"):
        print("Correct answer\n")
        #add points if user anwsered correctly using an accumluator variable using addition, to questions 1 thru 11
        totalpoints+=100
        print("Current score is",totalpoints)
    # else statment if user answers incorrectly
    else :
        print("incorrect answer\n")
   
    #question 2 ********************************************************

    #print(list_2[question],list_2[option1],list_2[option2],list_2[option3],list_2[option4])
    #user = input("Please enter a choice:")
    
    if user ==list_2[answer].strip("\n"):
        print("Correct answer\n")
        #add points
        totalpoints+=100
        print("Current score is\n",totalpoints)


    else :
        print("incorrect answer\n")
   
    #question 3 ********************************************************
    #print(list_3[question],list_3[option1],list_3[option2],list_3[option3],list_3[option4])
    user = input("Please enter a choice:")
    
    if user ==list_3[answer].strip("\n"):
        print("Correct answer\n")
        #add points
        totalpoints+=100
        print("Current score is",totalpoints)


    else :
        print("incorrect answer\n")
   

     #question 4********************************************************
    #print(list_4[question],list_4[option1],list_4[option2],list_4[option3],list_4[option4])
    user = input("Please enter a choice:")
    
    if user ==list_4[answer].strip("\n"):
        print("Correct answer\n")
        #add points
        totalpoints+=100
        print("Current score is\n",totalpoints)


    else :
        print("incorrect answer\n")



 #question 5********************************************************
    #print(list_5[question],list_5[option1],list_5[option2],list_5[option3],list_5[option4])
    user = input("Please enter a choice:")
    
    if user ==list_5[answer].strip("\n"):
        print("Correct answer\n")
        #add points
        totalpoints+=100
        print("Current score is\n",totalpoints)


    else :
        print("incorrect answer\n")


#question 6********************************************************
    #print(list_6[question],list_6[option1],list_6[option2],list_6[option3],list_6[option4])
    user = input("Please enter a choice:")
    
    if user ==list_6[answer].strip("\n"):
        print("Correct answer\n")
        #add points
        totalpoints+=100
        print("Current score is",totalpoints)


    else :
        print("incorrect answer\n")

#question 7********************************************************
   #print(list_7[question],list_7[option1],list_7[option2],list_7[option3],list_7[option4])
    user = input("Please enter a choice:")
    
    if user ==list_7[answer].strip("\n"):
        print("Correct answer\n")
        #add points
        totalpoints+=100
        print("Current score is\n",totalpoints)


    else :
        print("incorrect answer\n")

#question 8********************************************************
    #print(list_8[question],list_8[option1],list_8[option2],list_8[option3],list_9[option4])
    user = input("Please enter a choice:")
    
    if user ==list_9[answer].strip("\n"):
        print("Correct answer\n")
        #add points
        totalpoints+=100
        print("Current score is\n",totalpoints)

    else :
        print("incorrect answer\n")

#question 9********************************************************
    #print(list_9[question],list_9[option1],list_9[option2],list_9[option3],list_9[option4])
    user = input("Please enter a choice:")
    
    if user ==list_9[answer].strip("\n"):
        print("Correct answer\n")
        #add points
        totalpoints+=100
        print("Current score is\n",totalpoints)


    else :
        print("incorrect answer\n")


#question 10********************************************************
    #print(list_10[question],list_10[option1],list_10[option2],list_10[option3],list_10[option4])
    user = input("Please enter a choice:")
    
    if user ==list_10[answer].strip("\n"):
        print("Correct answer\n")
        #add points
        totalpoints+=100
        print("Current score is\n",totalpoints)


    else :
        print("incorrect answer\n")



#question 11********************************************************
    #print(list_11[question],list_11[option1],list_11[option2],list_11[option3],list_11[option4])
    user = input("Please enter a choice:")
    
    if user ==list_11[answer].strip("\n"):
        print("Correct answer\n")
        #add points
        totalpoints+=100
        print("Current score is\n",totalpoints)


    else :
        print("incorrect answer\n")
#**********************************************************************
    #Display total score to user
    print(totalpoints)
#********************************************************************
# Create another read in highscore .txt file, that contains the recent user's highest score
# Then read in the infomation

    path2="highscore.txt"
    disney_outfile=open(path2,"r")
    #Create variables that contain the info from the read in using .readline()
    uScore= disney_outfile.readline()
    uName= disney_outfile.readline()
    #Close the file after you're done reading 
    disney_outfile.close()

   
#Create a decision structure that detemines if the new total high score is greater than the previous
#total high score then the new score will overtake the previous score if higher by means of writing in the info
# If new score is not higher than previous,then use else statement
    if totalpoints > int(uScore):
        disney_outfile=open(path2,"w")
        disney_outfile.write(str(totalpoints)+"\n")
        uName= input("Please enter your name: ")

        disney_outfile.write(uName+"\n")
        print(str(totalpoints))
        print(uName)

    
    else:
        print("You do not have the highest score")
        


main()
