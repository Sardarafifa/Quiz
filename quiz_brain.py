class QuizBrain:
    def __init__(self,questionlist):
        self.question_number=0
        self.score=0
        self.questionlist=questionlist
    def next_question(self):
        current_question=self.questionlist[self.question_number]
        self.question_number+=1
        useranswer=input(f"Q.{self.question_number} {current_question.text} is (True/False)?")
        self.check_answer(useranswer,current_question.answer)

    def still_has_questions(self):
        return self.question_number<len(self.questionlist)
    
    def check_answer(self,useranswer,correctanswer):
        if useranswer.lower()==correctanswer.lower():
            self.score+=1
            print("Yay! That's right")
        else:
            print("Ohho! That's wrong")
        print(f"The correct answer was {correctanswer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")


    



