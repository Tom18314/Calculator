from tkinter import *

input = ""

def press(num):
    global input
  
    input = input + str(num)
    equation.set(input)
  
def calculate(): 
    try:
        global input 

        total = str(round(eval(input), 7))
        equation.set(total)
        input = total
    except:
        equation.set(" error ")
        input = ""

def clear():
    global input
    input = ""
    equation.set("0")

def removelast():
    global input

    input = input[:-1]
    equation.set(input)

if __name__ == "__main__":
    gui = Tk()
    gui.title("Calculator")
    gui.resizable(False, False)

    equation = StringVar()
    equation.set('0')

    huidige_calculate = Label(gui, textvariable=equation, font=("Arial", 35))
    huidige_calculate.grid(row=0, columnspan=4, padx=5, pady=10, ipady=5)

    haakjeopen = Button(gui, text=' ( ', fg='black', bg='#DADADA', command=lambda: press("("), height=3, width=10)
    haakjeopen.grid(row=1, column='0')

    haakjesluit = Button(gui, text=' ) ', fg='black', bg='#DADADA', command=lambda: press(")"), height=3, width=10)
    haakjesluit.grid(row=1, column='1')

    clear = Button(gui, text=' C ', fg='black', bg='#DADADA', command=clear, height=3, width=10)
    clear.grid(row=1, column='2')

    remove = Button(gui, text=' <- ', fg='black', bg='#DADADA', command=removelast, height=3, width=10)
    remove.grid(row=1, column='3')

    button7 = Button(gui, text=' 7 ', fg='black', bg='#F3F3F3', command=lambda: press(7), height=3, width=10) 
    button7.grid(row=3, column=0)
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='#F3F3F3', command=lambda: press(8), height=3, width=10) 
    button8.grid(row=3, column=1)
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='#F3F3F3', command=lambda: press(9), height=3, width=10) 
    button9.grid(row=3, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='#F3F3F3', command=lambda: press(4), height=3, width=10)
    button4.grid(row=4, column=0)
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='#F3F3F3', command=lambda: press(5), height=3, width=10) 
    button5.grid(row=4, column=1)
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='#F3F3F3', command=lambda: press(6), height=3, width=10) 
    button6.grid(row=4, column=2)

    button1 = Button(gui, text=' 1 ', fg='black', bg='#F3F3F3', command=lambda: press(1), height=3, width=10) 
    button1.grid(row=5, column=0)
  
    button2 = Button(gui, text=' 2 ', fg='black', bg='#F3F3F3', command=lambda: press(2), height=3, width=10) 
    button2.grid(row=5, column=1)
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='#F3F3F3', command=lambda: press(3), height=3, width=10) 
    button3.grid(row=5, column=2)

    divide = Button(gui, text=' / ', fg='black', bg='#F3F3F3', command=lambda: press("/"), height=3, width=10)
    divide.grid(row=6, column=0)
  
    button0 = Button(gui, text=' 0 ', fg='black', bg='#F3F3F3', command=lambda: press(0), height=3, width=10)
    button0.grid(row=6, column=1)

    comnma = Button(gui, text=' , ', fg='black', bg='#F3F3F3', command=lambda: press("."), height=3, width=10)
    comnma.grid(row=6, column=2)

    equal = Button(gui, text=' = ', fg='black', bg='#70A7CF', command=calculate, height=3, width=10)
    equal.grid(row=6, column=3)
  
    plus = Button(gui, text=' + ', fg='black', bg='#DADADA', command=lambda: press("+"), height=3, width=10) 
    plus.grid(row=5, column=3)
  
    minus = Button(gui, text=' - ', fg='black', bg='#DADADA', command=lambda: press("-"), height=3, width=10)
    minus.grid(row=4, column=3)
  
    multiply = Button(gui, text=' X ', fg='black', bg='#DADADA', command=lambda: press("*"), height=3, width=10)
    multiply.grid(row=3, column=3)

    gui.mainloop()