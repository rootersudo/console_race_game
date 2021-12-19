from main import Menu as m

class Cars():
    print("you are at diller centre!")
    print("type h to see commands")
    def __init__(self):

        while True:
            a = input("input your command her -> ")
            Cars.check(self,a)
            break
    def check(self,a):
        C = Cars
        if a == 'h':
            print(m.all_commands_d(self))
            C.__init__(self)
        if a == 'f':
            b=input("what type of car do you want? (1/2/3) -> ")
            C = Cars
            if b =='1':
                print(C.DG_car1.name, "( to choose type dg )\n", C.BWM_car1.name, "( to choose type bwm )\n",
                      C.MCD_car1.name,
                      "( to choose type mcd )\n", C.TRD_car1.name, "( to choose type trd )\n")
                c = input("your choice -> ")
                C.look(self,c,b)
            if b == '2':
                print(C.DG_car2.name, "( to choose type dg )\n", C.BWM_car2.name, "( to choose type bwm )\n",
                      C.MCD_car2.name,
                      "( to choose type mcd )\n", C.TRD_car2.name, "( to choose type trd )\n")
                c = input("your choice -> ")
                C.look(self, c,b)
            if b =='3':
                print(C.DG_car3.name, "( to choose type dg )\n", C.BWM_car3.name, "( to choose type bwm )\n", C.MCD_car3.name,
                      "( to choose type mcd )\n")
                c = input("your choice -> ")
                C.look(self, c, b)




    def look(self,c,b):

        if b=='1':
            if c == 'bwm':
                car = Cars.BWM_car1
                print(' ',car.color,'\n',car.power,'hp\n',car.tires,'\n',car.weight,'kg\n',car.name,'\n')
                Cars.__init__(self)
            if c == 'mcd':
                car = Cars.MCD_car1
                print(' ',car.color,'\n',car.power,'hp\n',car.tires,'\n',car.weight,'kg\n',car.name,'\n')
                Cars.__init__(self)
            if c == 'trd':
                car = Cars.TRD_car1
                print(' ',car.color, '\n', car.power, 'hp\n', car.tires, '\n', car.weight, 'kg\n', car.name, '\n')
                Cars.__init__(self)
            if c == 'dg':
                car = Cars.DG_car1
                print(' ',car.color, '\n', car.power, 'hp\n', car.tires, '\n', car.weight, 'kg\n', car.name, '\n')
                Cars.__init__(self)

        if b =='2':
           if c == 'bwm':
               car = Cars.BWM_car2
               print(' ', car.color, '\n', car.power, 'hp\n', car.tires, '\n', car.weight, 'kg\n', car.name, '\n')
               Cars.__init__(self)
           if c == 'mcd':
               car = Cars.MCD_car2
               print(car.color, '\n', car.power, 'hp\n', car.tires, '\n', car.weight, 'kg\n', car.name, '\n')
               Cars.__init__(self)
           if c == 'trd':
               car = Cars.TRD_car2
               print(car.color, '\n', car.power, 'hp\n', car.tires, '\n', car.weight, 'kg\n', car.name, '\n')
               Cars.__init__(self)
           if c == 'dg':
               car = Cars.DG_car2
               print(car.color, '\n', car.power, 'hp\n', car.tires, '\n', car.weight, 'kg\n', car.name, '\n')
               Cars.__init__(self)

        if b == '3':
            if c == 'bwm':
                car = Cars.BWM_car3
                print(' ', car.color, '\n', car.power, 'hp\n', car.tires, '\n', car.weight, 'kg\n', car.name, '\n')
                Cars.__init__(self)
            if c == 'mcd':
                car = Cars.MCD_car3
                print(car.color, '\n', car.power, 'hp\n', car.tires, '\n', car.weight, 'kg\n', car.name, '\n')
                Cars.__init__(self)
            if c == 'trd':
                car = Cars.TRD_car3
                print(car.color, '\n', car.power, 'hp\n', car.tires, '\n', car.weight, 'kg\n', car.name, '\n')
                Cars.__init__(self)
            if c == 'dg':
                car = Cars.DG_car3
                print(car.color, '\n', car.power, 'hp\n', car.tires, '\n', car.weight, 'kg\n', car.name, '\n')
                Cars.__init__(self)



    def buy_car(self):
        print('hi')
        a = input("what type do you want? -> ")
        b=input ("input name of the car -> " )
        if a == '1':
            if b=='dg':
                car = Cars.DG_car1
                car.ptice = a*car.power%car.weight*car.tires_connection*100
                print("Price = ", car.price)

            if b == 'bwm':
                car = Cars.BWM_car1
                car.ptice = a * car.power % car.weight * car.tires_connection * 100
                print("Price = ", car.price)

            if b == 'mcd':
                car = Cars.MCD_car1
                car.ptice = a * car.power % car.weight * car.tires_connection * 100
                print("Price = ", car.price)

            if b == 'trd':
                car = Cars.TRD_car1
                car.ptice = a * car.power % car.weight * car.tires_connection * 100
                print("Price = ", car.price)

        if a == '2':
            if b == 'dg':
                car = Cars.DG_car2
                car.ptice = a * car.power % car.weight * car.tires_connection * 100
                print("Price = ", car.price)

            if b == 'bwm':
                car = Cars.BWM_car2
                car.ptice = a * car.power % car.weight * car.tires_connection * 100
                print("Price = ", car.price)

            if b == 'mcd':
                car = Cars.MCD_car2
                car.ptice = a * car.power % car.weight * car.tires_connection * 100
                print("Price = ", car.price)

            if b == 'trd':
                car = Cars.TRD_car2
                car.ptice = a * car.power % car.weight * car.tires_connection * 100
                print("Price = ", car.price)

        if a == '3':
            if b == 'dg':
                car = Cars.DG_car3
                car.ptice = a * car.power % car.weight * car.tires_connection * 100
                print("Price = ", car.price)

            if b == 'bwm':
                car = Cars.BWM_car3
                car.ptice = a * car.power % car.weight * car.tires_connection * 100
                print("Price = ", car.price)

            if b == 'mcd':
                car = Cars.MCD_car3
                car.ptice = a * car.power % car.weight * car.tires_connection * 100
                print("Price = ", car.price)

            else:
                print("try one more time ")
                Cars.__init__(self)

    class default():
        color = 'red'
        weight = 1523
        power = 167
        name = 'd'
        tires = 'yoko'
        tires_connection = 51
        price = int
    class BWM_car1():
        color = 'green'
        weight = 1123
        power = 231
        name = 'M'
        tires = ''
        tires_connection = 67
        price = int
    class MCD_car1():
        color = 'green'
        weight = 1235
        power = 234
        name = "A"
        tires = ''
        tires_connection = 67
        price = int
    class TRD_car1():
        color = 'orange'
        weight = 1093
        power = 327
        name = "S"
        tires = ''
        tires_connection = 63
        price = int
    class DG_car1():
        color = 'black'
        weight = 2100
        power = 723
        name = "CR"
        tires = ''
        tires_connection = 71
        price = int
    class BWM_car2():
        color = 'green'
        weight = 1723
        power = 279
        name = 'M1'
        tires = ''
        tires_connection = 73
        price = int
    class MCD_car2():
        color = 'green'
        weight = 1835
        power = 320
        name = "A"
        tires = ''
        tires_connection = 70
        price = int
    class TRD_car2():
        color = 'green'
        weight = 2100
        power = 299
        name = "S1"
        tires = ''
        tires_connection = 73
        price = int
    class DG_car2():
        color = 'black'
        weight = 2300
        power = 649
        name = "CR1"
        tires = ''
        tires_connection = 73
        price = int

    class BWM_car3():
        color = 'green'
        weight = 1223
        power = 456
        name = 'M2'
        tires = ''
        tires_connection = 75
        price = int

    class MCD_car3():
        color = 'green'
        weight = 1235
        power = 433
        name = "A2"
        tires = ''
        tires_connection = 73
        price = int


    class DG_car3():
        color = 'black'
        weight = 2235
        power = 790
        name = "CR2"
        tires = ''
        tires_connection = 73
        price = int

    class F1():
        color='cool'
        weight=810
        power=900
        name="queen"
        tyres='michka'
        tyres_connection=87
        price = int

e = Cars()
input()