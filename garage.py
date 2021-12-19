import os
import sys
from main import Menu as m
import diller as d

class Mycar():

    car_name = d.Cars.default.name
    car_power = d.Cars.default.power
    car_weight = d.Cars.default.weight
    car_tyres = d.Cars.default.tires
    print('you are in garage!!!\nyou have 1 car :\nname =',car_name,'\npower =',car_power,'\nweight =',car_weight,'\ntyres =',car_tyres)
    def __init__(self):
        while True:
          c =  input("input your command here -> ")
          if c:break
        if c=="help":
             print(m.all_commands_g(self))
             Mycar.__init__(self)
        if c=='r':

            input()
        if c == 'd':
            input()
        if c=='f':
            input()
        if c =='s':
            input()
        if c =='m':
             os.startfile('start.py')
             sys.exit()

        if c == 'gr':
            input()





a=Mycar()
input()
