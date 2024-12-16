from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

class Bill_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Invitation Management")
        self.root.geometry("1465x835+230+80")

        self.var_ref=StringVar()
        self.var_price=StringVar()
        self.var_event=StringVar()

        # Title
        lbl_title = Label(
            self.root, text="Manage Bill", font=("times new roman", 20, "bold"),
            bg="green", fg="white", bd=4, relief=RIDGE
        )
        lbl_title.place(x=0,y=0,width=1708,height=50)

        # Main Frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=5,y=50,width=420,height=780)

        # Labels and Entries
        lbl_invitation_id = Label(main_frame, text="Bill ID:", font=("arial", 12, "bold"), padx=2,pady=6)
        lbl_invitation_id.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.txt_invitation_id = ttk.Entry(main_frame, textvariable=self.var_ref, font=("times new roman", 14), width=20,state="readonly")
        self.txt_invitation_id.grid(row=0, column=1)
        
        lbl_user_id = Label(main_frame, text="Price", font=("arial", 12, "bold"), padx=2,pady=6)
        lbl_user_id.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.txt_user_id = ttk.Entry(main_frame, textvariable=self.var_price, font=("times new roman", 14), width=20,state="readonly")
        self.txt_user_id.grid(row=1, column=1)
        
        lbl_event_id = Label(main_frame, text="Event ID:", font=("arial", 12, "bold"), padx=2,pady=6)
        lbl_event_id.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.txt_event_id = ttk.Entry(main_frame, textvariable=self.var_event, font=("times new roman", 14), width=20, state="readonly")
        self.txt_event_id.grid(row=2, column=1)

        # Display Data Frame
        data_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details & Search", font=("times new roman", 12, "bold"),padx=2)
        data_frame.place(x=435,y=50,width=990,height=780)

        lblSearchBy=Label(data_frame,font=("arial", 12, "bold"),text="Search By", bg="orange", fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W, padx=2)
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(data_frame,textvariable=self.search_var,font=("arial", 12, "bold"),width=24,state="readonly")
        combo_Search["value"]=("Ref", "Event")
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
            details_table, columns=("ID", "Price", "Event"), xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_x.config(command=self.data_table.xview)
        scroll_y.config(command=self.data_table.yview)

        self.data_table.heading("ID", text="ID")
        self.data_table.heading("Price", text="Price")
        self.data_table.heading("Event", text="Event")
        self.data_table["show"] = "headings"
        self.data_table.column("ID", width=100)
        self.data_table.column("Price", width=100)
        self.data_table.column("Event", width=100)
        
        self.data_table.pack(fill=BOTH, expand=1)
        self.data_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
        my_cursor=conn.cursor()
        query = """
                SELECT * FROM Transaction_Bill
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
        self.var_price.set(row[1]),
        self.var_event.set(row[2]),
    
    def search(self):
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="Spade.Z@88",database="EventManagement")
            my_cursor=conn.cursor()
            
            column_mapping = {
            "Ref": "BillID",
            "Event": "EventID",
            }

            search_field = self.search_var.get()
            search_value = self.txt_search.get()
            
            column=column_mapping[search_field]

            if search_field not in column_mapping:
                messagebox.showerror("Error", "Invalid search field selected.", parent=self.root)
                return
            
            else:
                query = f"SELECT * FROM Transaction_Bill WHERE {column_mapping[search_field]} LIKE %s"
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
    obj = Bill_Win(root)
    root.mainloop()