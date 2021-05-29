from main import Question
from question import data
questionbank=[]
for i in data:
    ques = i["question"]
    ans = i["correct_answer"]
    p = Question(ques,ans)
    questionbank.append(p)

from brainquizz import Brainquizz
quiz = Brainquizz(questionbank)
for i in range(len(data)):
    print(quiz.nextquestion())
