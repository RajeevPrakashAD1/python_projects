class Brainquizz():


    def __init__(self,qlist):
        self.qn = 0

        self.ql = qlist

    def nextquestion(self):
        import sys
        score = 0
        se = self.ql[self.qn].text
        self.qn += 1
        new = input(f"Q.{self.qn}   {se} (True/False): ")
        anss = self.ql[self.qn -1].answer
        print("input off to exit qizz")
        print("this is your ans",new)
        print("this is right answer",anss)
        if new == anss:
            score = score+1
        elif new == "off":
            sys.exit()
        print("your score" ,score)



