from tkinter import *
from textwrap import fill
from tkinter import ttk
from tkinter import ttk,messagebox
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x750+0+0")
        
        
        title = Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#1E90FF",fg="white")
        title.pack(side=TOP,fill=X)
        
        
        self.std_enroll=StringVar()
        self.std_name=StringVar()
        self.std_email=StringVar()
        self.std_shift=StringVar()
        self.std_program=StringVar()
        self.std_gender=StringVar()
        self.std_contact=StringVar()
        self.std_dob=StringVar()
       
       
        self.search_by=StringVar()
        self.search_txt=StringVar()
        #======Manage Frame=====#
        Manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="#031F3c")
        Manage_frame.place(x=20,y=100,width=450,height=600)
          
        # m_title=Label(Manage_frame,text="Manage Students",font=("times new roman",22,"bold"),fg="white",bg="#031F3c")
        # m_title.grid(row=0,columnspan=2,pady=5)
          
        l_enrollment = Label(Manage_frame,text="Enrollment",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        l_enrollment.grid(row=1,column=0,pady=10,padx=10,sticky="w")
        txt_enrollment = Entry(Manage_frame,textvariable=self.std_enroll,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_enrollment.grid(row=1,column=1,pady=5,padx=10,sticky="w")
        
        
        l_name = Label(Manage_frame,text="Name",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        l_name.grid(row=2,column=0,pady=10,padx=10,sticky="w")
        txt_name = Entry(Manage_frame,textvariable=self.std_name,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=10,sticky="w")
        
        
        l_email = Label(Manage_frame,text="Email",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        l_email.grid(row=3,column=0,pady=10,padx=10,sticky="w")
        txt_email = Entry(Manage_frame,textvariable=self.std_email,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=10,sticky="w")
        
        l_shift = Label(Manage_frame,text="Shift",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        l_shift.grid(row=4,column=0,pady=10,padx=10,sticky="w")
        
        combo_shift=ttk.Combobox(Manage_frame,textvariable=self.std_shift,font=("times new roman",13,"bold"),state='readonly')
        combo_shift['values']=("First","Second")
        combo_shift.grid(row=4,column=1,padx=10,pady=10)
        
        
        
        l_program = Label(Manage_frame,text="Program",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        l_program.grid(row=5,column=0,pady=10,padx=10,sticky="w")
        combo_program=ttk.Combobox(Manage_frame,textvariable=self.std_program,font=("times new roman",13,"bold"),state='readonly')
        combo_program['values']=("Computer","Electronics","Civil","Mechanical")
        combo_program.grid(row=5,column=1,padx=10,pady=10)
     
        l_gender = Label(Manage_frame,text="Gender",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        l_gender.grid(row=6,column=0,pady=10,padx=10,sticky="w")
        combo_gender=ttk.Combobox(Manage_frame,textvariable=self.std_gender,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=6,column=1,padx=10,pady=10)
    
        l_conatct = Label(Manage_frame,text="Conatct",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        l_conatct.grid(row=7,column=0,pady=10,padx=10,sticky="w")
        txt_contact = Entry(Manage_frame,textvariable=self.std_contact,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=7,column=1,pady=10,padx=10,sticky="w")
        
        
        l_dob = Label(Manage_frame,text="D.O.B",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        l_dob.grid(row=8,column=0,pady=10,padx=10,sticky="w")
        txt_dob = Entry(Manage_frame,textvariable=self.std_dob,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=8,column=1,pady=10,padx=10,sticky="w")
        
        
        l_address = Label(Manage_frame,text="Address",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        l_address.grid(row=9,column=0,pady=10,padx=10,sticky="w")
        
        self.txt_address=Text(Manage_frame,width=30,height=4,font=("",10))
        self.txt_address.grid(row=9,column=1,padx=10,pady=10,sticky="w")
    
    
        #====Button Frame======#
        
        
        Button_Frame=Frame(Manage_frame,bd=4,relief=RIDGE,bg="#031F3c")
        Button_Frame.place(x=15,y=520,width=410,)
    
        Addbtn=Button(Button_Frame,bg="#1E90FF",command=self.add_student,text="Add",width=10).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(Button_Frame,bg="#1E90FF",command=self.update_data,text="Update",width=10).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(Button_Frame,bg="#1E90FF",command=self.delete_data,text="Delete",width=10).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(Button_Frame,bg="#1E90FF",command=self.clear,text="Clear",width=10).grid(row=0,column=3,padx=10,pady=10)
        
        
        
        #======Detail Frame=====#
        Detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="#031F3c")
        Detail_frame.place(x=500,y=100,width=800,height=600)
        
        l_search = Label(Detail_frame,text="Search By",bg="#031F3c",fg="white",font=("times new roman",15,"bold"))
        l_search.grid(row=0,column=0,padx=20,pady=10)
        
        combo_gender=ttk.Combobox(Detail_frame,textvariable=self.search_by,width=12,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("enroll_no","name","conatct")
        combo_gender.grid(row=0,column=1,padx=20,pady=10)
        
        txt_search = Entry(Detail_frame,textvariable=self.search_txt,width=18,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          
        Searchbtn=Button(Detail_frame,bg="#1E90FF",command=self.search_data,text="Search",width=10,padx=5).grid(row=0,column=3,padx=10,pady=10)
        ShowAllbtn=Button(Detail_frame,bg="#1E90FF",command=self.fetch_data,text="Show ALL",width=10,padx=5).grid(row=0,column=4,padx=10,pady=10)



        #=========Table Frame======#
        Table_Frame=Frame(Detail_frame,bd=4,relief=RIDGE,bg="#031F3c")
        Table_Frame.place(x=20,y=70,width=750,height=500)
        
        
       
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Enrollment","name","email","shift","program","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Enrollment",text="Enrollment ")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("shift",text="Shift")
        self.Student_table.heading("program",text="Program")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("Address",text="Address")
        
        self.Student_table['show']='headings'
        self.Student_table.column("Enrollment",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("shift",width=100)
        self.Student_table.column("program",width=100)
        self.Student_table.column("program",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("Address",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_student(self):
        if self.std_enroll.get()=="" or self.std_name.get()=="":
           messagebox.showerror("Error","All fields are required!!!!")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="stm")
                cur = con.cursor()
                cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.std_enroll.get(),
                                                                                    self.std_name.get(),
                                                                                    self.std_email.get(),
                                                                                    self.std_shift.get(),
                                                                                    self.std_program.get(),
                                                                                    self.std_gender.get(),
                                                                                    self.std_contact.get(),
                                                                                    self.std_dob.get(),
                                                                                    self.txt_address.get('1.0', END)
                                                                                    ))

                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been Inserted")
            except Exception as es:
                print(es)

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

        
        
    def clear(self):
        self.std_enroll.set("")
        self.std_name.set("")
        self.std_email.set("")
        self.std_shift.set("")
        self.std_program.set("")
        self.std_gender.set("")
        self.std_contact.set("")
        self.std_dob.set("")
        self.txt_address.delete("1.0",END)
            
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        content=self.Student_table.item(cursor_row)
        row=content['values']
        self.std_enroll.set(row[0])
        self.std_name.set(row[1])
        self.std_email.set(row[2])
        self.std_shift.set(row[3])
        self.std_program.set(row[4])
        self.std_gender.set(row[5])
        self.std_contact.set(row[6])
        self.std_dob.set(row[7])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[8])
        
        
    def update_data(self):
        if self.std_enroll.get()=="" or self.std_name.get()=="":
            messagebox.showerror("Error","Please select data!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("update student set name=%s,email=%s,shift=%s,program=%s,gender=%s,conatct=%s,dob=%s,address=%s where enroll_no=%s",(
                                                                                    self.std_name.get(),
                                                                                    self.std_email.get(),
                                                                                    self.std_shift.get(),
                                                                                    self.std_program.get(),
                                                                                    self.std_gender.get(),
                                                                                    self.std_contact.get(),
                                                                                    self.std_dob.get(),
                                                                                    self.txt_address.get('1.0', END),
                                                                                    self.std_enroll.get()
                                                                                    ))
        

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record updated")
        
    def delete_data(self):
        if self.std_enroll.get()=="" or self.std_name.get()=="":
            messagebox.showerror("Error","Please select data!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("delete from student where enroll_no=%s",self.std_enroll.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success", "Record Deleted")
        
    def search_data(self):
        if self.search_txt.get()=="" or self.search_by.get()=="":
            messagebox.showerror("Error","Please select identity")
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close() 
         
root = Tk()
ob = Student(root)
root.mainloop()