#!/usr/bin/env python3

import tkinter
import turtle
from math import sin, cos, radians
from functools import partial

from pdb import set_trace as debug

class CalculatorTurtle(turtle.RawTurtle):
    def __init__(self, canvas):
        turtle.RawTurtle.__init__(self, canvas)
        self.penup()
        self.width = 48
        self.height = 80
        # max speed for testing purposes; comment out (or use speed
        # menu) for demos
        self.speed(0)
        self.digits = {
            '0':self.zero, '1':self.one, '2':self.two,
            '3':self.three, '4':self.four, '5':self.five,
            '6':self.six, '7':self.seven, '8':self.eight,
            '9':self.nine
        }

        class ResizedTurtle:
            def __init__(self, turtle, factor):
                self.turtle = turtle
                self.factor = factor

            def __enter__(self):
                self.turtle.width *= self.factor
                self.turtle.height *= self.factor

            def __exit__(self, _type, _value, _traceback):
                self.turtle.width /= self.factor
                self.turtle.height /= self.factor

        self.do_half = ResizedTurtle(self, 0.5)

    def to_waypoint(self, a, b, x, y):
        wp = ((x+a)*self.width, (y+b)*self.height)
        self.setheading(self.towards(wp[0], wp[1]))
        self.forward(self.distance(wp[0], wp[1]))

    def hit_waypoints(self, points, x, y):
        for p in points:
            self.to_waypoint(*(p+(x,y)))

    def zero(self, x, y):
        self.penup()
        n = 14
        angles = [((360/n)*i + 90)%360 for i in range(n,-1,-1)]
        points = list(map(lambda t: (0.3*cos(radians(t))+0.5, 0.3*sin(radians(t))+0.5), angles))
        self.to_waypoint(*(points[0]+(x,y)))
        self.pendown()
        self.hit_waypoints(points, x, y)
        self.penup()

    def one(self, x, y):
        self.penup()
        points = [(0.5, 0.8), (0.5, 0.2)]
        self.to_waypoint(*(points[0]+(x,y)))
        self.pendown()
        self.hit_waypoints(points, x, y)
        self.penup()

    def two(self, x, y):
        self.penup()
        self.to_waypoint(0.2, 0.6, x, y)
        self.pendown()
        self.setheading(90)
        self.circle(-0.3*self.width, 180)
        self.to_waypoint(0.2, 0.2, x, y)
        self.to_waypoint(0.8, 0.2, x, y)
        self.penup()

    def three(self, x, y):
        self.penup()
        self.to_waypoint(0.25, 0.65, x, y)
        self.pendown()
        self.setheading(90)
        self.circle(-0.15*self.height, 270)
        self.setheading(0)
        self.circle(-0.15*self.height, 270)
        self.penup()

    def four(self, x, y):
        self.penup()
        points = [(0.2, 0.8), (0.2, 0.5), (0.8, 0.5)]
        self.to_waypoint(*(points[0]+(x,y)))
        self.pendown()
        self.hit_waypoints(points, x, y)
        self.penup()
        points = [(0.8, 0.8), (0.8, 0.2)]
        self.to_waypoint(*(points[0]+(x,y)))
        self.pendown()
        self.hit_waypoints(points, x, y)
        self.penup()

    def five(self, x, y):
        self.penup()
        points = [(0.8, 0.8), (0.2, 0.8), (0.2, 0.5)]
        self.to_waypoint(*(points[0]+(x,y)))
        self.pendown()
        self.hit_waypoints(points, x, y)
        self.setheading(40)
        self.circle(-0.195*self.height, 260)
        self.penup()

    def six(self, x, y):
        self.penup()
        self.to_waypoint(0.8, 0.65, x, y)
        self.pendown()
        self.setheading(90)
        self.circle(0.3*self.width, 180)
        self.forward(0.3*self.height)
        self.circle(0.3*self.width)
        self.penup()

    def seven(self, x, y):
        self.penup()
        self.to_waypoint(0.2, 0.8, x, y)
        self.pendown()
        self.to_waypoint(0.8, 0.8, x, y)
        self.to_waypoint(0.2, 0.2, x, y)
        self.penup()

    def eight(self, x, y):
        self.penup()
        self.to_waypoint(0.5, 0.85, x, y)
        self.pendown()
        self.setheading(0)
        self.circle(-0.17*self.height, 180)
        self.circle(0.17*self.height, 180)
        self.circle(0.17*self.height, 180)
        self.circle(-0.17*self.height, 180)
        self.penup()

    def nine(self, x, y):
        self.penup()
        self.to_waypoint(0.8, 0.7, x, y)
        self.pendown()
        self.setheading(270)
        self.circle(-0.3*self.width)
        self.forward(0.5*self.height)
        self.penup()

    def plus(self, x, y):
        self.penup()
        self.to_waypoint(0.1, 0.5, x, y)
        self.pendown()
        self.setheading(0)
        self.forward(0.8*self.width)
        self.penup()
        self.to_waypoint(0.5, 0.74, x, y)
        self.pendown()
        self.setheading(270)
        self.forward(0.48*self.height)
        self.penup()

    def minus(self, x, y):
        self.penup()
        self.to_waypoint(0.1, 0.5, x, y)
        self.pendown()
        self.setheading(0)
        self.forward(0.8*self.width)
        self.penup()

    def times(self, x, y):
        self.penup()
        self.to_waypoint(0.1, 0.74, x, y)
        self.pendown()
        self.to_waypoint(0.9, 0.26, x, y)
        self.penup()
        self.to_waypoint(0.9, 0.74, x, y)
        self.pendown()
        self.to_waypoint(0.1, 0.26, x, y)
        self.penup()

    def bottom_line(self, x, y, length):
        self.penup()
        self.to_waypoint(0, 0, x, y)
        self.pendown()
        self.setheading(0)
        self.forward(length*self.width)
        self.penup()

    def slash(self, x, y):
        self.penup()
        self.to_waypoint(0.15, 0.85, x, y)
        self.pendown()
        self.to_waypoint(0.85, 0.15, x, y)
        self.penup()

    def r(self, x, y):
        # TODO: a better 'r' is possible
        self.penup()
        self.to_waypoint(0.2, 0.5, x, y)
        self.setheading(-90)
        self.pendown()
        self.forward(0.4*self.height)
        self.penup()
        self.setheading(90)
        self.forward(0.35*self.height)
        self.pendown()
        self.setheading(15)
        self.circle(-0.5*self.width, 60)
        self.penup()

    def number(self, digits, x, y):
        for i, d in enumerate(digits):
            self.digits[d](x+i, y)

    def statement(self, arg1, arg2, op, x, y):
        args_length = max([len(a) for a in (arg1, arg2)])
        args = [s.zfill(args_length) for s in (arg1, arg2)]
        for i, s in enumerate(args):
            leading_zeros = True
            for j, figure in enumerate(s):
                if not leading_zeros or figure!='0' or j == args_length-1:
                    leading_zeros = False
                    draw_digit = self.digits[figure]
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
        summands = ['0'+s for s in
                    self.statement(summand1, summand2, '+', x, y)]
        summands_length = len(summands[0])
        carry = 0
        for i in range(1, summands_length+1):
            place_sum = sum([int(s[-i]) for s in summands])
            place_sum += carry
            place_sum = str(place_sum).zfill(2)
            if not (i == summands_length and place_sum[-1] == '0'):
                draw_result_digit = self.digits[place_sum[-1]]
                draw_result_digit(x+summands_length-i, y-2)
            if place_sum[-2] != '0':
                draw_carry_digit = self.digits[place_sum[-2]]
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
                draw_result_digit = self.digits[str(place_difference)]
                draw_result_digit(x+len(minuhend)+1-i, y-2)
            else:
                # I worry that temporarily adjusting the length and
                # width properties like this is a kludge; how _should_
                # it be done?
                self.slash(x+len(minuhend)-i, y)
                with self.do_half:
                    draw_creditor_digit = self.digits[str(int(minuhend[-(i+1)]) - 1)]
                    draw_creditor_digit(2*(x+len(minuhend)-i)+1,
                                        2*(y+1))
                    minuhend = minuhend[:-(i+1)] + str(int(minuhend[-(i+1)]) - 1) + minuhend[-i:]
                self.slash(x+len(minuhend)-i+1, y)
                with self.do_half:
                    self.one(2*(x+len(minuhend)+1-i), 2*(y+1))
                    draw_debtor_digit = self.digits[minuhend[-i]]
                    draw_debtor_digit(2*(x+len(minuhend)+1-i)+1, 2*(y+1))
                place_difference = int('1' + minuhend[-i]) - int(subtrahend[-i])
                draw_result_digit = self.digits[str(place_difference)]
                draw_result_digit(x+len(minuhend)+1-i, y-2)
        self.forward(45)

    def multiply(self, factor1, factor2, x, y):
        self.statement(factor1, factor2, 'x', x, y)
        factors_length = max(len(factor1), len(factor2))
        carry = 0
        summands = [[0]*n for n in range(len(factor2))]
        for i in range(1, len(factor2)+1):
            for j in range(1, len(factor1)+1):
                place_product = (int(factor1[-j])*int(factor2[-i]))
                place_product += carry
                place_product = str(place_product).zfill(2)
                draw_result_digit = self.digits[place_product[-1]]
                draw_result_digit(x+factors_length-i-j+2, y-1-i)
                summands[i-1].append(int(place_product[-1]))
                carry = int(place_product[-2])
                if j == len(factor1):
                    draw_last_digit = self.digits[place_product[-2]]
                    draw_last_digit(x+factors_length-i-j+1, y-1-i)
                    summands[i-1].append(int(place_product[-2]))
                    carry = 0
        summands_length = max(len(s) for s in summands)
        self.bottom_line(x-(summands_length-factors_length)+1,
                         y-len(factor2)-1, summands_length)
        for s in summands:
            for p in range(summands_length - len(s)):
                s.append(0)
        summands.append([0]*summands_length) # carry digits
        for p in range(1, summands_length+1):
            place_sum = str(sum(s[p-1] for s in summands))
            draw_final_digit = self.digits[place_sum[-1]]
            draw_final_digit(x+factors_length-p+1, y-len(factor2)-2)
            for i, d in enumerate(map(int,
                                      reversed(list(place_sum[:-1])))):
                summands[-1][p+i] += d
                # but also need to support final carry into result
                # wait, perhaps not

    def division_tableau(self, x, y, length):
        self.penup()
        # maybe tweak first arg to -0.1ish for curved bar---
        self.to_waypoint(0, 0, x, y-1)
        self.pendown()
        # straight bar, not as cool
        self.to_waypoint(0, 0, x, y)
        # curved bar #TODO calculate parameters of right-paren shape
        # self.setheading(??)
        # self.circle(self.height, ??)
        self.bottom_line(x, y, length)

    def division_statement(self, dividend, divisor, x, y):
        self.penup()
        self.number(divisor, x, y-1)
        self.division_tableau(x+len(divisor), y, len(dividend))
        self.number(dividend, x+len(divisor), y-1)

    def divide(self, dividend, divisor, x, y):
        self.division_statement(dividend, divisor, x, y)
        i = 0
        while int(dividend[:i+1]) < int(divisor) and i < len(dividend)-1:
            i += 1
        place_dividend = dividend[:i]
        for j, d in enumerate(dividend[i:]):
            place_dividend += d
            place_quotient = str(int(place_dividend)//int(divisor))
            self.number(place_quotient, x+len(divisor)+i+j, y)
            place_subtrahend = str(int(place_quotient)*int(divisor))
            self.number(place_subtrahend,
                        x+len(divisor)+i+j-(len(place_subtrahend)-1),
                        y+(-2)*(j+1))
            self.bottom_line(x+len(divisor)+i+j-(len(place_subtrahend)-1),
                             y+(-2)*(j+1), len(place_subtrahend))
            place_dividend = str(int(place_dividend)-int(place_subtrahend))
            self.number(place_dividend,
                        x+len(divisor)+i+j-(len(place_dividend)-1),
                        y+(-2)*(j+1)-1)
            if j != len(dividend[i:])-1:
                self.digits[dividend[i+j+1]](x+len(divisor)+i+j+1,
                                             y+(-2)*(j+1)-1)
        remainder = place_dividend
        self.r(x+len(divisor)+len(dividend), y)
        self.number(remainder, x+len(divisor)+len(dividend)+1, y)
        self.forward(20)

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
        # BUG: appearance and speed menus appear to behave as part of
        # same radio group
        self.appearance_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.appearance_menu.add_radiobutton(
            label="Chalkboard", command=self.chalkboard_appearance
        )
        self.appearance_menu.add_radiobutton(
            label="Whiteboard", command=self.whiteboard_appearance
        )
        self.menu_bar.add_cascade(
            label="Appearance", menu=self.appearance_menu
        )

          # TODO: test speed menu for odd behavior; it seems to work
          # inconsistently (!?!) when changed during turtle action; in
          # the worst case it could be disabled during action
        self.speed_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        for s in ['slowest', 'slow', 'normal', 'fast', 'fastest']:
            self.speed_menu.add_radiobutton(
                label=s, command=lambda s=s: self.our_heroine.speed(s)
            )
        self.menu_bar.add_cascade(label="Speed", menu=self.speed_menu)

        self.config(menu=self.menu_bar)

        self.canvas_width = 500
        self.canvas_height = 500
        self.turtle_canvas = tkinter.Canvas(
            self, width=self.canvas_width, height=self.canvas_height
        )
        self.turtle_canvas.grid(row=0, columnspan=4)

        self.argument_labels = []
        self.argument_fields = []

        for argument_configs in (("First", 1), ("Second", 2)):
            new_label = tkinter.Label(
                self, text="{} number:".format(argument_configs[0])
            )
            new_label.grid(row=argument_configs[1], column=1, sticky='E')
            self.argument_labels.append(new_label)

            new_field = tkinter.Entry(self)
            new_field.configure(width=10)
            new_field.grid(row=argument_configs[1], column=2, sticky='W')
            self.argument_fields.append(new_field)

        self.add_button = tkinter.Button(
            self, text="Add", command=self.operation('+')
        )
        self.add_button.grid(row=3, column=0)

        self.add_button = tkinter.Button(
            self, text="Subtract", command=self.operation('-')
        )
        self.add_button.grid(row=3, column=1)

        self.add_button = tkinter.Button(
            self, text="Multiply", command=self.operation('x')
        )
        self.add_button.grid(row=3, column=2)

        self.add_button = tkinter.Button(
            self, text="Divide", command=self.operation('/')
        )
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
        return partial(self.do_operation, op)

    def do_operation(self, op):
        raw_arguments = [f.get().strip() for f in self.argument_fields]
        a, b = raw_arguments

        arguments = []
        nonnumbers = []
        for raw_argument in raw_arguments:
            try:
                arguments.append(int(raw_argument))
            except ValueError:
                nonnumbers.append(raw_argument)

        if nonnumbers:
            if len(nonnumbers) == 1:
                error_tail = '"{}" is not a number.'.format(nonnumbers[0])
            elif len(nonnumbers) == 2:
                error_tail = '"{}" and "{}" are not numbers.'.format(*nonnumbers)
            tkinter.messagebox.showerror(
                "Turtle Comprehension Error",
                "The turtle doesn't understand; {}".format(error_tail)
            )
            return

        m, n = arguments
        if m < 0 or n < 0:
            tkinter.messagebox.showerror(
                "Turtle Ignorant of Negative Numbers",
                "The turtle doesn't understand negative numbers."
            )
            for i in range(2):
                self.appearance_menu.entryconfig(i, state=tkinter.NORMAL)
            return
        for i in range(2):
            self.appearance_menu.entryconfig(i, state=tkinter.DISABLED)
        self.our_heroine.clear()

        if op == '+':
            true_blocks = self.aspect('+', a, b)
            self.our_heroine.add(a, b, 1, (self.canvas_height/true_blocks[1])-2)
        elif op == '-':
            if m < n:
                tkinter.messagebox.showerror(
                    "Turtle Ignorant of Negative Numbers",
                    ("The turtle doesn't know how to subtract a "
                    "bigger number from a smaller one.")
                )
                for i in range(2):
                    self.appearance_menu.entryconfig(i, state=tkinter.NORMAL)
                return
            true_blocks = self.aspect('-', a, b)
            self.our_heroine.subtract(
                a, b, 1, (self.canvas_height/true_blocks[1])-2
            )
        elif op == 'x':
            self.our_heroine.multiply(a, b, 2, 5)
        elif op == '/':
            with self.our_heroine.do_half:
                self.our_heroine.divide(a, b, 2, 11)
        for i in range(2):
            self.appearance_menu.entryconfig(i, state=tkinter.NORMAL)

if __name__ == "__main__":
    TurtleArithmetic()
