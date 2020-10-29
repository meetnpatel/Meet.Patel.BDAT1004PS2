from tkinter import *
import tkinter as tk

master = Tk()
master.geometry('600x180')

root2 = Frame(master)
root2.pack(side = RIGHT)
root1 = Frame(master)
root1.pack(side = LEFT)

label1 = Label(root1, text="Loan Amount:",width=20,font=("bold", 10))
label1.grid(row=0, column=0)
entry1 = Entry(root1)
entry1.grid(row=0, column=1)
label2 = Label(root1, text="Interest rate:",width=20,font=("bold", 10))
label2.grid(row=1, column=0)
entry2 = Entry(root1)
entry2.grid(row=1, column=1)
label3 = Label(root1, text="Loan terms:",width=20,font=("bold", 10))
label3.grid(row=2, column=0)
entry3 = Entry(root1)
entry3.grid(row=2, column=1)
button1 = Button(root1, text='Compute Mortgage',height=1, width=17)
button1.grid(row=3, column=0)
entry4 = Entry(root1)
entry4.grid(row=3, column=1)



expression = Entry(root2)
expression.grid(columnspan=4, ipadx=80) 

button1 = Button(root2, text=' MC ',height=1, width=8) 
button1.grid(row=2, column=0)

button2 = Button(root2, text=' M+ ', height=1, width=8) 
button2.grid(row=2, column=1) 

button3 = Button(root2, text=' M- ', height=1, width=8) 
button3.grid(row=2, column=2)

button4 = Button(root2, text=' MR ', height=1, width=8) 
button4.grid(row=2, column=3) 

button5 = Button(root2, text=' C ', height=1, width=8) 
button5.grid(row=3, column=0) 

button6 = Button(root2, text=' \u221a ', height=1, width=8) 
button6.grid(row=3, column=1) 

button7 = Button(root2, text=' x² ', height=1, width=8) 
button7.grid(row=3, column=2) 

button8 = Button(root2, text=' + ', height=1, width=8) 
button8.grid(row=3, column=3)

button9 = Button(root2, text=' 7 ', height=1, width=8) 
button9.grid(row=4, column=0) 

button10 = Button(root2, text=' 8 ', height=1, width=8) 
button10.grid(row=4, column=1) 

button11 = Button(root2, text=' 9 ', height=1, width=8) 
button11.grid(row=4, column=2) 

button12 = Button(root2, text=' - ', height=1, width=8) 
button12.grid(row=4, column=3)

button13 = Button(root2, text=' 4 ', height=1, width=8) 
button13.grid(row=5, column=0)

button14 = Button(root2, text='5', height=1, width=8) 
button14.grid(row=5, column='1')

button15 = Button(root2, text=' 6 ', height=1, width=8) 
button15.grid(row=5, column=2)

button16 = Button(root2, text=' * ', height=1, width=8) 
button16.grid(row=5, column=3) 

button17= Button(root2, text='1', height=1, width=8) 
button17.grid(row=6, column=0)

button18= Button(root2, text='2', height=1, width=8) 
button18.grid(row=6, column=1)

button19= Button(root2, text='3', height=1, width=8) 
button19.grid(row=6, column=2)

button20= Button(root2, text='/', height=1, width=8) 
button20.grid(row=6, column=3)

button21= Button(root2, text='0', height=1, width=8) 
button21.grid(row=7, column=0)

button22= Button(root2, text='.', height=1, width=8) 
button22.grid(row=7, column=1)

button23= Button(root2, text='+-', height=1, width=8) 
button23.grid(row=7, column=2)

button24= Button(root2, text='=', height=1, width=8) 
button24.grid(row=7, column=3)

master.mainloop()
