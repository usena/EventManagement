from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Venue_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Event Management System")
        self.root.geometry("1465x835+230+80")
        
        self.var_ref=StringVar()
        self.var_name=StringVar()
        self.var_address=StringVar()
        self.var_type=StringVar()
        self.var_phone=StringVar()
        self.var_email=StringVar()
        self.var_capacity=StringVar()
        self.var_price=StringVar()
        
        lbl_title = Label(self.root, text="Add Venue Details", font=("times new roman", 38, "bold"), bg="green", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1708,height=50)
        
        labelframleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Venue Details", font=("times new roman", 12, "bold"),padx=2)
        labelframleft.place(x=5,y=50,width=420,height=780)
        
        vref=Label(labelframleft,text="Ref", font=("arial", 12, "bold"), padx=2,pady=6)
        vref.grid(row=0,column=0,sticky=W)
        txtRef=ttk.Entry(labelframleft,textvariable=self.var_ref,font=("arial", 13, "bold"),width=29,state="readonly")
        txtRef.grid(row=0,column=1)
        
        vname=Label(labelframleft,text="Name", font=("arial", 12, "bold"), padx=2,pady=6)
        vname.grid(row=1,column=0,sticky=W)
        txtName=ttk.Entry(labelframleft,textvariable=self.var_name,font=("arial", 13, "bold"),width=29)
        txtName.grid(row=1,column=1)
        
        vaddress=Label(labelframleft,text="Address", font=("arial", 12, "bold"), padx=2,pady=6)
        vaddress.grid(row=2,column=0,sticky=W)
        txtAddress=ttk.Entry(labelframleft,textvariable=self.var_address,font=("arial", 13, "bold"),width=29)
        txtAddress.grid(row=2,column=1)
        
        vtype=Label(labelframleft,text="Type", font=("arial", 12, "bold"), padx=2,pady=6)
        vtype.grid(row=3,column=0,sticky=W)
        combo_type=ttk.Combobox(labelframleft,textvariable=self.var_type,font=("arial", 12, "bold"),width=27,state="readonly")
        combo_type["value"]=("Indoor", "Outdoor")
        combo_type.grid(row=3,column=1)

        vphone=Label(labelframleft,text="Phone Number", font=("arial", 12, "bold"), padx=2,pady=6)
        vphone.grid(row=4,column=0,sticky=W)
        txtPhone=ttk.Entry(labelframleft,textvariable=self.var_phone,font=("arial", 13, "bold"),width=29)
        txtPhone.grid(row=4,column=1)
        
        vemail=Label(labelframleft,text="Email", font=("arial", 12, "bold"), padx=2,pady=6)
        vemail.grid(row=5,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframleft,textvariable=self.var_email,font=("arial", 13, "bold"),width=29)
        txtEmail.grid(row=5,column=1)
        
        vcapacity=Label(labelframleft,text="Capacity", font=("arial", 12, "bold"), padx=2,pady=6)
        vcapacity.grid(row=6,column=0,sticky=W)
        txtCapacity=ttk.Entry(labelframleft,textvariable=self.var_capacity,font=("arial", 13, "bold"),width=29)
        txtCapacity.grid(row=6,column=1)
        
        vprice=Label(labelframleft,text="Price", font=("arial", 12, "bold"), padx=2,pady=6)
        vprice.grid(row=7,column=0,sticky=W)
        txtPrice=ttk.Entry(labelframleft,textvariable=self.var_price,font=("arial", 13, "bold"),width=29)
        txtPrice.grid(row=7,column=1)
        
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
        combo_Search["value"]=("Ref", "Type", "Capacity", "Price")
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
        
        self.Venue_Details_Table=ttk.Treeview(details_table,columns=("Ref", "Name", "Address", "Type", "Phone", "Email", "Capacity", "Price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Venue_Details_Table.xview)
        scroll_y.config(command=self.Venue_Details_Table.yview)
        
        self.Venue_Details_Table.heading("Ref", text="Refer No")
        self.Venue_Details_Table.heading("Name", text="Name")
        self.Venue_Details_Table.heading("Address", text="Address")
        self.Venue_Details_Table.heading("Type", text="Type")
        self.Venue_Details_Table.heading("Phone", text="Phone Number")
        self.Venue_Details_Table.heading("Email", text="Email")
        self.Venue_Details_Table.heading("Capacity", text="Capacity")
        self.Venue_Details_Table.heading("Price", text="Price")
        
        self.Venue_Details_Table["show"]="headings"
        
        self.Venue_Details_Table.column("Ref",width=100)
        self.Venue_Details_Table.column("Name",width=100)
        self.Venue_Details_Table.column("Address",width=100)
        self.Venue_Details_Table.column("Type",width=100)
        self.Venue_Details_Table.column("Phone",width=100)
        self.Venue_Details_Table.column("Email",width=100)
        self.Venue_Details_Table.column("Capacity",width=100)
        self.Venue_Details_Table.column("Price",width=100)
        
        self.Venue_Details_Table.pack(fill=BOTH,expand=1)
        self.Venue_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if  (not self.var_name.get().strip() or
            not self.var_address.get().strip() or
            not self.var_type.get().strip() or
            not self.var_phone.get().strip() or
            not self.var_capacity.get().strip() or
            not self.var_price.get().strip()):
            messagebox.showwarning("Error", "All entry except email must be filled!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
                my_cursor=conn.cursor()
                query = """
                        INSERT INTO Venue (VenueName, VenueAddress, VenueType, VenuePhone, VenueEmail, VenueCapacity, VenuePrice) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """
                        
                values = (
                self.var_name.get(),
                self.var_address.get(),
                self.var_type.get(),
                self.var_phone.get(),
                self.var_email.get(),
                self.var_capacity.get(),
                self.var_price.get(),
                )
                
                my_cursor.execute(query,values)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "venue has been added",parent=self.root)
                
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
                SELECT * FROM Venue
                """
        my_cursor.execute(query)
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Venue_Details_Table.delete(*self.Venue_Details_Table.get_children())
            for i in rows:
                self.Venue_Details_Table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self,event=""):
        cursor_row=self.Venue_Details_Table.focus()
        content=self.Venue_Details_Table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0])
        self.var_name.set(row[1]),
        self.var_address.set(row[2]),
        self.var_type.set(row[3]),
        self.var_phone.set(row[4]),
        self.var_email.set(row[5]),
        self.var_capacity.set(row[6]),
        self.var_price.set(row[7]),
    
    def update(self):
        if (not self.var_name.get().strip() or
            not self.var_address.get().strip() or
            not self.var_type.get().strip() or
            not self.var_phone.get().strip() or
            not self.var_capacity.get().strip() or
            not self.var_price.get().strip()):
            messagebox.showwarning("Error", "All entry except email must be filled!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
                my_cursor=conn.cursor()
                query = """
                        UPDATE Venue 
                        SET VenueName=%s, VenueAddress=%s, VenueType=%s, VenuePhone=%s, VenueEmail=%s, VenueCapacity=%s, VenuePrice=%s
                        WHERE VenueID=%s
                        """
                values = (
                    self.var_name.get(),
                    self.var_address.get(),
                    self.var_type.get(),
                    self.var_phone.get(),
                    self.var_email.get(),
                    self.var_capacity.get(),
                    self.var_price.get(),
                    self.var_ref.get(),
                    )
                my_cursor.execute(query,values)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "venue details has been updated",parent=self.root)
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
        mDelete=messagebox.askyesno("Event Management System","Do you  want to delete this venue", parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
            my_cursor=conn.cursor()
            query = """
                    DELETE FROM Venue WHERE VenueID=%s
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
        self.var_address.set(""),
        self.var_type.set(""),
        self.var_phone.set(""),
        self.var_email.set(""),
        self.var_capacity.set(""),
        self.var_price.set(""),
    
    def search(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
            my_cursor=conn.cursor()
            
            column_mapping = {
            "Ref": "VenueID",
            "Type": "VenueType",
            "Capacity": "VenueCapacity",
            "Price": "VenuePrice"
            }

            search_field = self.search_var.get()
            search_value = self.txt_search.get()

            if search_field not in column_mapping:
                messagebox.showerror("Error", "Invalid search field selected.", parent=self.root)
                return
            
            column=column_mapping[search_field]
            
            if search_field in ["Capacity", "Price"]:
                try:
                    numeric_value = float(search_value)  # Ensure the input is numeric
                    if search_field == "Capacity":
                        query = f"SELECT * FROM Venue WHERE {column} >= %s"
                    elif search_field == "Price":
                        query = f"SELECT * FROM Venue WHERE {column} <= %s"
                    value = (numeric_value,)
                except ValueError:
                    messagebox.showerror("Error", f"Please enter a valid number for {search_field}.", parent=self.root)
                    return
            else:
                query = f"SELECT * FROM Venue WHERE {column_mapping[search_field]} LIKE %s"
                value=(f"%{self.txt_search.get()}%",)
                
            my_cursor.execute(query,value)
            rows=my_cursor.fetchall()
            
            if len(rows)!=0:
                self.Venue_Details_Table.delete(*self.Venue_Details_Table.get_children())
                for i in rows:
                    self.Venue_Details_Table.insert("",END, values=i)
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
    obj=Venue_Win(root)
    root.mainloop()