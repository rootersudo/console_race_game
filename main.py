

import os
import time



class Menu():
    print("you are in game!")
    def __init__(self):

        print("Type h to see map commands")
        while True:
            self.a=input("input your command here ->")
            if (self.a) :
                Menu.check_command(self,self.a)
                break
    def check_command(self,a):

        if a == "h":

            print(Menu.all_commands(self))
            Menu.__init__(self)
        if a == "g":
             os.startfile('garage.py')
             SystemExit()


        if a == "d":
            os.startfile("diller.py")
            SystemExit()
        if a == 'exit':
            print("Exiting...")
            time.sleep(3)
            SystemExit()
        if a =='cw':
            print('none')
            Menu.__init__(self)


    def all_commands(self):
        self.c1 = 'go to garage(g)'
        self.c2 = 'go to diller(d)'
        self.c3 = 'go to bank(b)'
        self.c4 = 'go home(gh)'
        self.c5 = 'go to casino(c)'
        self.c7 = 'check your wallet(cw)'
        self.c6 = 'exit'
        return (self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7)


    def all_commands_g(self):
        self.c1 = 'repair (r)'
        self.c2 = 'buy details(d)'
        self.c3 = 'feed your car(f)'
        self.c4 = 'sell your car(s)'
        self.c5 = 'go to map(m)'
        self.c6 = 'go on race(gr)'
        return (self.c1, self.c2, self.c3, self.c4, self.c5)

    def all_commands_d(self):
        self.c1 = 'trade-in (t)'
        self.c2 = 'buy car(c)'
        self.c3 = 'see car(f)'

        self.c5 = 'go to map(m)'

        return (self.c1, self.c2, self.c3, self.c5)



