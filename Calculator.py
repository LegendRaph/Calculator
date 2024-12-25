from tkinter import *

window = Tk()


# FUNCTIONS
def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


def equality():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set('Arithmetic Error')
    except SyntaxError:
        equation_label.set('Syntax Error')


form = 's'


def approx():
    global equation_text
    global form
    if form == 's':
        total = str(round(eval(equation_text)))
        equation_label.set(total)
        equation_text = total
        form = 'd'
    elif form == 'd':
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
        form = 's'


mode = 'light'


def colormode():
    global mode
    global b4
    if mode == 'light':
        b4 = Button(window, text='🌙')
        window.config(background='#212221')
        label.config(bg='#212221', fg='white')
        clear_button.config(bg='#ef4c4a', fg='black')
        backspace_button.config(bg='#626360', fg='white')
        b3.config(bg='#626360', fg='white')
        b4.config(bg='#3f403e', fg='white')
        b5.config(bg='#3f403e', fg='white')
        b6.config(bg='#3f403e', fg='white')
        b7.config(bg='#3f403e', fg='white')
        b8.config(bg='#626360', fg='white')
        b9.config(bg='#3f403e', fg='white')
        b10.config(bg='#3f403e', fg='white')
        b11.config(bg='#3f403e', fg='white')
        b12.config(bg='#626360', fg='white')
        b13.config(bg='#3f403e', fg='white')
        b14.config(bg='#3f403e', fg='white')
        b15.config(bg='#3f403e', fg='white')
        b16.config(bg='#626360', fg='white')
        b17.config(bg='#3f403e', fg='white')
        b18.config(bg='#3f403e', fg='white')
        b19.config(bg='#3f403e', fg='white')
        b4 = Button(window, text='☀', padx=33, pady=18, bd=1, command=colormode, bg='#626360', fg='white',
                    activebackground='#cccccc')
        b4.place(x=5, y=90)
        mode = 'dark'

    else:
        window.config(background='white')
        label.config(bg='white', fg='black')
        clear_button.config(bg='#ef4c4a', fg='black')
        backspace_button.config(bg='#c6c7c5', fg='black')
        b3.config(bg='#c6c7c5', fg='black')
        b4.config(bg='white', fg='black')
        b5.config(bg='white', fg='black')
        b6.config(bg='white', fg='black')
        b7.config(bg='white', fg='black')
        b8.config(bg='#c6c7c5', fg='black')
        b9.config(bg='white', fg='black')
        b10.config(bg='white', fg='black')
        b11.config(bg='white', fg='black')
        b12.config(bg='#c6c7c5', fg='black')
        b13.config(bg='white', fg='black')
        b14.config(bg='white', fg='black')
        b15.config(bg='white', fg='black')
        b16.config(bg='#c6c7c5', fg='black')
        b17.config(bg='white', fg='black')
        b18.config(bg='white', fg='black')
        b19.config(bg='white', fg='black')
        b4 = Button(window, text='🌙', padx=35, pady=18, bd=1, command=colormode, bg='#c6c7c5', fg='black',
                    activebackground='#cccccc')
        b4.place(x=5, y=90)
        mode = 'light'


# UI
window.geometry('385x420')
window.title("Calculator")
window.resizable(width=False, height=False)
window.config(bg='white')

icon = PhotoImage(file='calc.png')
window.iconphoto(True, icon)

equation_text = ""
equation_label = StringVar()

# INPUT BOX
label = Label(window, justify="right", textvariable=equation_label, font=('consolas', 25), bg='white', width=18,
              height=1, pady=20)
label.pack()

# BUTTONS
clear_button = Button(window, text='C', command=clear, padx=34, pady=18, bd=1, activebackground='#ae110f', bg='#ef4c4a')
clear_button.place(x=195, y=90)

backspace_button = Button(window, text='x^2', padx=31, pady=18, bd=1, command=lambda: button_press('**2'), bg='#c6c7c5',
                          activebackground='#cccccc')
backspace_button.place(x=100, y=90)

b3 = Button(window, text='➗', padx=30, pady=18, bd=1, command=lambda: button_press('/'), bg='#c6c7c5',
            activebackground='#cccccc')
b3.place(x=295, y=90)

b4 = Button(window, text='🌙', padx=35, pady=18, bd=1, command=colormode, bg='#c6c7c5', activebackground='#cccccc')
b4.place(x=5, y=90)

b5 = Button(window, text='7', padx=32, pady=11, font=1, bd=1, command=lambda: button_press(7),
            activebackground='#cccccc')
b5.place(x=5, y=155)

b6 = Button(window, text='8', padx=32, pady=11, font=1, bd=1, command=lambda: button_press(8),
            activebackground='#cccccc')
b6.place(x=100, y=155)

b7 = Button(window, text='9', padx=29, pady=11, font=1, bd=1, command=lambda: button_press(9),
            activebackground='#cccccc')
b7.place(x=195, y=155)

b8 = Button(window, text='X', padx=29, pady=11, font=1, bd=1, command=lambda: button_press('*'), bg='#c6c7c5',
            activebackground='#cccccc')
b8.place(x=295, y=155)

b9 = Button(window, text='4', padx=32, pady=11, font=1, bd=1, command=lambda: button_press(4),
            activebackground='#cccccc')
b9.place(x=5, y=220)

b10 = Button(window, text='5', padx=32, pady=11, font=1, bd=1, command=lambda: button_press(5),
             activebackground='#cccccc')
b10.place(x=100, y=220)

b11 = Button(window, text='6', padx=29, pady=11, font=1, bd=1, command=lambda: button_press(6),
             activebackground='#cccccc')
b11.place(x=195, y=220)

b12 = Button(window, text='➖', padx=30, pady=18, bd=1, command=lambda: button_press('-'), bg='#c6c7c5',
             activebackground='#cccccc')
b12.place(x=295, y=220)

b13 = Button(window, text='1', padx=32, pady=11, font=1, bd=1, command=lambda: button_press(1),
             activebackground='#cccccc')
b13.place(x=5, y=285)

b14 = Button(window, text='2', padx=32, pady=11, font=1, bd=1, command=lambda: button_press(2),
             activebackground='#cccccc')
b14.place(x=100, y=285)

b15 = Button(window, text='3', padx=29, pady=11, font=1, bd=1, command=lambda: button_press(3),
             activebackground='#cccccc')
b15.place(x=195, y=285)

b16 = Button(window, text='➕', padx=30, pady=18, bd=1, command=lambda: button_press('+'), bg='#c6c7c5',
             activebackground='#cccccc')
b16.place(x=295, y=285)

b17 = Button(window, text='s/d', padx=32, pady=18, bd=1, command=approx, activebackground='#cccccc')
b17.place(x=5, y=350)

b18 = Button(window, text='0', padx=32, pady=11, bd=1, font=1, command=lambda: button_press('0'),
             activebackground='#cccccc')
b18.place(x=100, y=350)

b19 = Button(window, text='▫', padx=35, pady=18, bd=1, command=lambda: button_press('.'), activebackground='#cccccc')
b19.place(x=195, y=350)

b20 = Button(window, text='=', padx=29, pady=11, font=1, bd=1, command=equality, bg='#2ed16d',
             activebackground='#23a056')
b20.place(x=295, y=350)

window.mainloop()
