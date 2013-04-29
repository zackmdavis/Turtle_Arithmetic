#!/usr/bin/python3

import tkinter
import turtle

class CalculatorTurtle(turtle.RawTurtle):
    
    def __init__(self, canvas):
        turtle.RawTurtle.__init__(self, canvas)
        self.penup()
        self.width = 48
        self.height = 80
        self.speed(0) # max speed for testing purposes; comment out (or use speed menu) for demos
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

    def times(self, x, y):
        self.penup()
        waypoint = self.make_block_waypoint(0.1, 0.74, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        waypoint = self.make_block_waypoint(0.9, 0.26, x, y)
        self.to_waypoint(waypoint)
        self.penup()
        waypoint = self.make_block_waypoint(0.9, 0.74, x, y)
        self.to_waypoint(waypoint)
        self.pendown()
        waypoint = self.make_block_waypoint(0.1, 0.26, x, y)
        self.to_waypoint(waypoint)
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

    def statement(self, arg1, arg2, op, x, y):
        args_length = max([len(a) for a in [arg1, arg2]])
        args = [s.zfill(args_length) for s in [arg1, arg2]]
        for i, s in enumerate(args):
            leading_zeros = True
            for j, figure in enumerate(s):
                if not leading_zeros or figure!='0' or j == args_length-1:
                    leading_zeros = False
                    draw_digit = self.symbols[figure]
                    draw_digit(x+j+1, y-i)
            if i == len(args)-2:
                if op == '+':
                    self.plus(x, y-1)
                elif op == '-':
                    self.minus(x, y-1)
                elif op == 'x':
                    self.times(x, y-1)
            if i == len(args)-1:
                self.bottom_line(x, y-1, args_length+1)
        return args

    def add(self, summand1, summand2, x, y):
        summands = ['0'+s for s in self.statement(summand1, summand2, '+', x, y)]
        summands_length = len(summands[0])
        carry = 0
        for i in range(1, summands_length+1):
            place_sum = sum([int(s[-i]) for s in summands])
            place_sum += carry
            place_sum = str(place_sum).zfill(2)
            if not (i==summands_length and place_sum[-1]=='0'):
                draw_result_digit = self.symbols[place_sum[-1]]
                draw_result_digit(x+summands_length-i, y-2)
            if place_sum[-2]!='0':
                draw_carry_digit = self.symbols[place_sum[-2]]
                draw_carry_digit(x+summands_length-1-i, y+1)
            carry = int(place_sum[-2])
        self.forward(45)

    def subtract(self, minuhend, subtrahend, x, y):
        # TODO: add support for multiple borrowings, strip leading
        # zeros, refrain from retracing already drawn slashes and
        # digits
        self.statement(minuhend, subtrahend, '-', x, y)
        subtrahend = subtrahend.zfill(len(minuhend))
        for i in range(1, len(minuhend)+1):
            place_difference = int(minuhend[-i]) - int(subtrahend[-i])
            if place_difference >= 0:
                draw_result_digit = self.symbols[str(place_difference)]
                draw_result_digit(x+len(minuhend)+1-i, y-2)
            else:
                # I worry that temporarily adjusting the length and
                # width properties like this is a kludge; how _should_
                # it be done?
                self.slash(x+len(minuhend)-i, y)
                self.width /= 2
                self.height /= 2
                draw_creditor_digit = self.symbols[str(int(minuhend[-(i+1)]) - 1)]
                draw_creditor_digit(2*(x+len(minuhend)-i)+1, 2*(y+1))
                minuhend = minuhend[:-(i+1)] + str(int(minuhend[-(i+1)]) - 1) + minuhend[-i:]
                self.width *= 2
                self.height *= 2
                self.slash(x+len(minuhend)-i+1, y)
                self.width /= 2
                self.height /= 2
                self.one(2*(x+len(minuhend)+1-i), 2*(y+1))
                draw_debtor_digit = self.symbols[minuhend[-i]]
                draw_debtor_digit(2*(x+len(minuhend)+1-i)+1, 2*(y+1))
                self.width *= 2
                self.height *= 2
                place_difference = int('1' + minuhend[-i]) - int(subtrahend[-i])
                draw_result_digit = self.symbols[str(place_difference)]
                draw_result_digit(x+len(minuhend)+1-i, y-2)                
        self.forward(45)

    def multiply(self, factor1, factor2, x, y):
        self.statement(factor1, factor2, 'x', x, y)
        factors_length = max(len(factor1), len(factor2))
        carry = 0
        summands = []
        for i in range(1, len(factor2)+1):
            for j in range(1, len(factor1)+1):
                place_product = str((int(factor1[j])*int(factor2[i])) + carry)
                place_product = place_product.zfill(2)
                if not (i == factors_length and place_product == '0'):
                    draw_result_digit = self.symbols[place_product[-1]]
                    draw_result_digit(x+factors_length-i-j, y-1-j)
                

    def divide(self, dividend, divisor, x, y):
        pass # TODO

class TurtleArithmetic(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("Turtle Arithmetic (in development)")
        self.resizable(width='FALSE', height='FALSE')

        self.menu_bar = tkinter.Menu(self)
        self.file_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Quit", command=self.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # TODO: submenu to choose chalk colors?
        # IDEA: optional general colorpicker popup window?
        # BUG: appearance and speed menus appear to behave as part of same radio group
        self.appearance_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.appearance_menu.add_radiobutton(label="Chalkboard", command=self.chalkboard_appearance)
        self.appearance_menu.add_radiobutton(label="Whiteboard", command=self.whiteboard_appearance)
        self.menu_bar.add_cascade(label="Appearance", menu=self.appearance_menu)

          # TODO: test speed menu for odd behavior; it seems to work
          # inconsistently (!?!) when changed during turtle action; in
          # the worst case it could be disabled during action
        self.speed_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        for s in ['slowest', 'slow', 'normal', 'fast', 'fastest']:
            self.speed_menu.add_radiobutton(label=s, command=lambda s=s: self.our_heroine.speed(s))
        self.menu_bar.add_cascade(label="Speed", menu=self.speed_menu)

        self.config(menu=self.menu_bar)
        
        self.canvas_width = 500
        self.canvas_height = 500
        self.turtle_canvas = tkinter.Canvas(self, width=self.canvas_width, height=self.canvas_height)
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

        self.add_button = tkinter.Button(self, text="Multiply", command=lambda: self.operation('x'))
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

    def aspect(self, op, arg1, arg2):
        # BUG: while this crude first draft of a dynamic resizing
        # routine sort-of works, it is obviously not correct (e.g.,
        # sums of four-digit numbers display larger than their
        # one-digit counterparts)
        if op == '+' or op == '-':
            calculation_width = max(len(arg1), len(arg2))+1
            calculation_height = 4
            max_block_width = self.canvas_width / (calculation_width + 2)
            max_block_height = self.canvas_height / (calculation_height + 2)
            if max_block_width < max_block_height:
                true_block_width = max_block_width
                true_block_height = (5/3)*(max_block_width)
            elif max_block_width >= max_block_height:
                true_block_height = max_block_height
                true_block_width = (3/5)*(max_block_height)
            self.our_heroine.width = true_block_width
            self.our_heroine.height = true_block_height
            return (true_block_width, true_block_height)
        elif op == 'x':
            pass # TODO
        elif op == '/':
            pass # TODO

    def operation(self, op):
        # TODO: check for spaces---Python's int() handles them
        # intelligently, but my 'add' (&c.) method does not
        # also, leading zeros
        a, b = self.first_number_field.get(), self.second_number_field.get()
        nonnumbers = []
        try:
            m = int(a)
        except ValueError:
            nonnumbers.append(a)
        try:
            n = int(b)
        except ValueError:
            nonnumbers.append(b)
        if nonnumbers:
            if len(nonnumbers) == 1:
                error_tail = '"' + nonnumbers[0] + '" is not a number.'
            elif len(nonnumbers) == 2:
                error_tail = '"' + nonnumbers[0] + '" and "' + nonnumbers[1] + '" are not numbers.'
            tkinter.messagebox.showerror("Turtle Comprehension Error", "The turtle doesn't understand: " + error_tail)
            return
        for i in range(2):
            self.appearance_menu.entryconfig(i, state=tkinter.DISABLED)
        self.our_heroine.clear()
        if op == '+':
            true_blocks = self.aspect('+', a, b)
            self.our_heroine.add(a, b, 1, (self.canvas_height/true_blocks[1])-2)
        elif op == '-':
            if m < n:
                tkinter.messagebox.showerror("Turtle Ignorant of Negative Numbers", "The turtle doesn't know how to subtract a bigger number from a smaller one.")
                for i in range(2):
                    self.appearance_menu.entryconfig(i, state=tkinter.NORMAL)
                return
            true_blocks = self.aspect('-', a, b)
            self.our_heroine.subtract(a, b, 1, (self.canvas_height/true_blocks[1])-2)

        elif op == 'x':
            self.our_heroine.multiply(a, b, 2, 4)
        elif op == '/':
            pass # TODO
        for i in range(2):
            self.appearance_menu.entryconfig(i, state=tkinter.NORMAL)

if __name__ == "__main__":
    TurtleArithmetic()
