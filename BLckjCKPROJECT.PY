'''jai mata di'''
print("welcome to black jack 21")

import random
def choosecard():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card= random.choice(cards)
    return card
    
dc1=choosecard()
dc2=choosecard()
pc1=choosecard()
pc2=choosecard()

print("dealer first card",dc1)
print("your first card",pc1)
print("your second card",pc2)

print("choose what you wanna do hit(choose another card),stay(bet)")
ui=input()


if ui=="stay":



    def wtd():
        
        
        
        utv= pc2+pc1
        ctv=dc1+dc2
        while ctv<17:
            ctv=ctv+choosecard()

        if ctv>21:
            print("dealer brust 'YOU WIN'")
        elif ctv<21 and utv == ctv:
            print("DRAW")
        elif utv>21:
            print("you brust'LOOSE'")
        elif utv>ctv:
            print("YOU WIN","your total:",utv,"deale total:",ctv)
        elif ctv>utv:
            print("YOu LOOSE","your total:",utv,"dealer total:",ctv)  
    print(wtd())        
elif ui=="hit":
    if pc1+pc2>21:
        print("you loose YOU BRUST", "your score :",pc1+pc2)
        
    else:
        
        sum1=pc1+pc2
        while ui=="hit" and sum1<22:
            if sum1<22:


                ntc=choosecard()
                print("your next card",ntc)
                sum1=sum1+ntc
                print("your all cards sum ",sum1)
                if sum1>21:
                    '''print("you loose YOU BRUST", "your score :"sum1)'''
                    break

                else:
                    print("choose what you wanna do hit(choose another card),stay(bet)")
                    ui=input()
                
            '''else:
                print("you loose YOU BRUST", "your score :",sum1)'''  
        
                

    def wtd():

        utv=0
        utv=sum1
        ctv=dc1+dc2
        while ctv<17:
            ctv=ctv+choosecard()
        if utv>21:
            print("you brust'LOOSE'")
        elif ctv>21:
            print("dealer brust 'YOU WIN'")
        elif ctv<21 and utv == ctv:
            print("DRAW")
        elif utv>21:
            print("you brust'LOOSE'")
        elif utv>ctv:
            print("YOU WIN","your total:",utv,"deale total:",ctv)
        elif ctv>utv:
            print("YOu LOOSE","your total:",utv,"dealer total:",ctv)  
    wtd()        
else:
    print("you should type all in small letter either stay or hit")
    













'''
if pc1+pc2>21:
    print("you loose YOU BRUST",)
if ui=="hit" and pc1+pc2<=21:
    ntc=choosecard()
    print("your next card",ntc)
    print("your all cards ",pc1,pc2,ntc)


    print("choose what you wanna do hit(choose another card),stay(bet)")
    
    ui2=input()
    if u12=="hit":

            if pc1+pc2+ntc>21:
                print("you loose YOU BRUST",)
            elif ui=="hit" and pc1+pc2+ntc<=21:
                ntc=choosecard()
                print("your next card",ntc)
                print("your all cards ",pc1,pc2,ntc)


                print("choose what you wanna do hit(choose another card),stay(bet)")
        
                ui2=input(hit)

        




    utv= pc2+pc1+choosecard()
    ctv=dc1+dc2
    while ctv<17:
        ctv=ctv+choosecard()

    if ctv>21:
        print("dealer brust 'YOU WIN'")
    elif ctv<21 and utv == ctv:
        print("DRAW")
    elif utv>21:
        print("you brust'LOOSE'")
    elif utv>ctv:
        print("YOU WIN")
    elif ctv>utv:
        print("YOR LOOSE")     '''








