from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Invitation_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Invitation Management")
        self.root.geometry("1465x835+230+80")

        self.var_ref=StringVar()
        self.var_event=StringVar()
        self.var_user=StringVar()
        self.var_attend=BooleanVar()

        # Title
        lbl_title = Label(
            self.root, text="Manage Invitations", font=("times new roman", 20, "bold"),
            bg="green", fg="white", bd=4, relief=RIDGE
        )
        lbl_title.place(x=0,y=0,width=1708,height=50)

        # Main Frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=5,y=50,width=420,height=780)

        # Labels and Entries
        lbl_invitation_id = Label(main_frame, text="Invitation ID:", font=("arial", 12, "bold"), padx=2,pady=6)
        lbl_invitation_id.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.txt_invitation_id = ttk.Entry(main_frame, textvariable=self.var_ref, font=("times new roman", 14), width=20,state="readonly")
        self.txt_invitation_id.grid(row=0, column=1)
        
        lbl_event_id = Label(main_frame, text="Event ID:", font=("arial", 12, "bold"), padx=2,pady=6)
        lbl_event_id.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.txt_event_id = ttk.Entry(main_frame, textvariable=self.var_event, font=("times new roman", 14), width=20)
        self.txt_event_id.grid(row=1, column=1)
        
        lbl_user_id = Label(main_frame, text="User ID:", font=("arial", 12, "bold"), padx=2,pady=6)
        lbl_user_id.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.txt_user_id = ttk.Entry(main_frame, textvariable=self.var_user, font=("times new roman", 14), width=20)
        self.txt_user_id.grid(row=2, column=1)
        
        lbl_attend_id = Label(main_frame, text="Attend", font=("arial", 12, "bold"), padx=2,pady=6)
        lbl_attend_id.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        self.txt_attend_id = Checkbutton(main_frame, variable=self.var_attend, offvalue=FALSE, onvalue=TRUE, font=("times new roman", 14), width=20)
        self.txt_attend_id.grid(row=3, column=1)

        btn_frame=Frame(main_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial", 12, "bold"),bg="green",fg="white",width=9)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial", 12, "bold"),bg="green",fg="white",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial", 12, "bold"),bg="green",fg="white",width=9)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial", 12, "bold"),bg="green",fg="white",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        # Display Data Frame
        data_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details & Search", font=("times new roman", 12, "bold"),padx=2)
        data_frame.place(x=435,y=50,width=990,height=780)

        lblSearchBy=Label(data_frame,font=("arial", 12, "bold"),text="Search By", bg="orange", fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W, padx=2)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(data_frame,textvariable=self.search_var,font=("arial", 12, "bold"),width=24,state="readonly")
        combo_Search["value"]=("Ref", "Event", "User")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1, padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(data_frame,textvariable=self.txt_search,font=("arial", 13, "bold"),width=34)
        txtSearch.grid(row=0,column=2, padx=2)
        
        btnSearch=Button(data_frame,text="Search",command=self.search,font=("arial", 12, "bold"),bg="green",fg="white",width=13)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShow=Button(data_frame,text="Show All",command=self.fetch_data,font=("arial", 12, "bold"),bg="green",fg="white",width=13)
        btnShow.grid(row=0,column=4,padx=1)
        
        details_table=Frame(data_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=975,height=650)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)
        self.data_table = ttk.Treeview(
            details_table, columns=("ID", "Event", "User", "Attend"), xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.data_table.xview)
        scroll_y.config(command=self.data_table.yview)

        self.data_table.heading("ID", text="ID")
        self.data_table.heading("Event", text="Event")
        self.data_table.heading("User", text="User")
        self.data_table.heading("Attend", text="Attend")
        self.data_table["show"] = "headings"
        self.data_table.column("ID", width=100)
        self.data_table.column("Event", width=100)
        self.data_table.column("User", width=100)
        self.data_table.heading("Attend", text="Attend")
        
        self.data_table.pack(fill=BOTH, expand=1)
        self.data_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    def add_data(self):
        if  (not self.var_event.get().strip() or
            not self.var_user.get().strip()):
            messagebox.showwarning("Error", "All entries must be filled!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
                my_cursor=conn.cursor()
                query = """
                        INSERT INTO Invitation (EventID, UserID, Attend) 
                        VALUES (%s, %s, %s)
                        """
                        
                values = (
                self.var_event.get(),
                self.var_user.get(),
                self.var_attend.get(),
                )
                
                my_cursor.execute(query,values)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "invitation has been added",parent=self.root)
                
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
                SELECT * FROM Invitation
                """
        my_cursor.execute(query)
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.data_table.delete(*self.data_table.get_children())
            for i in rows:
                self.data_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.data_table.focus()
        content=self.data_table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0])
        self.var_event.set(row[1]),
        self.var_user.set(row[2]),
    
    def update(self):
        if (not self.var_event.get().strip() or
            not self.var_user.get().strip()):
            messagebox.showwarning("Error", "All entries must be filled!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
                my_cursor=conn.cursor()
                query = """
                        UPDATE Invitation
                        SET EventID=%s, UserID=%s, Attend=%s
                        WHERE InvitationID=%s
                        """
                values = (
                            self.var_event.get(),
                            self.var_user.get(),
                            self.var_attend.get(),
                        )
                my_cursor.execute(query,values)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "invitation details has been updated",parent=self.root)
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
        mDelete=messagebox.askyesno("Event Management System","Do you  want to delete this invitation", parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
            my_cursor=conn.cursor()
            query = """
                    DELETE FROM Invitation WHERE InvitationID=%s
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
        self.var_event.set(""),
        self.var_user.set(""),
        self.var_attend.set(FALSE)
    
    def search(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
            my_cursor=conn.cursor()
            
            column_mapping = {
            "Ref": "InvitationID",
            "Event": "EventID",
            "User": "UserID",
            "Attend": "Attend",
            }

            search_field = self.search_var.get()
            search_value = self.txt_search.get()
            
            column=column_mapping[search_field]

            if search_field not in column_mapping:
                messagebox.showerror("Error", "Invalid search field selected.", parent=self.root)
                return
            
            else:
                query = f"SELECT * FROM Invitation WHERE {column_mapping[search_field]} LIKE %s"
                value=(f"%{self.txt_search.get()}%",)
                
            my_cursor.execute(query,value)
            rows=my_cursor.fetchall()
            
            if len(rows)!=0:
                self.data_table.delete(*self.data_table.get_children())
                for i in rows:
                    self.data_table.insert("",END, values=i)
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
    root = Tk()
    obj = Invitation_Win(root)
    root.mainloop()