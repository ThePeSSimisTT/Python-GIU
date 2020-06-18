from tkinter import*
import Firms_Result
import Firms_Add


def ShowRecords_for_firms(root):     
    root_results = Toplevel(root)
    root_results.geometry("800x800")

#-------------resizing image-----------------------
    #icon=Image.open('Serach.png')
    #icon=icon.resize((30,30),Image.ANTIALIAS)
    #icon.save("Search.png","png")
#--------------------------------------------------

    f=Frame(root_results,width = 1000,height=100,relief=SUNKEN,bd=5)
    f.grid_propagate(0)
    f.grid(row=0,column=0,rowspan=10,columnspan=100)

    root_results.photo=PhotoImage(file="Add.png", master = root_results)
    
    b=Button(f,image = root_results.photo,width="30",height="30")
    b.grid(row=0,column=0,sticky=W+E)
    b.bind('<Button-1>',lambda event,root=root_results:Firms_Add.Add(root))
    
    r=Button(f,image = root_results.photo,width="30",height="30")
    r.grid(row=0,column=1,sticky=W)
    r.bind('<Button-1>',lambda event,root=root_results:Firms_Result.Normal_Results(root_results))

    e=Entry(f,width=10)
    e.grid(row=0,column=4,pady=2,sticky=W+E+N+S)
     
    var=StringVar(f)
    var.set("ЕИК")

    def get(event):
        s.bind('<Button-1>',lambda event,sel=var.get(),root=root_results,ent=e:Firms_Result.Search(sel,root,ent))
    
    s=Button(f,image = root_results.photo,width="30",height="30")
    s.grid(row=0,column=5,padx=2)
    s.bind('<Button-1>',lambda event,sel=var.get(),root=root_results,ent=e:Firms_Result.Search(sel,root,ent))
    
    drop=OptionMenu(f,var,"ЕИК", "Име", "Управител", "Държава", "Град",command=get)
    drop.config(width="10")
    drop.grid(row=0,column=3,sticky=E+N+S)

    beautify=Label(f,width="5")
    beautify.grid(row=0,column=2)
    
    Firms_Result.Normal_Results(root_results)
