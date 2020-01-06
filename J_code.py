#python3 Group project
#Ana Inacio, Jason Polanco, Justin
#11/4/2019
#This program is a Disney Quiz game

#Define main
def main():
    #Intro
    print("\nWelcome to the Disney Quiz Game")
    #prompt for name 
    name = input("\nEnter your name:")
    print("\nLets have fun", name)
    
    
    try:
        #Declare and Initialize Variables
        fileNameIn = "disney1.txt"
        fileNameOut = "highscores.txt"
        infileList = []
        questionList = []
        userAnswer = ""
        answer = ""
        totalPoints = 0
        index= 0
        
        #Open file and read in all lines to a list
        infile = open(fileNameIn,'r')
        infileList = infile.readlines(-1) 
        infile.close()
        
        #Use a for loop to convert each line into a list, using split function to separate question, options, and final answers
        
        for i in infileList:
            questionList = i.split("|")
            
            #The last position in the list is always the answer
            answer = questionList[-1]
            
            #For loop to print out full question and answer options, except for the final answer
            for q in questionList:
                index = index + 1
                if q != answer:
                        print(q)
                 
                #Prompt user for answer
                #Use decision Structures to determine the right entry from the user
                #If user does not enter a valid option, keep asking to enter a valid option
                if index % 6 ==0:
                    userAnswer = input("\nPlease enter a choice:")
                    userAnswerUpper = userAnswer.upper()
                    if userAnswerUpper == "A" or userAnswerUpper == "B" or userAnswerUpper == "C" or  userAnswerUpper == "D":
                        print()
                    else:
                        print("Invalid input, Please, enter a valid option")
                        userAnswer = input("\nPlease enter a choice:")
                        

                #If the answer is correct then add points and say that the answer is correct
                #If the answer is incorrect then say so and show correct answer
            if userAnswer.title() == answer.strip("\n").title():
                print("\nThat is the correct answer.")
                    #addpoints
                totalPoints+=100 
                print("You have earned a total of",totalPoints,"points\n")
            else:
                print("\nThat is the incorrect answer. \nThe correct answer is", answer)

        #read in from text file with highScores 
        fileOut = "highscores.txt"
        disney_outfile = open(fileOut,"r")
        uScore = disney_outfile.readline()
        uName = disney_outfile.readline()
        disney_outfile.close()

        #Write to the file
        #Create a text file with the user's highscore and name
        #use a decision structure to determine if the user got the highscore
        if totalPoints >int(uScore):
            disney_outfile = open(fileOut,"w")
            disney_outfile.write(str(totalPoints)+ "\n")
            uName = input("Enter your name:")
            disney_outfile.write(uName + "\n")

        else:
            print("You do not have the highest score:",uScore )

        print("Thank you for playing this game.")

         
    except:
        print("error")
        main()

main()
