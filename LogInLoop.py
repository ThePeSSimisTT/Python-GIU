from tkinter import*
import Database
import MainLoop
    
def LogIn_Window():

    def LogIn(event):
        flag=0

        connection = Database.DatabaseConnectionError();
        cursor = connection.cursor()
         
        t_password=ent_password.get()
        t_name=ent_name.get()
         
        sql_select_Query = "select * from users"
        cursor.execute(sql_select_Query)
        records=cursor.fetchall()
                
        for row in records:
            if row[1]==t_name and row[2]==t_password:
                flag=1
        if flag==1:
            root.destroy()
            MainLoop.MainEvent()
        l_r.set("Wrong Password or Username")
            
    root = Tk()
    root.state('zoomed')
    
    lab_name=Label(root, text="Потребител")
    lab_password=Label(root, text="Парола")
    
    ent_name=Entry(root, width=40)
    ent_password=Entry(root,show ='*', width=40)
    
    but_ok=Button(root, text="OK")

    lab_name.pack()
    ent_name.pack()
    lab_password.pack()
    ent_password.pack()

    l_r = StringVar(root)
    lable_result=Label(root,textvariable = l_r,width=40)
    lable_result.pack()
    def set_label(event):
        l_r.set("")
    
    but_ok.pack()
    but_ok.bind('<Button-1>',LogIn)
    ent_password.bind ('<Return>',LogIn,add='+')
    ent_password.bind ('<FocusIn>',set_label,add='+')
    ent_name.bind ('<Return>',LogIn,add='+')
    ent_name.bind ('<FocusIn>',set_label)
    
       
    root.mainloop()
