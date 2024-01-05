import tkinter as tk
from tkinter import ttk 
from tkinter import scrolledtext
root=tk.Tk()
root.title("scrolltext")
root.geometry("600x600")

ttk.Label(root,text="python life",background="blue",foreground="white",font=("Times new Roman",15)).grid(row=0,column=1)



#combobox

'''n=tk.StringVar()
course=ttk.Combobox(root,width=20,textvariable=n)
course['values']=("python","django","machine learniing")
course.grid(column=1,row=5)'''

#scrolltext
text1=scrolledtext.ScrolledText(root,wrap=tk.WORD,width=10,heigh=10)
text1.grid(column=0,pady=10,padx=10)

text1.focus()

                  


root.mainloop()