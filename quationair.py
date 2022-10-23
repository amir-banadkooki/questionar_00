
import pickle
#questions = []
#total_user_answers = []
   
   #creat a class of question:
class question():
    def __init__(self, q , answers ):
        self.q = q
        self.answers = answers
   
    #deine a method to creat the question
    def new_question():
        global questions
        file = open('questions.pkl', 'rb')
        questions = pickle.load(file)
        file.close()
        y = input("Want to add a question? ")
        while  y == 'y' or y == 'Y':
            q = input("question you want to add to your questionair: ")
            number_of_answers = int(input('How many answers does your quetion have?'))
            answers = {}
            for j in range (number_of_answers): 
                answers[j] = input('enter answer')
                j+1
            question = {q: answers}
            questions.append(question)
            y = input("for adding another flashcard, press Y/y :")
            file = open('questions.pkl', 'wb')
            pickle.dump(questions,file)
            file.close()
    
    #deine a method to ask the question
    def ask():
        file = open('questions.pkl', 'rb')
        questions = pickle.load(file)
        file.close()  
        file = open('answers.pkl', 'rb')
        total_user_answers= pickle.load(file)
        file.close()
        for i in range(len(questions)):
            for key,Value in questions[i].items():
                print(key, "  " ,"\n" ,Value)
                answer_of_user= input('what is your choice?')
                que_ans ={i:answer_of_user}
                total_user_answers.append(que_ans)
                i = i + 1
        file = open('answers.pkl', 'wb')
        pickle.dump(total_user_answers,file)
        file.close()
        print(total_user_answers)

   #deine a method to analyse the results
    def analays():
        pass
        
#question.new_question()
#question.ask()
