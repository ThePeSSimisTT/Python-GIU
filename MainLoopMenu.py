from tkinter import*
import Cars
import Models
import Firms

def main_menu(root_main):
    m=Menu(root_main)
    root_main.config(menu=m)

    fm=Menu(m,tearoff=0)
    m.add_cascade(label="1",menu=fm)
    fm.add_command(label="Cars",command=lambda:Cars.ShowRecords_for_cars())
    fm.add_command(label="Firms",command=lambda root=root_main:Firms.ShowRecords_for_firms(root))
    fm.add_command(label="Models",command=lambda:Models.ShowRecords_for_models())
    fm.add_command(label="1.3")
    fm.add_command(label="1.4")

    hm =Menu(m)
    m.add_cascade(label="2",menu=hm)
    hm.add_command(label="2.0")
    hm.add_command(label="2.1")
    hm.add_command(label="2.2")
    hm.add_command(label="2.3")
    hm.add_command(label="2.4")

    lm = Menu(m)
    m.add_cascade(label="3",menu=lm)
    lm.add_command(label="3.0")
    lm.add_command(label="3.1")
    lm.add_command(label="3.2")
    lm.add_command(label="3.3")
    lm.add_command(label="3.4")
