#!/usr/bin/python3

import tkinter
import turtle

class CalculatorTurtle(turtle.RawTurtle):
    
    def __init__(self, canvas):
        turtle.RawTurtle.__init__(self, canvas)
        self.penup()
        self.width = 48
        self.height = 80
        self.speed(0) # max speed for testing purposes; comment out for demos
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

    def add(self, summand1, summand2, x, y):
        summands_length = max([len(s) for s in [summand1, summand2]])
        result_length = summands_length + 1
        summands = [s.zfill(summands_length) for s in [summand1, summand2]]
        for i, s in enumerate(summands):
            leading_zeros = True
            for j, figure in enumerate(s):
                if not leading_zeros or figure!='0':
                    leading_zeros = False
                    draw_digit = self.symbols[figure]
                    draw_digit(x+j+1, y-i)
            if i == len(summands)-2:
                self.plus(x, y-1)
            if i == len(summands)-1:
                self.bottom_line(x, y-1, summands_length+1)
        carry = 0
        summands = ['0'+s for s in summands]
        for i in range(1, result_length+1):
            place_sum = sum([int(s[-i]) for s in summands])
            place_sum += carry
            place_sum = str(place_sum).zfill(2)
            if not (i==result_length and place_sum[-1]=='0'):
                draw_result_digit = self.symbols[place_sum[-1]]
                draw_result_digit(x+summands_length+1-i, y-2)
            if place_sum[-2]!='0':
                draw_carry_digit = self.symbols[place_sum[-2]]
                draw_carry_digit(x+summands_length-i, y+1)
            carry = int(place_sum[-2])
        self.forward(45)

    def subtract(self, minuhend, subtrahend, x, y):
        pass # TODO

    def multiply(self, factor1, factor2, x, y):
        pass # TODO

    def divide(self, dividend, divisor, x, y):
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

        # TODO: submenu to choose chalk colors?
        # IDEA: optional general colorpicker popup window?
        self.appearance_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.appearance_menu.add_radiobutton(label="Chalkboard", command=self.chalkboard_appearance)
        self.appearance_menu.add_radiobutton(label="Whiteboard", command=self.whiteboard_appearance)
        self.menu_bar.add_cascade(label="Appearance", menu=self.appearance_menu)

        # TODO: make this speed menu actually work (presently it seems to set speed to max)
        self.speed_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        for s in range(1, 12):
            self.speed_menu.add_radiobutton(label=str(s), command=lambda: self.our_heroine.speed(s))
            # Disable menu items for demo purposes until I can get them to work:
            self.speed_menu.entryconfig(s, state=tkinter.DISABLED)
        self.menu_bar.add_cascade(label="Speed", menu=self.speed_menu)

        self.config(menu=self.menu_bar)

        self.turtle_canvas = tkinter.Canvas(self, width=500, height=500)
        self.turtle_canvas.grid(row=0, columnspan=4)

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

        self.add_button = tkinter.Button(self, text="Add", command=lambda: self.operation('+'))
        self.add_button.grid(row=3, column=0)

        self.add_button = tkinter.Button(self, text="Subtract", command=lambda: self.operation('-'))
        self.add_button.grid(row=3, column=1)

        self.add_button = tkinter.Button(self, text="Multiply", command=lambda: self.operation('+'))
        self.add_button.grid(row=3, column=2)

        self.add_button = tkinter.Button(self, text="Divide", command=lambda: self.operation('/'))
        self.add_button.grid(row=3, column=3)

        self.setting = turtle.TurtleScreen(self.turtle_canvas)
        self.setting.setworldcoordinates(0, 0, 500, 500)
        self.our_heroine = CalculatorTurtle(self.setting)
        self.chalkboard_appearance()
        self.our_heroine.setheading(self.our_heroine.towards(250, 250))
        self.our_heroine.forward(self.our_heroine.distance(250, 250))
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

        #  TODO: dynamically change self.width and self.height in
        #  response to the number of digits in the user input; that
        #  way, the program can support larger numbers (and long
        #  division) without making all calculations unduly small

    # IDEA: also, instead of doing only a single binary operation from
    # two text fields, parse an abitrary arithmetic expression and do
    # all the calculations indicated

    def operation(self, op):
        # TODO: make error message explicitly name which input is bad
        # TODO: also, check for spaces---Python's int() handles them
        # intelligently, but my 'add' method does not
        a, b = self.first_number_field.get(), self.second_number_field.get()
        try:
            m = int(a); n = int(b)
        except ValueError:
            tkinter.messagebox.showinfo("Error", "The turtle doesn't understand.")
            return
        for i in range(2):
            self.appearance_menu.entryconfig(i, state=tkinter.DISABLED)
        self.our_heroine.clear()
        if op=='+':
            self.our_heroine.add(a, b, 4, 4)
        elif op=='-':
            pass # TODO
        elif op=='x':
            pass # TODO
        elif op=='/':
            pass # TODO
        for i in range(2):
            self.appearance_menu.entryconfig(i, state=tkinter.NORMAL)

if __name__ == "__main__":
    TurtleArithmetic()
