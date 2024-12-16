from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class User_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management System - User Details")
        self.root.geometry("1465x835+230+80")

        self.var_ref=StringVar()
        self.var_name=StringVar()
        self.var_lname=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()

        # Title Label
        lbl_title = Label(self.root, text="Add User Details", font=("times new roman", 38, "bold"), bg="green", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1708, height=50)

        # User Details Frame
        labelframe_left = LabelFrame(self.root, bd=2, relief=RIDGE, text="User Details", font=("times new roman", 12, "bold"), padx=2)
        labelframe_left.place(x=5, y=50, width=420, height=780)

        # User Reference
        lbl_user_ref = Label(labelframe_left, text="User Ref", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_user_ref.grid(row=0, column=0, sticky=W)
        self.entry_ref = ttk.Entry(labelframe_left,textvariable=self.var_ref, font=("arial", 13, "bold"),width=29,state="readonly")
        self.entry_ref.grid(row=0, column=1)

        # First Name
        lbl_uname = Label(labelframe_left, text="Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_uname.grid(row=1, column=0, sticky=W)
        self.txt_name = ttk.Entry(labelframe_left,textvariable=self.var_name, font=("arial", 13, "bold"),width=29)
        self.txt_name.grid(row=1, column=1)

        # Last Name
        lbl_ulname = Label(labelframe_left, text="Last Name", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_ulname.grid(row=2, column=0, sticky=W)
        self.txt_lname = ttk.Entry(labelframe_left, textvariable=self.var_lname, font=("arial", 13, "bold"),width=29)
        self.txt_lname.grid(row=2, column=1)

        # Phone Number
        lbl_uphone = Label(labelframe_left, text="Phone Number", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_uphone.grid(row=3, column=0, sticky=W)
        self.txt_phone = ttk.Entry(labelframe_left,textvariable=self.var_phone, font=("arial", 13, "bold"),width=29)
        self.txt_phone.grid(row=3, column=1)

        # Email
        lbl_uemail = Label(labelframe_left, text="Email", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_uemail.grid(row=4, column=0, sticky=W)
        self.txt_email = ttk.Entry(labelframe_left, textvariable=self.var_email, font=("arial", 13, "bold"),width=29)
        self.txt_email.grid(row=4, column=1)

        btn_frame=Frame(labelframe_left,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial", 12, "bold"),bg="green",fg="white",width=9)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial", 12, "bold"),bg="green",fg="white",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial", 12, "bold"),bg="green",fg="white",width=9)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial", 12, "bold"),bg="green",fg="white",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        # Data Table Frame
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE,text="View Details & Search", font=("times new roman", 12, "bold"),padx=2)
        table_frame.place(x=430, y=50, width=990, height=780)

        lblSearchBy=Label(table_frame,font=("arial", 12, "bold"),text="Search By", bg="orange", fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W, padx=2)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(table_frame,textvariable=self.search_var,font=("arial", 12, "bold"),width=24,state="readonly")
        combo_Search["value"]=("Ref", "Name", "Last Name")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1, padx=2)

        self.txt_search=StringVar()
        txtSearch=ttk.Entry(table_frame,textvariable=self.txt_search,font=("arial", 13, "bold"),width=34)
        txtSearch.grid(row=0,column=2, padx=2)
        
        btnSearch=Button(table_frame,text="Search",command=self.search,font=("arial", 12, "bold"),bg="green",fg="white",width=13)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShow=Button(table_frame,text="Show All",command=self.fetch_data,font=("arial", 12, "bold"),bg="green",fg="white",width=13)
        btnShow.grid(row=0,column=4,padx=1)
        
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=975,height=650)

        # Scrollbars
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.user_table = ttk.Treeview(details_table, columns=("ref", "name", "lname", "phone", "email"),
                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.user_table.xview)
        scroll_y.config(command=self.user_table.yview)

        self.user_table.heading("ref", text="User Ref")
        self.user_table.heading("name", text="Name")
        self.user_table.heading("lname", text="Last Name")
        self.user_table.heading("phone", text="Phone")
        self.user_table.heading("email", text="Email")

        self.user_table["show"] = "headings"
        self.user_table.column("ref", width=100)
        self.user_table.column("name", width=200)
        self.user_table.column("lname", width=200)
        self.user_table.column("phone", width=150)
        self.user_table.column("email", width=250)

        self.user_table.pack(fill=BOTH,expand=1)
        self.user_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        # Logic for saving user to the database
        if  (not self.var_name.get().strip() or
            not self.var_lname.get().strip() or
            not self.var_phone.get().strip()):
            messagebox.showwarning("Error", "All entry except email must be filled!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
                my_cursor=conn.cursor()
                query = """
                        INSERT INTO User (UserName, UserLName, UserPhone, UserEmail) 
                        VALUES (%s, %s, %s, %s)
                        """
                        
                values = (
                self.var_name.get(),
                self.var_lname.get(),
                self.var_phone.get(),
                self.var_email.get(),
                )
                
                my_cursor.execute(query,values)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "user has been added",parent=self.root)
                
            except mysql.connector.Error as err:
                # Parse and handle specific MySQL errors
                error_message = str(err)

                # Data too long for a column
                if "Data too long" in error_message:
                    messagebox.showerror("Database Error", "One of the inputs exceeds the maximum allowed length.", parent=self.root)
                
                # Incorrect integer or decimal value
                elif "Incorrect integer value" in error_message or "Incorrect decimal value" in error_message:
                    messagebox.showerror("Database Error", "Numeric fields must contain valid numbers.", parent=self.root)

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
                SELECT * FROM User
                """
        my_cursor.execute(query)
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.user_table.delete(*self.user_table.get_children())
            for i in rows:
                self.user_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.user_table.focus()
        content=self.user_table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0])
        self.var_name.set(row[1]),
        self.var_lname.set(row[2]),
        self.var_phone.set(row[3]),
        self.var_email.set(row[4]),

    def update(self):
        # Logic for updating user details in the database
        if (not self.var_name.get().strip() or
            not self.var_lname.get().strip() or
            not self.var_phone.get().strip()):
            messagebox.showwarning("Error", "All entries except email must be filled!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
                my_cursor=conn.cursor()
                query = """
                        UPDATE User 
                        SET UserName=%s, UserLName=%s, UserPhone=%s, UserEmail=%s
                        WHERE UserID=%s
                        """
                values = (
                    self.var_name.get(),
                    self.var_lname.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_ref.get(),
                    )
                my_cursor.execute(query,values)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "user details has been updated",parent=self.root)
            except mysql.connector.Error as err:
                # Parse and handle specific MySQL errors
                error_message = str(err)

                # Data too long for a column
                if "Data too long" in error_message:
                    messagebox.showerror("Database Error", "One of the inputs exceeds the maximum allowed length.", parent=self.root)
                
                # Incorrect integer or decimal value
                elif "Incorrect integer value" in error_message or "Incorrect decimal value" in error_message:
                    messagebox.showerror("Database Error", "Numeric fields must contain valid numbers.", parent=self.root)

                # Catch-all for other MySQL errors
                else:
                    messagebox.showerror("Database Error", f"An error occurred: {error_message}", parent=self.root)

            except Exception as es:
                # Generic exception handling
                messagebox.showerror("Error", f"Something went wrong: {str(es)}", parent=self.root)

    def mDelete(self):
        # Logic for deleting user from the database
        mDelete=messagebox.askyesno("Event Management System","Do you  want to delete this user", parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
            my_cursor=conn.cursor()
            query = """
                    DELETE FROM User WHERE UserID=%s
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
        self.var_lname.set(""),
        self.var_phone.set(""),
        self.var_email.set(""),
    
    def search(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
            my_cursor=conn.cursor()
            
            column_mapping = {
            "Ref": "UserID",
            "Name": "UserName",
            "Last Name": "UserLName",
            "Phone": "UserPhone",
            "Email": "UserEmail",
            }

            search_field = self.search_var.get()
            search_value = self.txt_search.get()
            
            column=column_mapping[search_field]

            if search_field not in column_mapping:
                messagebox.showerror("Error", "Invalid search field selected.", parent=self.root)
                return
            
            else:
                query = f"SELECT * FROM User WHERE {column_mapping[search_field]} LIKE %s"
                value=(f"%{self.txt_search.get()}%",)
                
            my_cursor.execute(query,value)
            rows=my_cursor.fetchall()
            
            if len(rows)!=0:
                self.user_table.delete(*self.user_table.get_children())
                for i in rows:
                    self.user_table.insert("",END, values=i)
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
    obj = User_Win(root)
    root.mainloop()