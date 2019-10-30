from tkinter import *
from tkinter import ttk
class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title("Bai5")
        self.minsize(640,400)
        #self.wm_iconbitmap('icon.ico')
        #self.configure(background='#4D4D4D')
        
        #self.label = ttk.Label(self,text="Label1")
        #self.label.grid(column = 1 ,row = 0)
        
        #self.button = ttk.Button(self,text="Label1",command=self.clickMe)
        #self.button.grid(column = 0 ,row = 0)
        self.initUI()
    
    def initUI(self):
        self.name = StringVar()
        self.label = ttk.Label(self,text="Label1")
        self.label.grid(column = 0 ,row = 0)
        
        self.textbox = ttk.Entry(self,width = 20, textvariable = self.name)
        self.textbox.grid(column = 0 , row = 1)
        
        self.button = ttk.Button(self,text="Label1",command=self.clickMe)
        self.button.grid(column = 0 ,row = 3)

    
    def clickMe(self):
        print("click me")
        self.label.configure(text="clicked" + self.name.get())
        self.label.configure(foreground="green")
        
        
        


root = Root()
root.mainloop()

