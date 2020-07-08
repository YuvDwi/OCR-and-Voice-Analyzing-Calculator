from tkinter import *
import speech_recognition as sr
import pyaudio

root = Tk()
root.title("VOICE CALCULATOR")
root.resizable(False, False)
e = Entry(root, width=35, borderwidth=20)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    add_num = e.get()
    e.delete(0, END)
    e.insert(0, number)
    e.insert(0, add_num)

def button_clear():
    e.delete(0, END)


def button_add():
    first = e.get()
    e.delete(0, END)
    e.insert(0, '+')
    e.insert(0, first)


def button_minus():
    first = e.get()
    e.delete(0, END)
    e.insert(0, "-")
    e.insert(0, first)

def button_multiply():
    first = e.get()
    e.delete(0, END)
    e.insert(0, "*")
    e.insert(0, first)

def button_divide():
    first = e.get()
    e.delete(0, END)
    e.insert(0, "/")
    e.insert(0, first)


def button_equal():
    equation = e.get()
    x = (eval(equation))
    e.delete(0, END)
    e.insert(0, x)


def record():
    print("Speak")
    e.delete(0, END)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)
    try:
        e.insert(0, eval(text))
    except:
        e.insert(0, "Speak an equation next time")


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=39, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=", padx=103.3, pady=20, command=button_equal)
button_clear = Button(root, text="clear", padx=94.7, pady=20, command=button_clear)
button_minus = Button(root, text="-", padx=40, pady=20, command=button_minus)
button_multiply = Button(root, text="x", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="÷", padx=40, pady=20, command=button_divide)
button_record = Button(root, text="Voice Activate", padx=40, pady=20, command=record)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_record.grid(row=0, column=4)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_minus.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()
