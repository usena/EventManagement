from tkinter import*
from tkinter import ttk

class User_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Event Management System")
        self.root.geometry("1465x835+230+80")
        
        lbl_title = Label(self.root, text="Add User Details", font=("times new roman", 38, "bold"), bg="green", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1708,height=50)
        
        labelframleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="User Details", font=("times new roman", 12, "bold"),padx=2)
        labelframleft.place(x=5,y=50,width=420,height=780)
        
        lbl_user_ref=Label(labelframleft,text="User Ref", font=("arial", 12, "bold"), padx=2,pady=6)
        lbl_user_ref.grid(row=0,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframleft,font=("arial", 13, "bold"))
        entry_ref.grid(row=0,column=1)
        
        uname=Label(labelframleft,text="Name", font=("arial", 12, "bold"), padx=2,pady=6)
        uname.grid(row=1,column=0,sticky=W)
        txtName=ttk.Entry(labelframleft,font=("arial", 13, "bold"))
        txtName.grid(row=1,column=1)
        
        ulname=Label(labelframleft,text="Last Name", font=("arial", 12, "bold"), padx=2,pady=6)
        ulname.grid(row=2,column=0,sticky=W)
        txtLName=ttk.Entry(labelframleft,font=("arial", 13, "bold"))
        txtLName.grid(row=2,column=1)
        
        uphone=Label(labelframleft,text="Phone Number", font=("arial", 12, "bold"), padx=2,pady=6)
        uphone.grid(row=3,column=0,sticky=W)
        txtPhone=ttk.Entry(labelframleft,font=("arial", 13, "bold"))
        txtPhone.grid(row=3,column=1)
        
        uemail=Label(labelframleft,text="Email", font=("arial", 12, "bold"), padx=2,pady=6)
        uemail.grid(row=4,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframleft,font=("arial", 13, "bold"))
        txtEmail.grid(row=4,column=1)
        
        

if __name__ == "__main__":
    root=Tk()
    obj=User_Win(root)
    root.mainloop()