questions =("How many continents are there? ",
            "What is the capital of India? ",
            "What is the currency of Japan? ",
            "Which planet is known as the Red Planet? ",
            "Who wrote 'Romeo and Juliet'? ")
options = (("A. Four ", "B. Five ", "C. Six ", "D. Seven"),
           ("A. Mumbai ", "B. Chennai ", "C. New Delhi ", "D. Kolkata"),
           ("A. Yen ", "B. Dollar ", "C. Euro ", "D. Rupee"),
           ("A. Earth ", "B. Mars ", "C. Jupiter ", "D. Saturn"),
           ("A. Shakespeare ", "B. Dickens ", "C. Austen ", "D. Twain"))
answers = ("D", "C", "A", "B", "A")
guesses =[]
score = 0
question_num = 0
for question in questions :
    print ("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B , C, D):").upper() #Incase user enters lowercase
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1

print ("--------------------------")
print("RESULTS")
print ("--------------------------")

print("Answers are : ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Guesses : ",end="")
for guess in guesses :
    print(guess,end=" ")
print()

score = (score/ len(answers))*100
print(f"Your Score is : {score}%")