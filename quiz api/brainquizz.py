
import html
class Brainquizz():




    def __init__(self,qlist):
        self.qn = 0
        self.score = 0

        self.ql = qlist

    def nextquestion(self):
        self.qn += 1
        import sys
        if self.qn>9:
            return ("false","false")
        else:

            question_to_display  = html.unescape(self.ql[self.qn].text)
            anss = self.ql[self.qn - 1].answer
            return  (question_to_display,anss)


        # new = input(f"Q.{self.qn}   {se} (True/False): ")
        # anss = self.ql[self.qn -1].answer

        # print("this is your ans",new)
        # print("this is right answer",anss)
        # if new == anss:
        #     self.score = self.score+1
        # elif new == "off":
        #     sys.exit()
        # print("your score" ,self.score)
    def check(self,answer):
        anss = self.ql[self.qn - 1].answer

        if answer == anss:
            self.score +=1
            return True
        else:

            return False



