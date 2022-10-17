class Character():
    print("Welcome to Mario World <3")
    x=input("press 0 to start\n")
    if (x=="0"):
        def __init__(self,name):
            self.name = name
            self.__life = 3
            self.__score = 0

        def kicked(self):
            self.__score+=10

        def punched(self):
            self.__score+=5

        def stabbed(self):
            self.__life-=1

        def displaylife(self):
            return self.__life
        
        def displayscore(self):
            return self.__score

        def intro(self):
            print(f"Name : {self.name}")
            print(f"Score : {self.__score}")
            print(f"Life : {self.__life}")

mario=Character("Mario")
abc=True
while(abc):
    z=input("""Press
            i = To check info
            f = To Kick, (5 Pts)
            g = To Punch (10 Pts)
            h = To Stab (1 Life reduced)\n""")
    
    if(z=="i"):
        mario.intro()
    elif(z=="f"):
        mario.kicked()
    elif(z=="g"):
        mario.punched()    
    elif(z=="h"):
        mario.stabbed()
    else:
        print("choose valid option")
        
    value=mario.displaylife()
    if(value==0):
        print ("Game Over!!!")
        n=int(input("press 1 to restart :"))
        if(n==1):
            mario=Character("Mario")
        else:
            abc=False
            exit()
