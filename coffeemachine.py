'''  lets do it'''
print ('cofffe machine')
import sys
water=7000
coffee=1000
sugar=2000  
while water>0 and sugar>0 and coffee>0:

    print("what you wanna drink  for expresso chooose(e),for cuppinno choose (c),for latte choose(l) ")


    ui=input("choose : ")
    if ui=="report":
        print("water capacity:",water )
        print("sugar capacity:",sugar )
        print("coffee capacity:",coffee )
    elif ui=="off":
        sys.exit()   
    else:



        print("select coins")
        t=int(input("ten rupee coin : "))
        f=int(input("five rupee coin: "))
        tw=int(input("two rupee coin: "))
        o=int(input("one rupee coin: "))
        coe=50
        col=40
        coc=30
        tc= t*10+f*5+tw*2+o*1
        print("total amount you paid :",tc)

        

        
        if ui=="e":
            if coe>tc:
                print("insufficient money")
            else:
                water=water-250
                sugar=sugar-50
                coffee=coffee-15
                if water<1 or sugar<1 or coffee<1:
                    print("insufficient material")
                    print("money refunded")
                    water=water+250
                    sugar=sugar+50
                    coffee=coffee+15
                else:   
                    print("you hot coffee is ready")
                    print("THANKYOU")
                    mr=tc-coe
                    print("money returned",mr)
                
        elif ui=="c":
            if coc>tc:
                print("insufficient money")
            else:
                water=water-300
                sugar=sugar-80
                coffee=coffee-30
                if water<1 or sugar<1 or coffee<1:
                    print("insufficient material")
                    print("money refunded")
                    water=water+300
                    sugar=sugar+80
                    coffee=coffee+30
                else:   
                    print("you hot coffee is ready")
                    print("THANKYOU")
                    mr=tc-coe
                    print("money returned",mr)
        elif ui=="l":
            if col>tc:
                print("insufficient money")
            else:
                water=water-350
                sugar=sugar-80
                coffee=coffee-20
                if water<1 or sugar<1 or coffee<1:
                    print("insufficient material")
                    print("money refunded")
                    water=water+350
                    sugar=sugar+80
                    coffee=coffee+20
                else:   
                    print("you hot coffee is ready")
                    print("THANKYOU")
                    mr=tc-coe
                    print("money returned",mr)
                        



        


