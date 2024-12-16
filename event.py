from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry

class Event_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Event Management System")
        self.root.geometry("1465x835+230+80")
        
        self.var_ref=StringVar()
        self.var_name=StringVar()
        self.var_type=StringVar()
        self.var_desc=StringVar()
        self.var_date=StringVar()
        self.var_capacity=StringVar()
        self.var_venue=StringVar()
        self.var_catering=StringVar()
        self.var_user=StringVar()
        self.var_organizer=StringVar()
        
        lbl_title = Label(self.root, text="Add Event Details", font=("times new roman", 38, "bold"), bg="green", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1708,height=50)
        
        labelframleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Event Details", font=("times new roman", 12, "bold"),padx=2)
        labelframleft.place(x=5,y=50,width=420,height=780)
        
        eref=Label(labelframleft,text="Ref", font=("arial", 12, "bold"), padx=2,pady=6)
        eref.grid(row=0,column=0,sticky=W)
        txtRef=ttk.Entry(labelframleft,textvariable=self.var_ref,font=("arial", 13, "bold"),width=29,state="readonly")
        txtRef.grid(row=0,column=1)
        
        ename=Label(labelframleft,text="Name", font=("arial", 12, "bold"), padx=2,pady=6)
        ename.grid(row=1,column=0,sticky=W)
        txtName=ttk.Entry(labelframleft,textvariable=self.var_name,font=("arial", 13, "bold"),width=29)
        txtName.grid(row=1,column=1)
        
        etype=Label(labelframleft,text="Type", font=("arial", 12, "bold"), padx=2,pady=6)
        etype.grid(row=2,column=0,sticky=W)
        combo_type=ttk.Combobox(labelframleft,textvariable=self.var_type,font=("arial", 12, "bold"),width=27,state="readonly")
        combo_type["value"]=("Birthday Party", "Wedding", "Conference", "Seminar", "Other")
        combo_type.grid(row=2,column=1)
        
        edesc=Label(labelframleft,text="Description", font=("arial", 12, "bold"), padx=2,pady=6)
        edesc.grid(row=3,column=0,sticky=W)
        txtDesc=ttk.Entry(labelframleft,textvariable=self.var_desc,font=("arial", 13, "bold"),width=29)
        txtDesc.grid(row=3,column=1)
        
        edate=Label(labelframleft,text="Date", font=("arial", 12, "bold"), padx=2,pady=6)
        edate.grid(row=4,column=0,sticky=W)
        txtDate = DateEntry(
            labelframleft,
            textvariable=self.var_date,
            font=("arial", 13, "bold"),
            width=27,
            background="darkblue",
            foreground="white",
            borderwidth=2,
            date_pattern="yyyy-mm-dd"  # Format: YYYY-MM-DD
        )
        txtDate.grid(row=4, column=1)
        
        ecapacity=Label(labelframleft,text="Capacity", font=("arial", 12, "bold"), padx=2,pady=6)
        ecapacity.grid(row=5,column=0,sticky=W)
        txtCapacity=ttk.Entry(labelframleft,textvariable=self.var_capacity,font=("arial", 13, "bold"),width=29)
        txtCapacity.grid(row=5,column=1)
        
        venue=Label(labelframleft,text="Venue", font=("arial", 12, "bold"), padx=2,pady=6)
        venue.grid(row=6,column=0,sticky=W)
        txtVenue=ttk.Entry(labelframleft,textvariable=self.var_venue,font=("arial", 13, "bold"),width=29)
        txtVenue.grid(row=6,column=1)
        
        catering=Label(labelframleft,text="Catering", font=("arial", 12, "bold"), padx=2,pady=6)
        catering.grid(row=7,column=0,sticky=W)
        txtCatering=ttk.Entry(labelframleft,textvariable=self.var_catering,font=("arial", 13, "bold"),width=29)
        txtCatering.grid(row=7,column=1)
        
        user=Label(labelframleft,text="User", font=("arial", 12, "bold"), padx=2,pady=6)
        user.grid(row=8,column=0,sticky=W)
        txtUser=ttk.Entry(labelframleft,textvariable=self.var_user,font=("arial", 13, "bold"),width=29)
        txtUser.grid(row=8,column=1)
        
        organizer=Label(labelframleft,text="Organizer", font=("arial", 12, "bold"), padx=2,pady=6)
        organizer.grid(row=9,column=0,sticky=W)
        txtOrganizer=ttk.Entry(labelframleft,textvariable=self.var_organizer,font=("arial", 13, "bold"),width=29)
        txtOrganizer.grid(row=9,column=1)
        
        btn_frame=Frame(labelframleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial", 12, "bold"),bg="green",fg="white",width=9)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial", 12, "bold"),bg="green",fg="white",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial", 12, "bold"),bg="green",fg="white",width=9)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial", 12, "bold"),bg="green",fg="white",width=9)
        btnReset.grid(row=0,column=3,padx=1)
        
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details & Search", font=("times new roman", 12, "bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=990,height=780)
        
        lblSearchBy=Label(Table_Frame,font=("arial", 12, "bold"),text="Search By", bg="orange", fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W, padx=2)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial", 12, "bold"),width=24,state="readonly")
        combo_Search["value"]=("Ref", "Type", "Date", "Venue", "Catering", "User", "Organizer")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1, padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial", 13, "bold"),width=34)
        txtSearch.grid(row=0,column=2, padx=2)
        
        btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial", 12, "bold"),bg="green",fg="white",width=13)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShow=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial", 12, "bold"),bg="green",fg="white",width=13)
        btnShow.grid(row=0,column=4,padx=1)
        
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=975,height=650)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Event_Details_Table=ttk.Treeview(details_table,columns=("Ref", "Name", "Type", "Description", "Date", "Capacity","Venue", "Catering","User","Organizer"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Event_Details_Table.xview)
        scroll_y.config(command=self.Event_Details_Table.yview)
        
        self.Event_Details_Table.heading("Ref", text="Refer No")
        self.Event_Details_Table.heading("Name", text="Name")
        self.Event_Details_Table.heading("Type", text="Type")
        self.Event_Details_Table.heading("Description", text="Description")
        self.Event_Details_Table.heading("Date", text="Date")
        self.Event_Details_Table.heading("Capacity", text="Capacity")
        self.Event_Details_Table.heading("Venue", text="Venue")
        self.Event_Details_Table.heading("Catering", text="Catering")
        self.Event_Details_Table.heading("User", text="User")
        self.Event_Details_Table.heading("Organizer", text="Organizer")
        
        self.Event_Details_Table["show"]="headings"
        
        self.Event_Details_Table.column("Ref",width=100)
        self.Event_Details_Table.column("Name",width=100)
        self.Event_Details_Table.column("Type",width=100)
        self.Event_Details_Table.column("Description",width=100)
        self.Event_Details_Table.column("Date",width=100)
        self.Event_Details_Table.column("Capacity",width=100)
        self.Event_Details_Table.column("Venue",width=100)
        self.Event_Details_Table.column("Catering",width=100)
        self.Event_Details_Table.column("User",width=100)
        self.Event_Details_Table.column("Organizer",width=100)
        
        self.Event_Details_Table.pack(fill=BOTH,expand=1)
        self.Event_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if  (not self.var_name.get().strip() or
            not self.var_type.get().strip() or
            not self.var_date.get().strip() or
            not self.var_capacity.get().strip() or
            not self.var_venue.get().strip() or
            not self.var_catering.get().strip() or
            not self.var_user.get().strip()):
            messagebox.showwarning("Error", "All entries except description & organizer must be filled!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
                my_cursor=conn.cursor()
                query = """
                        INSERT INTO Event (EventName, EventType, EventDetails, EventDate, EventCapacity, VenueID, CateringTypeID, UserID, OrganizerID) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
                        
                values = (
                self.var_name.get(),
                self.var_type.get(),
                self.var_desc.get(),
                self.var_date.get(),
                self.var_capacity.get(),
                self.var_venue.get(),
                self.var_catering.get(),
                self.var_user.get(),
                self.var_organizer.get(),
                )
                
                my_cursor.execute(query,values)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "event has been added",parent=self.root)
                
            except mysql.connector.Error as err:
                # Parse and handle specific MySQL errors
                error_message = str(err)

                # Data too long for a column
                if "Data too long" in error_message:
                    messagebox.showerror("Database Error", "One of the inputs exceeds the maximum allowed length.", parent=self.root)
                
                # Incorrect integer or decimal value
                elif "Incorrect integer value" in error_message or "Incorrect decimal value" in error_message:
                    messagebox.showerror("Database Error", "Numeric fields must contain valid numbers.", parent=self.root)
                    
                elif "FOREIGN KEY constraint fails" in error_message:
                    messagebox.showerror("Database Error", "Invalid Venue/Catering/User/Organizer ID: The specified venue does not exist.", parent=self.root)

                # Catch-all for other MySQL errors
                else:
                    messagebox.showerror("Database Error", f"An error occurred: {error_message}", parent=self.root)

            except Exception as es:
                # Generic exception handling
                messagebox.showerror("Error", f"Something went wrong: {str(es)}", parent=self.root)
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
        my_cursor=conn.cursor()
        query = """
                SELECT * FROM Event
                """
        my_cursor.execute(query)
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Event_Details_Table.delete(*self.Event_Details_Table.get_children())
            for i in rows:
                self.Event_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.Event_Details_Table.focus()
        content=self.Event_Details_Table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0])
        self.var_name.set(row[1]),
        self.var_type.set(row[2]),
        self.var_desc.set(row[3]),
        self.var_date.set(row[4]),
        self.var_capacity.set(row[5]),
        self.var_venue.set(row[6]),
        self.var_catering.set(row[7]),
        self.var_user.set(row[8]),
        self.var_organizer.set(row[9]),
    
    def update(self):
        if (not self.var_name.get().strip() or
            not self.var_type.get().strip() or
            not self.var_date.get().strip() or
            not self.var_capacity.get().strip() or
            not self.var_venue.get().strip() or
            not self.var_catering.get().strip() or
            not self.var_user.get().strip()):
            messagebox.showwarning("Error", "All entries except description and organizer must be filled!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
                my_cursor=conn.cursor()
                query = """
                        UPDATE Event 
                        SET EventName=%s, EventType=%s, EventDetails=%s, EventDate=%s, EventCapacity=%s, VenueID=%s, CateringTypeID=%s, UserID=%s, OrganizerID=%s
                        WHERE EventID=%s
                        """
                values = (
                            self.var_name.get(),
                            self.var_type.get(),
                            self.var_desc.get(),
                            self.var_date.get(),
                            self.var_capacity.get(),
                            self.var_venue.get(),
                            self.var_catering.get(),
                            self.var_user.get(),
                            self.var_organizer.get(),
                        )
                my_cursor.execute(query,values)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "event details has been updated",parent=self.root)
            except mysql.connector.Error as err:
                # Parse and handle specific MySQL errors
                error_message = str(err)

                # Data too long for a column
                if "Data too long" in error_message:
                    messagebox.showerror("Database Error", "One of the inputs exceeds the maximum allowed length.", parent=self.root)
                
                # Incorrect integer or decimal value
                elif "Incorrect integer value" in error_message or "Incorrect decimal value" in error_message:
                    messagebox.showerror("Database Error", "Numeric fields must contain valid numbers.", parent=self.root)

                elif "FOREIGN KEY constraint fails" in error_message:
                    messagebox.showerror("Database Error", "Invalid Venue/Catering/User/Organizer ID: The specified venue does not exist.", parent=self.root)

                # Catch-all for other MySQL errors
                else:
                    messagebox.showerror("Database Error", f"An error occurred: {error_message}", parent=self.root)

            except Exception as es:
                # Generic exception handling
                messagebox.showerror("Error", f"Something went wrong: {str(es)}", parent=self.root)
    
    def mDelete(self):
        mDelete=messagebox.askyesno("Event Management System","Do you  want to delete this event", parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
            my_cursor=conn.cursor()
            query = """
                    DELETE FROM Event WHERE EventID=%s
                    """
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not mDelete:
                return 
        conn.commit()
        self.fetch_data()
        conn.close()
    
    def reset(self):
        self.var_ref.set("")
        self.var_name.set(""),
        self.var_type.set(""),
        self.var_desc.set(""),
        self.var_date.set(""),
        self.var_capacity.set(""),
        self.var_venue.set(""),
        self.var_catering.set(""),
        self.var_user.set(""),
        self.var_organizer.set(""),
    
    def search(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
            my_cursor=conn.cursor()
            
            column_mapping = {
            "Ref": "EventID",
            "Type": "EventType",
            "Date": "EventDate",
            "Venue": "VenueID",
            "Catering": "CateringTypeID",
            "User": "UserID",
            "Organizer": "OrganizerID",
            }

            search_field = self.search_var.get()
            search_value = self.txt_search.get()
            
            column=column_mapping[search_field]

            if search_field not in column_mapping:
                messagebox.showerror("Error", "Invalid search field selected.", parent=self.root)
                return
            
            else:
                query = f"SELECT * FROM Event WHERE {column_mapping[search_field]} LIKE %s"
                value=(f"%{self.txt_search.get()}%",)
                
            my_cursor.execute(query,value)
            rows=my_cursor.fetchall()
            
            if len(rows)!=0:
                self.Event_Details_Table.delete(*self.Event_Details_Table.get_children())
                for i in rows:
                    self.Event_Details_Table.insert("",END, values=i)
                conn.commit()
            else:
                messagebox.showinfo("Info", "No matching records found.", parent=self.root)
            conn.close()
            
        except mysql.connector.Error as err:
            # Handle MySQL-specific errors
            messagebox.showerror("Database Error", f"An error occurred: {err}", parent=self.root)
            print(f"MySQL Error: {err}")

        except Exception as ex:
            # Handle other errors
            messagebox.showerror("Error", f"Something went wrong: {str(ex)}", parent=self.root)
            print(f"General Error: {str(ex)}")

if __name__ == "__main__":
    root=Tk()
    obj=Event_Win(root)
    root.mainloop()