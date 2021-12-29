from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime
#from login import login_Window

class booking_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Cab Booking System")
        # Put frame geometry starting from 0, 0
        self.root.geometry("905x350+250+150")

        self.var_from = StringVar()
        self.var_to = StringVar()
        self.var_ct = StringVar()
        self.var_jt = StringVar()
        self.var_dist = StringVar()
        self.var_cost = StringVar()

        img1 = Image.open("image2.jpg")
        img1 = img1.resize((430, 290), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl2 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lbl2.place(x=460, y=50, width=430, height=290)

        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Create Account", padx=2,
                                    font=("times new roman", 12, "bold"))
        lableframeleft.place(x=5, y=50, width=450, height=290)

        lbl1 = Label(self.root, text="Cab booking page", font=("arial", 28, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=905, height=50)

        lbl_from = Label(lableframeleft, text=" From : ", font=("times new roman", 12, "bold"), padx=2,
                             pady=6)
        lbl_from.grid(row=0, column=0, sticky=W)
        combo_from = ttk.Combobox(lableframeleft, textvariable=self.var_from, font=("times new roman", 12, "bold"),
                                      width=27, state="readonly")
        combo_from["value"] = ("Shivajinagar", "Aundh","Baner","Kothrud")
        combo_from.grid(row=0, column=1)

        lbl_to = Label(lableframeleft, text=" To : ", font=("times new roman", 12, "bold"), padx=2,
                             pady=6)
        lbl_to.grid(row=1, column=0, sticky=W)
        combo_to = ttk.Combobox(lableframeleft, textvariable=self.var_to, font=("times new roman", 12, "bold"),
                                      width=27, state="readonly")
        combo_to["value"] = ("Shivajinagar", "Aundh","Baner","Kothrud")
        combo_to.grid(row=1, column=1)


        lbl_ct = Label(lableframeleft, text=" Cab Type : ", font=("times new roman", 12, "bold"), padx=2,
                             pady=6)
        lbl_ct.grid(row=2, column=0, sticky=W)
        combo_ct = ttk.Combobox(lableframeleft, textvariable=self.var_ct, font=("times new roman", 12, "bold"),
                                      width=27, state="readonly")
        combo_ct["value"] = ("Standard", "Prime","SUV")
        combo_ct.grid(row=2, column=1)


        lbl_jt = Label(lableframeleft, text=" Journey Type : ", font=("times new roman", 12, "bold"), padx=2,
                             pady=6)
        lbl_jt.grid(row=3, column=0, sticky=W)
        combo_jt = ttk.Combobox(lableframeleft, textvariable=self.var_jt, font=("times new roman", 12, "bold"),
                                      width=27, state="readonly")
        combo_jt["value"] = ("One way", "Return")
        combo_jt.grid(row=3, column=1)

        lbl_dist = Label(lableframeleft, text="Distance(km): ", font=("times new roman", 12, "bold"), padx=2,
                         pady=6)
        lbl_dist.grid(row=4, column=0, sticky=W)
        entry_dist = ttk.Entry(lableframeleft,textvariable = self.var_dist, width=29, font=("times new roman", 13, "bold"), state="readonly")
        entry_dist.grid(row=4, column=1)

        # lbl_lug = Label(lableframeleft, text=" Extra Luggage : ", font=("times new roman", 12, "bold"), padx=2,
        #                      pady=6)
        # lbl_lug.grid(row=5, column=0, sticky=W)
        # combo_lug = ttk.Combobox(lableframeleft, textvariable=self.var_lug, font=("times new roman", 12, "bold"),
        #                               width=27, state="readonly")
        # combo_lug["value"] = ("1", "2", "3")
        # combo_lug.grid(row=5, column=1)

        lbl_cost = Label(lableframeleft, text="Cost : ", font=("times new roman", 12, "bold"), padx=2,
                         pady=6)
        lbl_cost.grid(row=6, column=0, sticky=W)
        entry_cost = ttk.Entry(lableframeleft,textvariable = self.var_cost, width=29, font=("times new roman", 13, "bold"), state="readonly")
        entry_cost.grid(row=6, column=1)

        btnBill = Button(lableframeleft, text="Generate Bill",command=self.total,font=("times new roman", 12, "bold"), bg="black", fg="gold", width= 17
                        )
        btnBill.grid(row=7, column=0)

        btnBook = Button(lableframeleft, text="Book",command=self.add_data,font=("times new roman", 12, "bold"), bg="black", fg="gold", width=15,
                        padx=1)
        btnBook.grid(row=7, column=1)

    def add_data(self):
        if self.var_jt.get()=="" :
            messagebox.showerror("Error","All details are required",parent=self.root)  
        else :
            try:

                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="cbs") 
                my_cursor=conn.cursor()
                my_cursor.execute("insert into booking values(%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_from.get(),
                                                                            self.var_to.get(),
                                                                            self.var_ct.get(),
                                                                            self.var_jt.get(),
                                                                            self.var_dist.get(),
                                                                        
                                                                            self.var_cost.get()
                                                                        ))
                                                                                                                                                                                                          
                conn.commit()
                # self.fetch_data
                conn.close()
                messagebox.showinfo("Success", "Cab Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong :{str(es)}",parent=self.root)


    def total(self):
        if(self.var_from.get()=="Shivajinagar" and self.var_to.get()=="Aundh") or (self.var_to.get()=="Shivajinagar" and self.var_from.get()=="Aundh") :
            if(self.var_ct.get() == "Standard" ):
                x= 1
            elif(self.var_ct.get() == "Prime" ):
                x= 2
            elif(self.var_ct.get() == "SUV" ):
                x= 3
            if(self.var_jt.get() == "One way" ):
                y= 1
            elif(self.var_jt.get() == "Return" ):
                y= 2
            distance=float(6)
            Priceperkm=float(20)
            cost=float(distance*Priceperkm*x*y)
            self.var_cost.set(cost)
            self.var_dist.set(distance)

        elif(self.var_from.get()=="Shivajinagar" and self.var_to.get()=="Baner") or (self.var_to.get()=="Shivajinagar" and self.var_from.get()=="Baner"):
            if(self.var_ct.get() == "Standard" ):
                x= 1
            elif(self.var_ct.get() == "Prime" ):
                x= 2
            elif(self.var_ct.get() == "SUV" ):
                x= 3
            if(self.var_jt.get() == "One way" ):
                y= 1
            elif(self.var_jt.get() == "Return" ):
                y= 2
            distance=float(9)
            Priceperkm=float(20)
            cost=float(distance*Priceperkm*x*y)
            self.var_cost.set(cost)
            self.var_dist.set(distance)


        elif(self.var_from.get()=="Shivajinagar" and self.var_to.get()=="Kothrud") or (self.var_to.get()=="Shivajinagar" and self.var_from.get()=="kothrud"):
            if(self.var_ct.get() == "Standard" ):
                x= 1
            elif(self.var_ct.get() == "Prime" ):
                x= 2
            elif(self.var_ct.get() == "SUV" ):
                x= 3
            if(self.var_jt.get() == "One way" ):
                y= 1
            elif(self.var_jt.get() == "Return" ):
                y= 2
            distance=float(7)
            Priceperkm=float(20)
            cost=float(distance*Priceperkm*x*y)
            self.var_cost.set(cost)
            self.var_dist.set(distance)

        
        elif(self.var_from.get()=="Aundh" and self.var_to.get()=="Baner") or (self.var_to.get()=="Aundh" and self.var_from.get()=="Baner"):
            if(self.var_ct.get() == "Standard" ):
                x= 1
            elif(self.var_ct.get() == "Prime" ):
                x= 2
            elif(self.var_ct.get() == "SUV" ):
                x= 3
            if(self.var_jt.get() == "One way" ):
                y= 1
            elif(self.var_jt.get() == "Return" ):
                y= 2
            
            distance=float(3)
            Priceperkm=float(20)
            cost=float(distance*Priceperkm*x*y)
            self.var_cost.set(cost)
            self.var_dist.set(distance)

        elif(self.var_from.get()=="Baner" and self.var_to.get()=="Kothrud") or (self.var_to.get()=="Baner" and self.var_from.get()=="Kothrud"):
            
            if(self.var_ct.get() == "Standard" ):
                x= 1
            elif(self.var_ct.get() == "Prime" ):
                x= 2
            elif(self.var_ct.get() == "SUV" ):
                x= 3
            if(self.var_jt.get() == "One way" ):
                y= 1
            elif(self.var_jt.get() == "Return" ):
                y= 2
            
            distance=float(12)
            Priceperkm=float(20)
            cost=float(distance*Priceperkm*x*y)
            self.var_cost.set(cost)
            self.var_dist.set(distance)

        elif(self.var_from.get()=="Aundh" and self.var_to.get()=="Kothrud") or (self.var_to.get()=="Aundh" and self.var_from.get()=="Kothrud"):
            if(self.var_ct.get() == "Standard" ):
                x= 1
            elif(self.var_ct.get() == "Prime" ):
                x= 2
            elif(self.var_ct.get() == "SUV" ):
                x= 3
            if(self.var_jt.get() == "One way" ):
                y= 1
            elif(self.var_jt.get() == "Return" ):
                y= 2
            distance=float(10)
            Priceperkm=float(20)
            cost=float(distance*Priceperkm*x*y)
            self.var_cost.set(cost)
            self.var_dist.set(distance)
        else :
            messagebox.showerror("Error","Try again",parent=self.root)
            
        

if __name__ == "__main__":
    root = Tk()
    obj = booking_Window(root)
    root.mainloop()