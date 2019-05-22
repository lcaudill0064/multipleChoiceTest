import random
import textwrap
class Test():
    def __init__(self, questions, multi_answers, correct_answers, user_answers):
        self.questions = questions
        self.multi_answers = multi_answers
        self.correct_answers = correct_answers
        self.user_answers = user_answers

def studyQs(self):
    questions = self.questions
    count = 0
    file = open("File Path", "r").readlines()
    file = [f.strip() for f in file]
    for num in range(len(file)):
        count += 1
        questions.append(file[num])

    return questions

def multiAs(self):
    multi_answers = self.multi_answers
    multi_holder = []
    count = 0
    file = open("File Path", "r").readlines()
    file = [f.strip() for f in file]
    for num in range(len(file)):
        count += 1
        multi_answers.append(file[num])

    return multi_answers

def take_test(self):
    questions = self.questions
    multi_answers = self.multi_answers
    user_answers = self.user_answers
    count = 0
    multi_holder = []
    while count < len(questions):
        print(textwrap.fill(questions[count]))
        print()
        for i in range(0, len(multi_answers), 4):
            temp = multi_answers[i:i+4]
            random.shuffle(temp)
            multi_holder.append(temp)
        for j in range(len(multi_holder[count])):
            print(textwrap.fill(multi_holder[count][j]))
            print()
        user_input = input(": ")
        if (user_input == "a" or user_input == "b" or user_input == "c" or user_input == "d"):
            user_answers.append(user_input)
        else:
            print("Wrong value!")
            continue
        print()
        print("--------------------------------------------------------------------------------")
        print()
        count += 1

    return user_answers

def correctAs(self):
    correct_answers = self.correct_answers
    count = 0
    file = open("File Path", "r").readlines()
    file = [f.strip() for f in file]
    for num in range(len(file)):
        count += 1
        correct_answers.append(file[num])

    return correct_answers

def verify_test(self):
    questions = self.questions
    multi_answers = self.multi_answers
    user_answers = self.user_answers
    correct_answers = self.correct_answers
    
    count = 1
    correct_total = 0
    total = 0
    for num in range(len(user_answers)):
        if user_answers[num] == correct_answers[num]:
            print("Question",count,"is correct!")
            print()
            print("----------------------------------------------")
            correct_total += 1
        else:
            print("Question",count,"is incorrect!")
            print(questions[num])
            print("Your answer: ",user_answers[num])
            print("Correct answer: ",correct_answers[num])
            print()
            print("----------------------------------------------")
        count += 1
        total += 1
        
    score = correct_total / total
    score = int(score * 100)
    print()
    if 75 <= score <= 79:
        print("You passed with a C!")
        print("You scored: ",score,"%",sep='')
    elif 80 <= score <= 89:
        print("You passed with a B!")
        print("You scored: ",score,"%",sep='')
    elif 90 <= score <= 99:
        print("You passed with an A!")
        print("You scored: ",score,"%",sep='')
    elif score == 100:
        print("You got a perfect score!")
        print("Congrats!")
        print("You scored: ",score,"%",sep='')
    else:
        print("You failed!")
        print("You scored: ",score,"%",sep='')

def main():
    option = ""
    while option != "end":
        try:
            if option == "end":
                break
            
            questions = []
            multi_answers = []
            correct_answers = []
            user_answers = []
            test = Test(questions, multi_answers, correct_answers, user_answers)
            studyQs(test)
            multiAs(test)
            take_test(test)
            correctAs(test)
            verify_test(test)

            option = input("Try again? 'yes' to continue or 'end' to break\n")
        except ValueError:
            pass
main()
