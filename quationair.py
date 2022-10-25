import pickle   
#survay_name_list =[]
#answers_name_list =[]

   #creat a class of question:
    #deine a method to creat the question
with open('survay_name_list.pkl', 'rb') as file:
    survay_name_list = pickle.load(file)
    file.close()
with open('answers_name_list.pkl', 'rb') as file:
    answers_name_list = pickle.load(file)
    file.close()

def new_question():
        global questions
        name = input('whats the name of ur survay?')
        
        if name in survay_name_list :
            with open(name + '.pkl', 'rb') as file:
                questions =  pickle.load(file)
                file.close()
        else:
            questions = [] 
            survay_name_list.append(name)
        with open('survay_name_list.pkl', 'wb') as file :
            pickle.dump(survay_name_list,file)
            file.close()
            with open(name + '.pkl', 'wb') as file:
                pickle.dump(questions,file)
                file.close()
            with open(name + '.pkl', 'rb') as file :
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

def ask():
        print('here is the list of ongoing survays: ',"\n" ,survay_name_list)
        c = input('which quationiar do you want to answer? ')
        with open(c+'.pkl', 'rb') as file :
            questions = pickle.load(file)
            file.close()  

        if c in answers_name_list :
            with open(c+'answers.pkl', 'rb') as file:
                total_user_answers= pickle.load(file)
                file.close()
        else:
            total_user_answers =[]
            answers_name_list.append(c)
            with open('answers_name_list.pkl','wb') as file:
                pickle.dump(answers_name_list,file)
                file.close()
            with open(c+'answers.pkl', 'wb') as file:
                pickle.dump(total_user_answers,file)
                file.close()
            with open(c+'answers.pkl', 'rb') as file:
                total_user_answers= pickle.load(file)
                file.close()    
                
        for i in range(len(questions)):
            for key,Value in questions[i].items():
                print(key, "  " ,"\n" ,Value)
                answer_of_user= input('what is your choice?')
                que_ans ={i:answer_of_user}
                total_user_answers.append(que_ans)
                i = i + 1
            with open(c+'answers.pkl', 'wb') as file:
                pickle.dump(total_user_answers,file)
                file.close()
   #deine a method to analyse the results
def analays():
        pass

def run_proramm():
    print('what do you wana do? ',"\n" , 
    'to creat a Questionair enter q' ,"\n" ,
    ' or to answer enter a ',"\n" , 
    'or to analyse enter an')
    b = input()
    if b == 'q':
        new_question()
    elif b == 'a':
        ask()
    elif b == 'an':
        analays()
    elif b == 'exit' :
        quit
    else:
        run_proramm()        

run_proramm()
