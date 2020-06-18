from tkinter import*
import Database


def Results(sql_count_Query,sql_select_Query,root_results):
    connection = Database.DatabaseConnectionError();
    cursor = connection.cursor()
    
    cursor.execute(sql_count_Query)
    number=int(cursor.fetchone()[0])

    cursor.execute(sql_select_Query)
    records=cursor.fetchall()

#-------------lables--------------------------------------------------------------------
    tags=["ЕИК","Име","Управител","Държава","Град","Улица","Номер"]
    for x,y in zip(tags,range(2,9)):
        Label(root_results,text = x).grid(row=11,column=y)

    Results.r_save=0
    entries=[]
    text=[]
#---removing the marking wrom the row when another is double clicked----------------------------------
    def clear_double_click(r):
        for x in range(1,9):
            entries[r+x].configure(readonlybackground="white",fg="black")
#---marking the whole row when double clicked----------------------------------------------
    def double_click(r):
        r=r-12
        r=r*9
        clear_double_click(Results.r_save)
        for x in range(1,9):
            entries[r+x].configure(readonlybackground="#0078D7",fg="#FFFFFF")
        Results.r_save=r
#---edit function------------------------------------------------------------------------
    def Edit(r):
        connection = Database.DatabaseConnectionError();
        cursor = connection.cursor()
        
        root_edit = Tk()
        r=r-12
        r=r*9
        
        text_edit=[]
        entry_edit=[]

#---labels and entry for label root------------------------------------------------------------------        
        for x in range(1,9):
            var=StringVar(root_edit, value=entries[r+x].get())
            text_edit.append(var)
        for x,y in zip(tags,range(7)):
            Label(root_edit,text = x).grid(row=0,column=y)
            e=Entry(root_edit,textvariable=text_edit[y])
            entry_edit.append(e)
            e.grid(row=1,column=y)
        
        ed=Button(root_edit, text="Edit")
        de=Button(root_edit, text="Delete")
#---destroy edit root----------------------------------------------------------------------------
        def Destroy_Edit(root):
            root.destroy()

#---delete event in edit root----------------------------------------------------------------------------
        def Delete_Edit(event):
            connection = Database.DatabaseConnectionError();
            cursor = connection.cursor()
            
            cursor.execute("UPDATE `owner` SET `firm_id` = NULL WHERE (`firm_id` = '"+entries[r+1].get()+"')")
            connection.commit()
            
            cursor.execute("DELETE FROM `firm` WHERE (`id` = "+entries[r+1].get()+")")
            connection.commit()
            
            cursor.execute("DELETE FROM `address` WHERE (`id` = (SELECT address_id FROM firm where id = "+entries[r+1].get()+"))")
            connection.commit()
            connection.close()

#---edit event in edit root----------------------------------------------------------------------------
        def Edit_Edit(event):
            connection = Database.DatabaseConnectionError();
            cursor = connection.cursor()
            
            cursor.execute("UPDATE `autonebg`.`firm` SET `EIK` = '"+entry_edit[1].get()+"', `name` = '"+entry_edit[2].get()+"', `shefa` = '"+entry_edit[3].get()+"' WHERE (`id` = '"+entries[r+1].get()+"')")
            connection.commit()

            cursor.execute("UPDATE `autonebg`.`address` SET `city` = '"+entry_edit[4].get()+"', `street` = '"+entry_edit[5].get()+"', `street_num` = '"+entry_edit[7].get()+"', `country` = '"+entry_edit[6].get()+"' WHERE (`id` = (SELECT address_id FROM firm where id = "+entries[r+1].get()+"))")
            connection.commit()
            connection.close()

        dummy=StringVar(root_edit,value="")
        de.grid(row=2,column=1)
        de.bind('<Button-1>',Delete_Edit,add="+")
        de.bind('<Button-1>',lambda event,s="",root=root_results,e=dummy:Search(s,root,e),add="+")
        de.bind('<Button-1>',lambda event,root=root_edit:Destroy_Edit(root),add="+")

        ed.grid(row=2,column=0)
        ed.bind('<Button-1>',Edit_Edit,add="+")
        ed.bind('<Button-1>',lambda event,root=root_results:Normal_Results(root),add="+")
        ed.bind('<Button-1>',lambda event,root=root_edit:Destroy_Edit(root),add="+")
#-------END OF EDIT-------------------------------------------------------------------------------------
    n=0
    r=12
#---placing all elements---------------------------------------------------------------
    for n in range(number):
        for x in range(0,8):
            var=StringVar(root_results, value=records[n][x])
            text.append(var)
        entries.append(Entry(root_results,relief=RAISED,width=2,state='disabled',disabledbackground="gray",))
        entries[-1].bind('<Button-1>',lambda event,row=r:double_click(row))
        entries[-1].bind('<Double-Button-1>',lambda event,row=r:Edit(row))
        entries[-1].grid(row=r,column=0)
        for y in range(0,8):
            e=Entry(root_results,textvariable=text[y],state='readonly',readonlybackground="white")
            entries.append(e)
            entries[-1].bind('<Button-1>',lambda event,row=r:double_click(row))
            entries[-1].bind('<Double-Button-1>',lambda event,row=r:Edit(row))
            entries[-1].grid(row=r,column=y+1)
        r=r+1
        text.clear()
        
def Normal_Results(root_results):
    sql_count_Query = "select count(id) from firm"
    sql_select_Query = "SELECT f.id,f.EIK,f.`name`,f.shefa,a.country,a.city,a.street,a.street_num FROM firm as f inner join address as a ON a.id=f.address_id order by f.id"
    Results(sql_count_Query,sql_select_Query,root_results)
def Search(sel,root_results,e):
    search_par="f.EIK"
    if sel == "ЕИК" : search_par="f.EIK"
    elif sel == "Име" : search_par="f.`name`"
    elif sel == "Управител" : search_par="f.shefa"
    elif sel == "Държава" : search_par="a.country"
    elif sel == "Град" : search_par="a.city"
    
    sql_count_Query = "select count(f.id) from firm as f inner join address as a ON a.id=f.address_id where "+search_par+" like '" + e.get() + "%'"
    sql_select_Query = "SELECT f.id,f.EIK,f.`name`,f.shefa,a.country,a.city,a.street,a.street_num FROM firm as f inner join address as a ON a.id=f.address_id where "+search_par+" like '" + e.get() + "%' order by f.id"
    clear(root_results)
    Results(sql_count_Query,sql_select_Query,root_results)
def clear(root_results):
    list = root_results.grid_slaves()
    for l in list:
        if(str(type(l)) != "<class 'tkinter.Frame'>"):
            l.destroy()
