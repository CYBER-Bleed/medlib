    #python quiz game

questions= ("How many cars does mayor own? :",
            "who was the best programmer you met?: ",
            "who created the program python?: ",
            "to whom much is given, much is ?:" ,
            "how skillfull can  solomon be on a scale of 1-10?: ")

options= (("A. 1", "B. 3", "C. 0", "D.4 ","E.8"),
          ("A.solomon ", "B.julian ", "C.bishop ", "D.goodness ","E.abayomi "),
          ("A.tinubu ", "B.ryan ", "C.guiseppe ", "D. none","E.budda "),
          ("A.he don ", "B.required ", "C.needed ", "D.borrowed ","E.dashed "),
          ("A.3 ", "B.6 ", "C.8 ", "D.9 ","E.1 "),)

answers= ("A", "A", "C","D","B", "D")
guesses=[]
score= 0
question_num= 0

for question in questions:
    print(" ........................")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess=input("Enter (A, B, C, D,E): ").upper()
    guesses.append(guess)
    if guess== answers[question_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")


    question_num+=1

print("....................")
print("     RESULTS       ")
 







