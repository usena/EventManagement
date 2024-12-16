from tkinter import*
from user import User_Win
from venue import Venue_Win
from event import Event_Win
from invitation import Invitation_Win
from catering import Catering_Win
from organizer import Organizer_Win
from bill import Bill_Win

class EventManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Event Management System")
        self.root.geometry("1150x800+0+0")
        
        lbl_title = Label(self.root, text="Event Management System", font=("times new roman", 38, "bold"), bg="green", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1708,height=50)
        
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=50, width=1708,height=882)
        
        lbl_title = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="green", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0,y=0,width=230)
        
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35, width=228,height=265)
        
        user_btn=Button(btn_frame,text="User",command=self.user_details, width=22,font=("times new roman", 14, "bold"), bg="green", fg="white",bd=0,cursor="hand1")
        user_btn.grid(row=0,column=0,pady=1)
        
        organizer_btn=Button(btn_frame,text="Organizer", command=self.organizer_details, width=22,font=("times new roman", 14, "bold"), bg="green", fg="white",bd=0,cursor="hand1")
        organizer_btn.grid(row=1,column=0,pady=1)
        
        venue_btn=Button(btn_frame,text="Venue", command=self.venue_details, width=22,font=("times new roman", 14, "bold"), bg="green", fg="white",bd=0,cursor="hand1")
        venue_btn.grid(row=2,column=0,pady=1)
        
        catering_btn=Button(btn_frame,text="Catering", command=self.catering_details, width=22,font=("times new roman", 14, "bold"), bg="green", fg="white",bd=0,cursor="hand1")
        catering_btn.grid(row=3,column=0,pady=1)
        
        event_btn=Button(btn_frame,text="Event", command=self.event_details, width=22,font=("times new roman", 14, "bold"), bg="green", fg="white",bd=0,cursor="hand1")
        event_btn.grid(row=4,column=0,pady=1)
        
        invitation_btn=Button(btn_frame,command=self.invitation_details,text="Invitation", width=22,font=("times new roman", 14, "bold"), bg="green", fg="white",bd=0,cursor="hand1")
        invitation_btn.grid(row=5,column=0,pady=1)
        
        bill_btn=Button(btn_frame,text="Bill", command=self.bill_details,width=22,font=("times new roman", 14, "bold"), bg="green", fg="white",bd=0,cursor="hand1")
        bill_btn.grid(row=6,column=0,pady=1)
    
    def user_details(self):
        self.new_window=Toplevel(self.root)
        self.app=User_Win(self.new_window)
        
    def venue_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Venue_Win(self.new_window)
        
    def event_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Event_Win(self.new_window)
    
    def invitation_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Invitation_Win(self.new_window)
        
    def organizer_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Organizer_Win(self.new_window)
    
    def catering_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Catering_Win(self.new_window)
    
    def bill_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Bill_Win(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=EventManagementSystem(root)
    root.mainloop()

