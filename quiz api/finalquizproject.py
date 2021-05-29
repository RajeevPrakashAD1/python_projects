from main import Question
from question import data
from tk import Quizzgui
questionbank=[]

for i in data:
    ques = i["question"]
    ans = i["correct_answer"]
    p = Question(ques,ans)
    questionbank.append(p)

from brainquizz import Brainquizz
quiz = Brainquizz(questionbank)
window = Quizzgui(quiz)

