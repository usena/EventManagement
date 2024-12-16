from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Catering_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management System")
        self.root.geometry("1465x835+230+80")
        
        # Variables for Catering Details
        self.var_ref = StringVar()
        self.var_name = StringVar()
        self.var_standard = StringVar()
        self.var_description = StringVar()
        self.var_allergy = BooleanVar()
        self.var_price = StringVar()
        
        lbl_title = Label(self.root, text="Add Catering Details", font=("times new roman", 38, "bold"), bg="green", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1708, height=50)
        
        labelframleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Catering Details", font=("times new roman", 12, "bold"), padx=2)
        labelframleft.place(x=5, y=50, width=420, height=780)
        
        # Catering Reference
        ref_label = Label(labelframleft, text="Ref", font=("arial", 12, "bold"), padx=2, pady=6)
        ref_label.grid(row=0, column=0, sticky=W)
        txtRef = ttk.Entry(labelframleft, textvariable=self.var_ref, font=("arial", 13, "bold"), width=29, state="readonly")
        txtRef.grid(row=0, column=1)
        
        # Catering Name
        name_label = Label(labelframleft, text="Name", font=("arial", 12, "bold"), padx=2, pady=6)
        name_label.grid(row=1, column=0, sticky=W)
        txtName = ttk.Entry(labelframleft, textvariable=self.var_name, font=("arial", 13, "bold"), width=29)
        txtName.grid(row=1, column=1)
        
        # Catering Type
        standard_label = Label(labelframleft, text="Standard", font=("arial", 12, "bold"), padx=2, pady=6)
        standard_label.grid(row=2, column=0, sticky=W)
        combo_type = ttk.Combobox(labelframleft, textvariable=self.var_standard, font=("arial", 12, "bold"), width=27, state="readonly")
        combo_type["value"] = ("Standard", "Premium")
        combo_type.grid(row=2, column=1)
        
        # Catering Description
        description_label = Label(labelframleft, text="Description", font=("arial", 12, "bold"), padx=2, pady=6)
        description_label.grid(row=3, column=0, sticky=W)
        txtDescription = ttk.Entry(labelframleft, textvariable=self.var_description, font=("arial", 13, "bold"), width=29)
        txtDescription.grid(row=3, column=1)
        
        # Catering Allergy
        allergen_label = Label(labelframleft, text="Contain Allergy", font=("arial", 12, "bold"), padx=2, pady=6)
        allergen_label.grid(row=4, column=0, sticky=W)
        txtAllergen = Checkbutton(labelframleft, variable=self.var_allergy, offvalue=FALSE, onvalue=TRUE, font=("arial", 13, "bold"))
        txtAllergen.grid(row=4, column=1)
        
        # Catering Price
        price_label = Label(labelframleft, text="Price", font=("arial", 12, "bold"), padx=2, pady=6)
        price_label.grid(row=5, column=0, sticky=W)
        txtPrice = ttk.Entry(labelframleft, textvariable=self.var_price, font=("arial", 13, "bold"), width=29)
        txtPrice.grid(row=5, column=1)
        
        btn_frame = Frame(labelframleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)
        
        # Buttons
        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="green", fg="white", width=9)
        btnAdd.grid(row=0, column=0, padx=1)
        
        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 12, "bold"), bg="green", fg="white", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)
        
        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("arial", 12, "bold"), bg="green", fg="white", width=9)
        btnDelete.grid(row=0, column=2, padx=1)
        
        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("arial", 12, "bold"), bg="green", fg="white", width=9)
        btnReset.grid(row=0, column=3, padx=1)
        
        # Table for Catering Details
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Catering Details & Search", font=("times new roman", 12, "bold"), padx=2)
        table_frame.place(x=435, y=50, width=990, height=780)
        
        lblSearchBy = Label(table_frame, font=("arial", 12, "bold"), text="Search By", bg="orange", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)
        
        self.search_var = StringVar()
        combo_Search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        combo_Search["value"] = ("Ref", "Standard", "Price")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)
        
        self.txt_search = StringVar()
        txtSearch = ttk.Entry(table_frame, textvariable=self.txt_search, font=("arial", 13, "bold"), width=34)
        txtSearch.grid(row=0, column=2, padx=2)
        
        btnSearch = Button(table_frame, text="Search", command=self.search, font=("arial", 12, "bold"), bg="green", fg="white", width=13)
        btnSearch.grid(row=0, column=3, padx=1)
        
        btnShow = Button(table_frame, text="Show All", command=self.fetch_data, font=("arial", 12, "bold"), bg="green", fg="white", width=13)
        btnShow.grid(row=0, column=4, padx=1)
        
        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=975, height=650)
        
        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)
        
        self.Catering_Details_Table = ttk.Treeview(details_table, columns=("Ref", "Name", "Standard", "Description", "Contain Allergy", "Price"),
                                                    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.Catering_Details_Table.xview)
        scroll_y.config(command=self.Catering_Details_Table.yview)
        
        self.Catering_Details_Table.heading("Ref", text="Refer No")
        self.Catering_Details_Table.heading("Name", text="Name")
        self.Catering_Details_Table.heading("Standard", text="Standard")
        self.Catering_Details_Table.heading("Description", text="Description")
        self.Catering_Details_Table.heading("Contain Allergy", text="Contain Allergy")
        self.Catering_Details_Table.heading("Price", text="Price")
        
        self.Catering_Details_Table["show"] = "headings"
        
        self.Catering_Details_Table.column("Ref", width=100)
        self.Catering_Details_Table.column("Name", width=100)
        self.Catering_Details_Table.column("Standard", width=100)
        self.Catering_Details_Table.column("Description", width=100)
        self.Catering_Details_Table.column("Contain Allergy", width=100)
        self.Catering_Details_Table.column("Price", width=100)
        
        self.Catering_Details_Table.pack(fill=BOTH, expand=1)
        self.Catering_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    def add_data(self):
        if  (not self.var_name.get().strip() or
            not self.var_standard.get().strip() or
            not self.var_description.get().strip() or
            not self.var_price.get().strip()):
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Spade.Z@88", database="EventManagement")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO CateringType (CateringType, CateringStandard, CateringDesc, ContainAllergens, CateringPrice) VALUES (%s, %s, %s, %s, %s)",
                                (self.var_name.get(), self.var_standard.get(), self.var_description.get(), self.var_allergy.get(), self.var_price.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Catering added successfully")
            except Exception as err:
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
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Spade.Z@88", database="EventManagement")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM CateringType")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.Catering_Details_Table.delete(*self.Catering_Details_Table.get_children())
                for row in rows:
                    self.Catering_Details_Table.insert("", END, values=row)
                conn.commit()
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")
    
    def get_cursor(self,event=""):
        cursor_row=self.Catering_Details_Table.focus()
        content=self.Catering_Details_Table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0])
        self.var_name.set(row[1]),
        self.var_standard.set(row[2]),
        self.var_description.set(row[3]),
        self.var_allergy.set(row[4]),
        self.var_price.set(row[5]),
    
    def update(self):
        if (not self.var_name.get().strip() or
            not self.var_standard.get().strip() or
            not self.var_description.get().strip() or
            not self.var_price.get().strip()):
            messagebox.showwarning("Error", "All entries must be filled!",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
                my_cursor=conn.cursor()
                query = """
                        UPDATE CateringType 
                        SET CateringType=%s, CateringStandard=%s, CateringDesc=%s, ContainAllergens=%s, CateringPrice=%s
                        WHERE CateringTypeID=%s
                        """
                values = (
                    self.var_name.get(),
                    self.var_standard.get(),
                    self.var_description.get(),
                    self.var_allergy.get(),
                    self.var_price.get(),
                    self.var_ref.get(),
                    )
                my_cursor.execute(query,values)
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "catering details has been updated",parent=self.root)
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
        mDelete=messagebox.askyesno("Event Management System","Do you  want to delete this catering", parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
            my_cursor=conn.cursor()
            query = """
                    DELETE FROM CateringType WHERE CateringTypeID=%s
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
        self.var_name.set("")
        self.var_standard.set("")
        self.var_description.set("")
        self.var_allergy.set(FALSE)
        self.var_price.set("")
    
    def search(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
            my_cursor=conn.cursor()
            
            column_mapping = {
            "Ref": "CateringTypeID",
            "Standard": "CateringStandard",
            "Price": "CateringPrice"
            }

            search_field = self.search_var.get()
            search_value = self.txt_search.get()
            
            if search_field not in column_mapping:
                messagebox.showerror("Error", "Invalid search field selected.", parent=self.root)
                return
            
            column=column_mapping[search_field]
            
            if search_field in ["Price"]:
                try:
                    numeric_value = float(search_value)  # Ensure the input is numeric
                    query = f"SELECT * FROM CateringType WHERE {column} <= %s"
                    value = (numeric_value,)
                except ValueError:
                    messagebox.showerror("Error", f"Please enter a valid number for {search_field}.", parent=self.root)
                    return
            else:
                query = f"SELECT * FROM CateringType WHERE {column_mapping[search_field]} LIKE %s"
                value=(f"%{self.txt_search.get()}%",)
                
            my_cursor.execute(query,value)
            rows=my_cursor.fetchall()
            
            if len(rows)!=0:
                self.Catering_Details_Table.delete(*self.Catering_Details_Table.get_children())
                for i in rows:
                    self.Catering_Details_Table.insert("",END, values=i)
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
    
# To run the program
if __name__ == "__main__":
    root = Tk()
    obj = Catering_Win(root)
    root.mainloop()
