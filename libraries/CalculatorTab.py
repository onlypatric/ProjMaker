
from tkinter import Tk;
from tkinter.ttk import *;


class CalculatorTab:
    def __init__(self,root:Frame) -> None:
        self.root=root
        for i in self.root.winfo_children():
            i.pack_forget()
#----------------------------------------------< for margin top >
        self.empty_label=Label(self.root,text="",font=("Segoe UI","30","bold"))
        self.empty_label.pack(side="top",fill="x")
#----------------------------------------------< for border width >
        self.calc_container_container=Frame(self.root,border="10")
        self.calc_container_container.pack(side="top",fill="x")
#----------------------------------------------< for frame >
        self.calc_container=LabelFrame(self.calc_container_container,text="Risultato",border="10")
        self.calc_container.pack(side="top",fill="x")
#----------------------------------------------< for actual label >
        self.calc_label=Label(self.calc_container,text="= 0",font=("Segoe UI","30","bold"),border="20",justify="right",anchor="e")
        self.calc_label.pack(side="top",fill="x",anchor="e")
#----------------------------------------------< for buttons layer 1 >
        self.buttons_label_1=Frame(self.root,border="5")
        self.buttons_label_1.pack(side="top",fill="x")
#----------------------------------------------< buttons layer 1 >
