import tkinter as tk
from tkinter import font
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x500")
        self.root.title("BATTLESHIP")
        
        self.label = tk.Label(self.root, text="text test")
        self.label.pack(padx=10,pady=10)
        
        # self.entry_label
        
        self.textbox = tk.Text(self.root, height=5)
        self.textbox.bind("<KeyPress>",self.shortcut)
        self.textbox.pack(padx=10,pady=10)
        
        self.check_state = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root, text='Show Messagebox',variable=self.check_state)
        self.check.pack(padx=10,pady=10)        
        
        self.button = tk.Button(self.root, text = 'Show Message',command=self.show_message)
        self.button.pack(padx=10,pady=10)
        
        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0',tk.END))
        else:
            messagebox.showinfo(title="message", message=self.textbox.get('1.0',tk.END))
            
    def shortcut(self, event):
        if event.keysym == "Return":
            self.show_message()
        
# MyGUI()
        
    
    
"""   
    
    
root = tk.Tk()

root.geometry("800x500")
root.title("BATTLESHIP")

label = tk.Label(root, text="testing",font=('Noto Sans Mono CJK TC',18))
label.pack(padx=20, pady=20)    #location of 'label'

textbox = tk.Text(root, height= 10, font = ('Noto Sans Mono CJK TC', 16))
textbox.pack(padx=10,pady=10)

# For single line data entry
# myentry = tk.Entry(root)
# myentry.pack()

button = tk.Button(root, text="click Me!",font=('Arial',18))
button.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0,weight=1)
buttonframe.columnconfigure(1,weight=1)
buttonframe.columnconfigure(2,weight=1)

btn1 = tk.Button(buttonframe, text="1")
btn1.grid(row=0,column=0, sticky=tk.W+tk.E)
btn2 = tk.Button(buttonframe, text="2")
btn2.grid(row=0,column=1, sticky=tk.W+tk.E)
btn3 = tk.Button(buttonframe, text="3")
btn3.grid(row=0,column=2, sticky=tk.W+tk.E)
btn4 = tk.Button(buttonframe, text="4")
btn4.grid(row=1,column=0, sticky=tk.W+tk.E)
btn5 = tk.Button(buttonframe, text="5")
btn5.grid(row=1,column=1, sticky=tk.W+tk.E)
btn6 = tk.Button(buttonframe, text="6")
btn6.grid(row=1,column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')

root.mainloop()
"""