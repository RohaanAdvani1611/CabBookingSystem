from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime
from booking import booking_Window
import re
#from login import login_Window

class Account_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Cab Booking System")
        # Put frame geometry starting from 0, 0
        self.root.geometry("905x450+250+150")


        self.var_username = StringVar()
        self.var_password = StringVar()
        self.var_name = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_age = StringVar()
        self.var_address = StringVar()
        self.var_pincode = StringVar()
        

        # Title
        lbl1 = Label(self.root, text="Create Account Page", font=("arial", 38, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=905, height=50)

        img1 = Image.open("image1.jpg")
        img1 = img1.resize((420, 190), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl2 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lbl2.place(x=460, y=50, width=420, height=190)

        img3 = Image.open("image3.jpg")
        img3 = img3.resize((420, 190), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl3 = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lbl3.place(x=460, y=245, width=420, height=190)

         # Label Frame
        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Create Account", padx=2,
                                    font=("times new roman", 12, "bold"))
        lableframeleft.place(x=5, y=50, width=450, height=380)
        
        #USERNAME
        lbl_username = Label(lableframeleft, text="Username : ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lbl_username.grid(row=1, column=0, sticky=W)
        entry_username = ttk.Entry(lableframeleft,textvariable = self.var_username, width=29, font=("times new roman", 13, "bold"))
        entry_username.grid(row=1, column=1)
        #PASSWORD
        lbl_password = Label(lableframeleft, text="Password : ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lbl_password.grid(row=2, column=0, sticky=W)
        entry_password = ttk.Entry(lableframeleft,textvariable = self.var_password, width=29, font=("times new roman", 13, "bold"))
        entry_password.grid(row=2, column=1)
        #NAME
        lbl_name = Label(lableframeleft, text="Name : ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lbl_name.grid(row=3, column=0, sticky=W)
        entry_name = ttk.Entry(lableframeleft,textvariable = self.var_name, width=29, font=("times new roman", 13, "bold"))
        entry_name.grid(row=3, column=1)
        #MOBILE
        lbl_mobile = Label(lableframeleft, text="Mobile No : ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lbl_mobile.grid(row=4, column=0, sticky=W)
        entry_mobile = ttk.Entry(lableframeleft,textvariable = self.var_mobile, width=29, font=("times new roman", 13, "bold"))
        entry_mobile.grid(row=4, column=1)
        #EMAIL
        lbl_email = Label(lableframeleft, text="Email : ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lbl_email.grid(row=5, column=0, sticky=W)
        entry_email = ttk.Entry(lableframeleft,textvariable = self.var_email, width=29, font=("times new roman", 13, "bold"))
        entry_email.grid(row=5, column=1)
        #AGE
        lbl_age = Label(lableframeleft, text="Age : ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lbl_age.grid(row=6, column=0, sticky=W)
        entry_age = ttk.Entry(lableframeleft,textvariable = self.var_age, width=29, font=("times new roman", 13, "bold"))
        entry_age.grid(row=6, column=1)
        #ADDRESS
        lbl_address = Label(lableframeleft, text="Address : ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lbl_address.grid(row=7, column=0, sticky=W)
        entry_address = ttk.Entry(lableframeleft,textvariable = self.var_address, width=29, font=("times new roman", 13, "bold"))
        entry_address.grid(row=7, column=1)
        #PINCODE
        lbl_pincode = Label(lableframeleft, text="Pincode : ", font=("times new roman", 12, "bold"), padx=2,
                            pady=6)
        lbl_pincode.grid(row=8, column=0, sticky=W)
        entry_pincode = ttk.Entry(lableframeleft,textvariable = self.var_pincode, width=29, font=("times new roman", 13, "bold"))
        entry_pincode.grid(row=8, column=1)

        btnCreate = Button(lableframeleft, text="Create Account",command=self.add_data,font=("times new roman", 12, "bold"), bg="black", fg="gold", width= 17
                        )
        btnCreate.grid(row=9, column=0)

        btnLogin = Button(lableframeleft, text="Login",command=self.login,font=("times new roman", 12, "bold"), bg="black", fg="gold", width=15,
                        padx=1)
        btnLogin.grid(row=9, column=1)


    def add_data(self):
        flag=1
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
        if self.var_mobile.get()=="" :
            messagebox.showerror("Error","All details are required",parent=self.root)  
        SpecialSym =['$', '@', '#', '%']
        if len(self.var_password.get()) < 6:
            messagebox.showerror('Error', 'length should be at least 6')
            flag=0
        if len(self.var_password.get()) > 20:
            messagebox.showerror('Error', 'length should be not be greater than 20')
            flag=0
        if not any(char.isdigit() for char in self.var_password.get()):
            messagebox.showerror('Error', 'Password should have at least one numeral')
            flag=0
        if not any(char.isupper() for char in self.var_password.get()):
            messagebox.showerror('Error', 'Password should have at least one uppercase letter')
            flag=0
        if not any(char.islower() for char in self.var_password.get()):
            messagebox.showerror('Error', 'Password should have at least one lowercase letter')
            flag=0
        if not any(char in SpecialSym for char in self.var_password.get()):
            messagebox.showerror('Error', 'Password should have at least one of the symbols $@#')
            flag=0
        if any(char.isdigit() for char in self.var_name.get()):
            messagebox.showerror('Error', 'name cannot contain digits')
            flag=0
        if not Pattern.match(self.var_mobile.get()) :
            messagebox.showerror('Error', 'Valid mobile number should contain 10 digits')
            flag=0
        if not re.fullmatch(regex, self.var_email.get()):
            messagebox.showerror('Error', 'Invalid Email Format')
            flag=0
        if  len(self.var_age.get()) == 2:
            for i in self.var_age.get():
                if not i.isdigit():
                    messagebox.showerror('Error', 'Invalid Age')
                    flag=0
        else:
            messagebox.showerror('Error', 'Invalid Age')
            flag=0
        if  len(self.var_pincode.get()) == 6:
            for i in self.var_pincode.get():
                if not i.isdigit():
                    messagebox.showerror('Error', 'Valid pincode should contain 6 digits')
                    flag=0
        else:
            messagebox.showerror('Error', 'Valid pincode should contain 6 digits')
            flag=0
        if(flag==1):
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="cbs") 
                my_cursor=conn.cursor()
                my_cursor.execute("insert into user values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                            self.var_username.get(),
                                                                            self.var_password.get(),
                                                                            self.var_name.get(),
                                                                            self.var_mobile.get(),
                                                                            self.var_email.get(),
                                                                            self.var_age.get(),
                                                                            self.var_address.get(),
                                                                            self.var_pincode.get()
                                                                        ))
                                                                                                                                                                                                          
                conn.commit()
                # self.fetch_data
                conn.close()
                messagebox.showinfo("Success", "Account created",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something went wrong :{str(es)}",parent=self.root)

    def login(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="cbs") 
        my_cursor=conn.cursor()
        my_cursor.execute("select username,password from user where username like '%"+str(self.var_username.get())+"%'")
        x= my_cursor.fetchall()
        if x :
            self.new_window = Toplevel(self.root)
            self.app = booking_Window(self.new_window)
        conn.commit()
        conn.close()

if __name__ == "__main__":
    root = Tk()
    obj = Account_Window(root)
    root.mainloop()
