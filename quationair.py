import pickle   
#survay_name_list =[]
#questions = []
   #creat a class of question:
    #deine a method to creat the question
def new_question():
        global questions
        
        name = input('whats the name of ur survay?')
        file = open(name + '.pkl', 'wb')
        pickle.dump(questions,file)
        file.close()

        file = open('survay_name_list.pkl', 'rb')
        survay_name_list = pickle.load(file)
        file.close()

        survay_name_list.append(name)
        file = open('survay_name_list.pkl', 'wb')
        pickle.dump(survay_name_list,file)
        file.close()

        file = open(name + '.pkl', 'rb')
        questions =  pickle.load(file)
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
            #print(question)
            y = input("for adding another Question, press Y/y :")
            file = open(name + '.pkl', 'wb')
            pickle.dump(questions,file)
            file.close()
    
    #deine a method to ask the question
def ask():
        c = input('which quationiar do you want to answer? ')
        file = open(c+'.pkl', 'rb')
        questions = pickle.load(file)
        file.close()  
        file = open(c+'answers.pkl', 'rb')
        total_user_answers= pickle.load(file)
        file.close()
        for i in range(len(questions)):
            for key,Value in questions[i].items():
                print(key, "  " ,"\n" ,Value)
                answer_of_user= input('what is your choice?')
                que_ans ={i:answer_of_user}
                total_user_answers.append(que_ans)
                i = i + 1
        file = open(c+'answers.pkl', 'wb')
        pickle.dump(total_user_answers,file)
        file.close()
        #print(total_user_answers)

   #deine a method to analyse the results
def analays():
        pass

def run_proramm():
    b = input('what do you wana do? to creat a Questionair enter q , or to answer enter a or to analyse enter an')
    if b == 'q':
        new_question()
    elif b == 'a':
        ask()
    elif b == 'an':
        analays()
    else:
        run_proramm()        

run_proramm()