#!/usr/bin/python3

import tkinter
import turtle

class CalculatorTurtle(turtle.RawTurtle):
    
    def __init__(self, canvas):
        turtle.RawTurtle.__init__(self, canvas)
        self.width = 48
        self.height = 80
        self.symbols = {'0':self.zero, '1':self.one, '2':self.two,
        '3':self.three, '4':self.four, '5':self.five, '6':self.six,
        '7':self.seven, '8':self.eight, '9':self.nine, '+':self.plus,
        '-':self.minus}

    def make_block_waypoint(self, a, b, x, y):
        return ((x+a)*self.width, (y+b)*self.height)

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
        self.penup()
        waypoint = self.make_block_waypoint(0.1, 0.5, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        self.setheading(0)
        self.forward(0.8*self.width)
        self.penup()
        waypoint = self.make_block_waypoint(0.5, 0.74, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        self.setheading(270)
        self.forward(0.48*self.height)
        self.penup()

    def minus(self, x, y):
        self.penup()
        waypoint = self.make_block_waypoint(0.1, 0.5, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        self.setheading(0)
        self.forward(0.8*self.width)
        self.penup()        

    def bottom_line(self, x, y, length):
        self.penup()
        waypoint = self.make_block_waypoint(0, 0, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        self.setheading(0)
        self.forward(length*self.width)
        self.penup()

    def slash(self, x, y):
        self.penup()
        waypoint = self.make_block_waypoint(0, 1, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        waypoint = self.make_block_waypoint(1, 0, x, y)
        self.to_waypoint(waypoint)
        self.penup()

    def add(self, summand1, summand2):
        # TODO: improve code readability, adjust line and operator sign
        for i, figure in enumerate(summand1):
            draw_digit = self.symbols[figure]
            draw_digit(i, 0)
        self.plus(len(summand1)-len(summand2)-1, -1)
        for i, figure in zip(range(len(summand1)-len(summand2), len(summand2)+1), summand2):
            draw_digit = self.symbols[figure]
            draw_digit(i, -1)
        self.bottom_line(len(summand1)-len(summand2), -1, len(summand2))
        result_length = max(len(summand1), len(summand2))+1
        for summand in [summand1, summand2]:
            summand = summand.zfill(result_length)
        carry = 0
        for i in range(1, result_length+1):
            place_sum = sum([int(s[-i]) for s in [summand1.zfill(result_length), summand2.zfill(result_length)]])
            place_sum += carry
            place_sum = str(place_sum).zfill(2)
            draw_result_digit = self.symbols[place_sum[-1]]
            if not (i==result_length and place_sum[-1]=='0'):
                draw_result_digit(len(summand1)-i, -2)
            if place_sum[-2]!='0':
                draw_carry_digit = self.symbols[place_sum[-2]]
                draw_carry_digit(len(summand1)-1-i, 1)
            carry = int(place_sum[-2])
        self.forward(30)

    def subtract(self, minuhend, subtrahend):
        pass # TODO

    def multiply(self, factor1, factor2):
        pass # TODO

    def divide(self, dividend, divisor):
        pass # TODO

class TurtleArithmetic(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Turtle Arithmetic (Unstable; in development)")
        self.resizable(width='FALSE', height='FALSE')

        self.menu_bar = tkinter.Menu(self)
        self.file_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Quit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.appearance_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.appearance_menu.add_radiobutton(label="Chalkboard", command=self.chalkboard_appearance)
        self.appearance_menu.add_radiobutton(label="Whiteboard", command=self.whiteboard_appearance)
        self.menu_bar.add_cascade(label="Appearance", menu=self.appearance_menu)

        # TODO: make this speed menu actually work (presently it seems to set speed to max)
        self.speed_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        for s in range(1, 12):
            self.speed_menu.add_radiobutton(label=str(s), command=lambda: self.our_heroine.speed(s))
        self.menu_bar.add_cascade(label="Speed", menu=self.speed_menu)

        self.config(menu=self.menu_bar)

        self.turtle_canvas = tkinter.Canvas(self, width=400, height=400)
        self.turtle_canvas.grid(row=0, columnspan=4)

        # TODO: adjust coordinate system. This would probably also
        # require adjustments to add method.

        self.first_number_label = tkinter.Label(self, text="First number:")
        self.first_number_label.grid(row=1, column=1, sticky='E')
        self.first_number_field = tkinter.Entry(self)
        self.first_number_field.configure(width=5)
        self.first_number_field.grid(row=1, column=2, sticky='W')

        self.second_number_label = tkinter.Label(self, text="Second number:")
        self.second_number_label.grid(row=2, column=1, sticky='E')
        self.second_number_field = tkinter.Entry(self)
        self.second_number_field.configure(width=5)
        self.second_number_field.grid(row=2, column=2, sticky='W')

        self.add_button = tkinter.Button(self, text="Add", command=self.addition)
        self.add_button.grid(row=3, column=0)

        self.add_button = tkinter.Button(self, text="Subtract", command=self.subtraction)
        self.add_button.grid(row=3, column=1)

        self.add_button = tkinter.Button(self, text="Multiply", command=self.multiplication)
        self.add_button.grid(row=3, column=2)

        self.add_button = tkinter.Button(self, text="Divide", command=self.division)
        self.add_button.grid(row=3, column=3)

        self.setting = turtle.TurtleScreen(self.turtle_canvas)
        self.our_heroine = CalculatorTurtle(self.setting)
        self.chalkboard_appearance()
        self.mainloop()

    def chalkboard_appearance(self):
        self.our_heroine.clear()
        self.setting.bgcolor("#2B502B")
        self.our_heroine.shape("turtle")
        self.our_heroine.pencolor("#FFFFFF")
        self.our_heroine.pensize(4)

    def whiteboard_appearance(self):
        self.our_heroine.clear()
        self.setting.bgcolor("#F5F5F5")
        self.our_heroine.shape("turtle")
        self.our_heroine.pencolor("#0000CD")
        self.our_heroine.pensize(4)

    def paper_appearance(self):
        pass # TODO

    def addition(self):
        for i in range(2):
            self.appearance_menu.entryconfig(i, state=tkinter.DISABLED)
        self.our_heroine.clear()
        self.our_heroine.add(self.first_number_field.get(), self.second_number_field.get())
        for i in range(2):
            self.appearance_menu.entryconfig(i, state=tkinter.NORMAL)

    def subtraction(self):
        pass # TODO

    def multiplication(self):
        pass # TODO

    def division(self):
        pass # TODO

if __name__ == "__main__":
    TurtleArithmetic()
