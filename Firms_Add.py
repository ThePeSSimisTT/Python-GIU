from tkinter import*
import Database
import Firms_Result

def Add(root_results):
    def Push(event):
        connection = Database.DatabaseConnectionError();
        cursor = connection.cursor()
            
        sql_insert_firm_Query = "INSERT INTO `firm` (`EIK`, `name`, `shefa`) VALUES ('"+entry[0].get()+"', '"+entry[1].get()+"', '"+entry[2].get()+"');"
        sql_insert_address_Query="INSERT INTO `address` (`city`, `street`, `street_num`, `country`) VALUES ('"+entry[4].get()+"', '"+entry[5].get()+"', '"+entry[6].get()+"', '"+entry[3].get()+"');"
        sql_insert_fk_Query="UPDATE `firm` SET `address_id` = (SELECT id FROM address order by id desc limit 1) order by id desc limit 1;"
        cursor.execute(sql_insert_firm_Query)
        cursor.execute(sql_insert_address_Query)
        cursor.execute(sql_insert_fk_Query)

        connection.commit()
        connection.close()
    def Destroy(event):
        root_add.destroy()

    root_add=Toplevel(root_results)
    entry=[]
    tags=["ЕИК","Име","Управител","Държава","Град","Улица","Номер"]
    for x,y in zip(range(7),tags):
        Label(root_add,text = y).grid(row=0,column=x)
        e=Entry(root_add)
        entry.append(e)
        entry[-1].grid(row=1,column=x)

    b=Button(root_add, text="Push")
    b.grid(row=2,column=3)
    b.bind('<Button-1>',Push,add="+")
    b.bind('<Button-1>',lambda event,root=root_results:Firms_Result.Normal_Results(root),add="+")
    b.bind('<Button-1>',Destroy,add="+")
