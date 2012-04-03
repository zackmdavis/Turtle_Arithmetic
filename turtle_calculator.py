import turtle

class CalculatorTurtle(turtle.RawTurtle):

    # maybe these should be instance variables?---I had thought that
    # these and the "symbols" dict should be class variables, but
    # "symbols" seems to need to belong to an instance in order for it
    # to work in the obvious way
    width = 48
    height = 80
    
    def __init__(self, canvas):
        turtle.RawTurtle.__init__(self, canvas)
        self.symbols = {'0':self.zero, '1':self.one, '2':self.two, '3':self.three, '4':self.four, '5':self.five, '6':self.six, '7':self.seven, '8':self.eight, '9':self.nine, '+':self.plus, '-':self.minus}

    @classmethod
    def make_block_waypoint(cls, a, b, x, y):
        return ((x+a)*cls.width, (y+b)*cls.height)

    def to_waypoint(self, wp):
        self.setheading(self.towards(wp[0], wp[1]))
        self.forward(self.distance(wp[0], wp[1]))

    # Note the many TODOs below; I should redesign all the digits,
    # but I made these sloppy digits first because I'm inspired by the
    # vision of having a minimal viable program as soon as possible

    def zero(self, x, y):
        # TODO: make this a proper elliptical zero, rather than a small circle
        self.penup()
        waypoint = self.make_block_waypoint(0.8, 0.5, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        self.setheading(90)
        self.circle(0.3*self.width)
        self.penup()

    def one(self, x, y):
        # TODO?-- a better numeral "1" than just a straight line?
        self.penup()
        waypoint = self.make_block_waypoint(0.5, 0.8, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        self.setheading(270)
        self.forward(0.6*self.height)
        self.penup()

    def two(self, x, y):
        # TODO: This isn't such a terrible "2" but it could probably be better
        self.penup()
        waypoint = self.make_block_waypoint(0.2, 0.6, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        self.setheading(90)
        self.circle(-0.3*self.width, 180)
        waypoint = self.make_block_waypoint(0.2, 0.2, x, y)
        self.to_waypoint(waypoint)
        waypoint = self.make_block_waypoint(0.8, 0.2, x, y)
        self.to_waypoint(waypoint)
        self.penup()

    def three(self, x, y):
        # TODO: Not terrible "3"; could be more natural
        self.penup()
        waypoint = self.make_block_waypoint(0.2, 0.7, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        self.setheading(45)
        self.circle(-0.15*self.height, 225)
        self.setheading(0)
        self.circle(-0.15*self.height, 225)
        self.penup()

    def four(self, x, y):
        # TODO: this is a crappy "4" in more ways than one
        self.penup()
        waypoint = self.make_block_waypoint(0.2, 0.8, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        waypoint = self.make_block_waypoint(0.2, 0.4, x, y)
        self.to_waypoint(waypoint)
        waypoint = self.make_block_waypoint(0.8, 0.4, x, y)
        self.to_waypoint(waypoint)
        self.penup()
        waypoint = self.make_block_waypoint(0.8, 0.8, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        waypoint = self.make_block_waypoint(0.8, 0.2, x, y)
        self.to_waypoint(waypoint)
        self.penup()

    def five(self, x, y):
        # TODO: design a better "5"
        self.penup()
        waypoint = self.make_block_waypoint(0.8, 0.8, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        waypoint = self.make_block_waypoint(0.2, 0.8, x, y)
        self.to_waypoint(waypoint)
        waypoint = self.make_block_waypoint(0.2, 0.5, x, y)
        self.to_waypoint(waypoint)
        self.setheading(0)
        self.forward(0.3*self.width)
        self.circle(-0.15*self.height, 240)
        self.penup()

    def six(self, x, y):
        # TODO: more natural "6"
        self.penup()
        waypoint = self.make_block_waypoint(0.8, 0.7, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        self.setheading(90)
        self.circle(0.3*self.width, 180)
        self.forward(0.4*self.height)
        self.circle(0.3*self.width)
        self.penup()

    def seven(self, x, y):
        # TODO: more natural "7"
        self.penup()
        waypoint = self.make_block_waypoint(0.2, 0.8, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        waypoint = self.make_block_waypoint(0.8, 0.8, x, y)
        self.to_waypoint(waypoint)
        waypoint = self.make_block_waypoint(0.2, 0.2, x, y)
        self.to_waypoint(waypoint)
        self.penup()

    def eight(self, x, y):
        # TODO: more natural "8"
        self.penup()
        waypoint = self.make_block_waypoint(0.5, 0.5, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        self.setheading(0)
        self.circle(0.15*self.height)
        self.circle(-0.15*self.height)
        self.penup()

    def nine(self, x, y):
        # TODO: more natural "9"
        self.penup()
        waypoint = self.make_block_waypoint(0.8, 0.7, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        self.setheading(270)
        self.circle(-0.3*self.width)
        self.forward(0.6*self.height)
        self.penup()

    def plus(self, x, y):
        pass # TODO: implement

    def minus(self, x, y):
        pass # TODO: implement

    def bottom_line(self, x, y, length):
        self.penup()
        waypoint = self.make_block_waypoint(0, 0, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        self.setheading(0)
        self.forward(length*self.width)
        self.penup()

    def add(self, summand1, summand2):
        for i, figure in enumerate(summand1):
            digit = self.symbols[figure]
            digit(i, 0)
        for i, figure in zip(range(len(summand1)-len(summand2), len(summand2)+1), summand2):
            digit = self.symbols[figure]
            digit(i, -1)
        self.bottom_line(len(summand1)-len(summand2), -1, len(summand2))
        #for i in range(max(len(summand1), len(summand2))):
        # TODO: finish writing this function
             
        

def digit_test():
    # Testing routine to be deleted later
    setting = turtle.Screen()
    setting.title("Turtle Graphics Calculator")
    setting.bgcolor('#C2EBFF')
    our_heroine = CalculatorTurtle(setting)
    our_heroine.shape("turtle")
    our_heroine.zero(0,0)
    our_heroine.one(1,0)
    our_heroine.two(2,0)
    our_heroine.three(3,0)
    our_heroine.four(4,0)
    our_heroine.five(5,0)
    our_heroine.six(0,-1)
    our_heroine.seven(1,-1)
    our_heroine.eight(2,-1)
    our_heroine.nine(3,-1)
    our_heroine.forward(100)
    setting.mainloop()

def add_test():
    # Testing routine to be deleted later
    setting = turtle.Screen()
    setting.title("Turtle Graphics Calculator")
    setting.bgcolor('#C2EBFF')
    our_heroine = CalculatorTurtle(setting)
    our_heroine.shape("turtle")
    our_heroine.add('234','5679')
    setting.mainloop()

#digit_test()
add_test()
