from tkinter import *
from tkinter.messagebox import *
import math as m

#defining the operations...
def backspace():
    equation = txt_field.get()
    equation = equation[0:len(equation)-1]
    txt_field.delete(0,END)
    txt_field.insert(0,equation)


def all_clear():
    txt_field.delete(0,END)

def on_click(flag):
    b = flag.widget
    text = b["text"]
    print(text)

    if text == "x":
        txt_field.insert(END,"*")
        return

    if text == "=":
        try:
            equation = txt_field.get()
            result = eval(equation)
            txt_field.delete(0,END)
            txt_field.insert(0, result)   
        except Exception as ex:
            showerror("Error..:", ex)
        return         
  

    txt_field.insert(END, text)

    


font = ("Lucida", 20,"bold")

#creating the box/window..
box = Tk()
box.title("Calculator")
box.geometry("500x430")
box.configure(background="Blue")

#Creating a menu bar

#heading label..
heading = Label(box, text = "Calculator", font =("Arial Rounded MT Bold", 24, "bold underline" ) )
heading.pack(side=TOP, pady=15)         #adding the heading to our window..


#adding the text field...
txt_field = Entry(box, font = font,  justify = CENTER)
txt_field.pack(side = TOP, padx = 15, fill = X)

#Frame class... This appears after we add buttons to it..
std_Frame = Frame(box)
std_Frame.pack(side=TOP, padx=15)

#adding buttons...
temp = 9
for i in range(3):
    for j in range(3):
        btn = Button(std_Frame, text=str(temp), font=font, width=6, relief="ridge", activebackground="grey" )
        btn.grid(row=i, column=j, padx=3, pady=3)
        temp-=1
        btn.bind("<Button-1>", on_click)

btnZero = Button(std_Frame, text="0", font=font, width=6, relief="ridge", activebackground="grey" )
btnZero.grid(row=3, column=0, padx=3, pady=3)

btnDot = Button(std_Frame, text=".", font=font, width=6, relief="ridge", activebackground="grey" )
btnDot.grid(row=3, column=1, padx=3, pady=3)

btnEquals = Button(std_Frame, text="=", font=font, width=6, relief="ridge", activebackground="grey" )
btnEquals.grid(row=3, column=2, padx=3, pady=3)

btnMultiply = Button(std_Frame, text="x", font=font, width=6, relief="ridge", activebackground="grey" )
btnMultiply.grid(row=0, column=3, padx=3, pady=3)

btnPlus = Button(std_Frame, text="+", font=font, width=6, relief="ridge", activebackground="grey" )
btnPlus.grid(row=1, column=3, padx=3, pady=3)

btnMinus = Button(std_Frame, text="-", font=font, width=6, relief="ridge", activebackground="grey" )
btnMinus.grid(row=2, column=3, padx=3, pady=3)

btnDivision = Button(std_Frame, text="/", font=font, width=6, relief="ridge", activebackground="grey" )
btnDivision.grid(row=3, column=3, padx=3, pady=3)

btnDelete = Button(std_Frame, text="<<---", font=font, width=13, relief="ridge", activebackground="grey", command=backspace )
btnDelete.grid(row=4, column=0, columnspan=2, padx=3, pady=3)

btnClear = Button(std_Frame, text="C", font=font, width=13, relief="ridge", activebackground="grey", command=all_clear )
btnClear.grid(row=4, column=2, columnspan=2, padx=1, pady=1)

#binding the remaining buttons..
btnZero.bind("<Button-1>", on_click)
btnDot.bind("<Button-1>", on_click)
btnEquals.bind("<Button-1>", on_click)
btnMultiply.bind("<Button-1>", on_click)
btnPlus.bind("<Button-1>", on_click)
btnMinus.bind("<Button-1>", on_click)
btnDivision.bind("<Button-1>", on_click)


#Scientific calculator
scFrame = Frame(box)

sinBtn = Button(scFrame, text='sinθ', font=font, width=6, relief="ridge", activebackground="grey")
sinBtn.grid(row=0, column=0)

cosBtn = Button(scFrame, text='cosθ', font=font, width=6, relief="ridge", activebackground="grey")
cosBtn.grid(row=0, column=1)

tanBtn = Button(scFrame, text='tanθ', font=font, width=6, relief="ridge", activebackground="grey")
tanBtn.grid(row=0, column=2)

commaBtn = Button(scFrame, text=',', font=font, width=6, relief="ridge", activebackground="grey")
commaBtn.grid(row=0, column=3)

factBtn = Button(scFrame, text='x!', font=font, width=13, relief="ridge", activebackground="grey")
factBtn.grid(row=1, column=0, columnspan=2, padx=3, pady=3)

powerBtn = Button(scFrame, text='^', font=font, width=13, relief="ridge", activebackground="grey")
powerBtn.grid(row=1, column=2, columnspan=2, padx=1, pady=1)



normalcalc = True

def calculate_sc(event):

    btn = event.widget
    text = btn['text']

    ex = txt_field.get()
    answer = ''

    if text == ",":
        txt_field.insert(END,",")
        return
    
    if text == 'x!':
        print("cal factorial")
        answer = str(m.factorial(int(ex)))
    elif text == 'sinθ':
        print("cal sin")
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cosθ':
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanθ':
        answer = str(m.tan(m.radians(int(ex))))
    elif text == '^':
        print('pow')
        base, power = ex.split(',')
        print(base)
        print(power)
        answer = m.pow(int(base), int(power))

    txt_field.delete(0, END)
    txt_field.insert(0, answer)


def sc_click():
    global normalcalc
    if normalcalc:
        
        std_Frame.pack_forget()
        # add sc frame
           
        scFrame.pack(side=TOP, pady=20)
        std_Frame.pack(side=TOP)
        box.geometry('500x600')
        
        normalcalc = False
    else:
        scFrame.pack_forget()
        box.geometry('500x430')
        normalcalc = True



# end functions
# binding sc buttons

sinBtn.bind("<Button-1>", calculate_sc)
cosBtn.bind("<Button-1>", calculate_sc)
tanBtn.bind("<Button-1>", calculate_sc)
commaBtn.bind("<Button-1>", calculate_sc)
factBtn.bind("<Button-1>", calculate_sc)
powerBtn.bind("<Button-1>", calculate_sc)


fontMenu = ('Arial', 15)
menubar = Menu(box, font=fontMenu)

filemenu = Menu(menubar, font=fontMenu, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Standard", command=sc_click)
filemenu.add_command(label="Scientific", command=sc_click)



box.config(menu=menubar)

box.mainloop()