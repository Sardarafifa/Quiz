class Question:
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer

my_question=Question("2+1=3","True")
print(my_question.text)