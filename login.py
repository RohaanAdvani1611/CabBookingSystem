from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime
from createAcc import Account_Window
from booking import booking_Window

class login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("CAB booking system")
        # Put frame geometry starting from 0, 0
        self.root.geometry("500x400+450+150")

        self.var_username = StringVar()
        self.var_password = StringVar()

        img1 = Image.open("image4.png")
        img1 = img1.resize((475, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl2 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lbl2.place(x=5, y=200, width=475, height=195)

         # Title
        lbl1 = Label(self.root, text="Login Page ", font=("arial", 18, "bold"), bg="black",
                     fg="gold", bd=4, relief=RIDGE)
        lbl1.place(x=0, y=0, width=500, height=50)

        lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Create Account", padx=2,
                                    font=("times new roman", 12, "bold"))
        lableframeleft.place(x=5, y=55, width=475, height=135)

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

        btnCreate = Button(lableframeleft, text="Create Account",command=self.Create,font=("times new roman", 12, "bold"), bg="black", fg="gold", width= 17
                        )
        btnCreate.grid(row=9, column=0)

        btnLogin = Button(lableframeleft, text="Login",command=self.login,font=("times new roman", 12, "bold"), bg="black", fg="gold", width=15,
                        padx=1)
        btnLogin.grid(row=9, column=1)

    def login(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="cbs") 
        my_cursor=conn.cursor()
        my_cursor.execute("select username,password from user where username like '%"+str(self.var_username.get())+"%'")

        # my_cursor.execute("select username,password from user where username like '%s'",(
                                                                        #     self.var_username.get()
                                                                            
                                                                        # ))
        
        x= my_cursor.fetchall()
        if x :
            self.new_window = Toplevel(self.root)
            self.app = booking_Window(self.new_window)
        conn.commit()
        conn.close()

    def Create(self):
        self.new_window = Toplevel(self.root)
        self.app = Account_Window(self.new_window)  


if __name__ == "__main__":
    root = Tk()
    obj = login_Window(root)
    root.mainloop()