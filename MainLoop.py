from tkinter import*
import MainLoopMenu



def MainEvent():
    root_main = Tk()
    root_main.state('zoomed')

    width_full = root_main.winfo_screenwidth()
    f=Frame(root_main,width = width_full,height=100,relief=SUNKEN,bd=5)
    f.grid_propagate(0)
    f.grid(row=0,column=0,rowspan=10,columnspan=100)

    photo = PhotoImage(file="Add.png", master=root_main)
    b=Button(f,image=photo,width = 30)
    b.grid(row=0,column=0)
    #b.bind('<Button-1>',lambda event,root=root_results:Cars_Add.Add(root))

    var=StringVar(f)
    var.set("Регистрационен номер")
    
    def get(event):
        #s.bind('<Button-1>',lambda event,sel=var.get(),root=root_results,ent=e:Cars_Result.Search(sel,root,ent))
        print()
    drop=OptionMenu(f,var,"Регистрационен номер", "Дата", "ID",command=get)
    drop.grid(row=1,column=0,sticky="ew")

    e=Entry(f,width=30)
    e.grid(row=1,column=1)

    s=Button(f, text="Search",width = 30)
    s.grid(row=1,column=2)
    #s.bind('<Button-1>',lambda event,sel=var.get(),root=root_results,ent=e:Cars_Result.Search(sel,root,ent))

    ent_col1=Entry(root_main, width=40)
    ent_col2=Entry(root_main, width=40)
    ent_col3=Entry(root_main, width=40)
    lab_col1=Label(root_main, text = "ID")
    lab_col2=Label(root_main, text = "Регистрациаонен номер")
    lab_col3=Label(root_main, text = "Марка")

    lab_col1.grid(row =16 ,column=0)
    lab_col2.grid(row =16 ,column=1)
    lab_col3.grid(row =16 ,column=2)

    ent_col1.grid(row =17 ,column=0)
    ent_col2.grid(row =17 ,column=1)
    ent_col3.grid(row =17 ,column=2)

    MainLoopMenu.main_menu(root_main)

    root_main.mainloop()
MainEvent()
