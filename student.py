from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")


        #====variables

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_addres=StringVar()
        self.var_teacher=StringVar()


#0 img
        img = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\qq.jpeg")
        img = img.resize((500,130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        self.first_lbl = Label(self.root, image=self.photoimg)
        self.first_lbl.place(x=0, y=0, width=500, height=130)

    #1  img    
        img1 = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\mm.jpeg")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)  

        self.first_lbl1 = Label(self.root, image=self.photoimg1)  
        self.first_lbl1.place(x=500, y=0, width=500, height=130)

    #2 image     
        img2 = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\tt.jpeg")
        img2 = img2.resize((550,130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)  

        self.first_lbl2 = Label(self.root, image=self.photoimg2)  
        self.first_lbl2.place(x=1000, y=0, width=550, height=130)


        #3 img for bg

        img3 = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\man.jpg")
        img3 = img3.resize((1530,710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)  

        bg_img = Label(self.root, image=self.photoimg3)  
        bg_img.place(x=0, y=130, width=1530, height=710)




        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT REPORT" , font=("times new roman",35,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=55,width=1515,height=640)

       #left lbl frame 

        Left_frame = LabelFrame(main_frame , bd = 2 , bg="white",relief=RIDGE , text = "STUDENT DETAILS" , font = ("times new roman" , 12 ,"bold"))
        Left_frame.place(x=10, y=10, width=730, height=580)


        img_left = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\men.jpg")
        img_left = img_left.resize((740,150), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)  

        self.first_lbl2 = Label(Left_frame, image=self.photoimg_left)  
        self.first_lbl2.place(x=5, y=0, width=720, height=150)



        #current course infooo


        current_course_frame = LabelFrame(Left_frame , bd = 2 , bg="white", relief=RIDGE , text = "CURRENT COURSE INFORMATION" , font = ("times new roman" , 12 ,"bold"))
        current_course_frame.place(x=5,y=135,width=725,height=115)


        #dept lvel 

        dep_level = Label(current_course_frame,text="DEPARTMENT",font = ("times new roman" , 12 ,"bold"),bg="white") 

        #grid line

        dep_level.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font = ("times new roman" , 12 ,"bold"),width = 22,state="readonly")
        dep_combo["values"]=("SELECT DEPARTMENT" , "COMPUTER SCIENCE" , "CIVIL ENGGERING" , "MACAHNICAL ENGGERING" , "ELECTRICAL ENGGERING")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10 ,sticky=W)

        #course combobox

        
        course_level = Label(current_course_frame,text="COURSE",font = ("times new roman" , 13 ,"bold"),bg="white")
        course_level.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font = ("times new roman" , 13 ,"bold"),width = 22,state="readonly")
        course_combo["values"]=("SELECT COURSE" , "COMPUTER SCIENCE ↴ ", "CSE - AI/ML" , "CSE - IOT" , "CSE - AIDS" , "CSE - DS" , "CIVIL ENGGERING ↴" ,"Construction Engineering","Structural Engineering","Geotechnical Engineering", "MACAHNICAL ENGGERING" , "ELECTRICAL ENGGERING")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10 ,sticky=W)


        #YEAR COMBO

        year_level = Label(current_course_frame,text="YEAR",font = ("times new roman" , 12 ,"bold"),bg="white")
        year_level.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font = ("times new roman" , 13 ,"bold"),width = 22,state="readonly")
        year_combo["values"]=("SELECT YEAR" , "2020-21","2021-22","2022-23","2023-24","2024-25","2025-26","2026-27")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10 ,sticky=W)


        #semester combo

        semester_level = Label(current_course_frame,text="SEMESTER",font = ("times new roman" , 12 ,"bold"),bg="white")
        semester_level.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font = ("times new roman" , 13 ,"bold"),width = 22,state="readonly")
        semester_combo["values"]=("SELECT SEMESTER" , "semester-1","semester-2","semester-3","semester-4","semester-5","semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10 ,sticky=W)
 
        #class student infoo
        class_student_frame = LabelFrame(Left_frame , bd = 2 , bg="white", relief=RIDGE , text = "CLASS STUDENT INFORMATION" , font = ("times new roman" , 12 ,"bold"))
        class_student_frame.place(x=5,y=250,width=750,height=300)


        #student id levl

        student_id_level = Label(class_student_frame,text="STUDENT-ID:",font = ("times new roman" , 12 ,"bold"),bg="white")
        student_id_level.grid(row=0,column=0,padx=10,sticky=W)


        #entry feild

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman" , 13 , "bold"))
        studentID_entry.grid(row=0,column=1,padx=10,sticky=W)



        #student name

        student_name_level = Label(class_student_frame,text="STUDENT NAME:",font = ("times new roman" , 12 ,"bold"),bg="white")
        student_name_level.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman" , 13 , "bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)


        #class section


        class_div_level = Label(class_student_frame,text="CLASS DIVISION:",font = ("times new roman" , 12 ,"bold"),bg="white")
        class_div_level.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_level_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font = ("times new roman" , 13 ,"bold"),width = 18,state="readonly")
        class_div_level_combo["values"]=("SELECT DIVISION" , "A","B","C","D","E")
        class_div_level_combo.current(0)
        class_div_level_combo.grid(row=1,column=1,padx=2,pady=5 ,sticky=W)


        #ROLL NO

        class_rollno_level = Label(class_student_frame,text="ROLL NO:",font = ("times new roman" , 12 ,"bold"),bg="white")
        class_rollno_level.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        class_rollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman" , 13 , "bold"))
        class_rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)



        #gender

        gender_level = Label(class_student_frame,text="GENDER:",font = ("times new roman" , 12 ,"bold"),bg="white")
        gender_level.grid(row=2,column=0,padx=10,pady=5,sticky=W)


        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font = ("times new roman" , 13 ,"bold"),width = 18,state="readonly")
        gender_combo["values"]=("SELECT GENDER" , "MALE" , "FEMALE", "OTHERS")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5 ,sticky=W)



        #gender_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman" , 13 , "bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #dob

        dob_level = Label(class_student_frame,text="DATE OF BIRTH:",font = ("times new roman" , 12 ,"bold"),bg="white")
        dob_level.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        dob_entry=ttk.Entry(class_student_frame ,textvariable=self.var_dob, width=20,font=("times of roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


        #email

        email_label = Label(class_student_frame,text="EMAIL:",font = ("times new roman" , 12 ,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        email_entry=ttk.Entry(class_student_frame , textvariable=self.var_email,width=20,font=("times of roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)



        #PHONE NO

        

        phone_level = Label(class_student_frame,text="PHONE NO:",font = ("times new roman" , 12 ,"bold"),bg="white")
        phone_level.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        phone_entry=ttk.Entry(class_student_frame ,textvariable=self.var_phone, width=20,font=("times of roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)



        #ADDRES

        addres_label = Label(class_student_frame,text="ADDRES:",font = ("times new roman" , 12 ,"bold"),bg="white")
        addres_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        addres_entry=ttk.Entry(class_student_frame ,textvariable=self.var_addres, width=20,font=("times of roman",13,"bold"))
        addres_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)


        
        #TEACHER NAME

        

        teacher_level = Label(class_student_frame,text="TEACHER NAME:",font = ("times new roman" , 12 ,"bold"),bg="white")
        teacher_level.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        teacher_entry=ttk.Entry(class_student_frame ,textvariable=self.var_teacher, width=20,font=("times of roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


        #radio buttons

        
        self.var_radio1 = StringVar()

# Radiobutton 1
        radiobtn1 = ttk.Radiobutton(class_student_frame, text="TAKE PHOTO SAMPLE", variable=self.var_radio1, value="Yes")
        radiobtn1.grid(row=6, column=0)

# Radiobutton 2 
        radiobtn2 = ttk.Radiobutton(class_student_frame, text="NO PHOTO SAMPLE", variable=self.var_radio1, value="No")
        radiobtn2.grid(row=6, column=1)




        #BUTTON FRAME

        btn_frame=Frame(class_student_frame ,bd=2 , relief = RIDGE , bg="white")
        btn_frame.place(x=0,y=205,width=715,height=35)

        #save button 
    
        save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width=17, font = ("times new roman" , 13, "bold"),bg="black",fg="white")
        save_btn.grid(row=0,column=0 )


        #update

        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,width=17, font = ("times new roman" , 13, "bold"),bg="black",fg="white")
        update_btn.grid(row=0,column=1 )


        #DELETE
        delete_btn=Button(btn_frame,text="DELETE",command=self.delete_data,width=17, font = ("times new roman" , 13, "bold"),bg="black",fg="white")
        delete_btn.grid(row=0,column=2 )

        #RESET
        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=17, font = ("times new roman" , 13, "bold"),bg="black",fg="white")
        reset_btn.grid(row=0,column=3 )


        btn_frame1=Frame(class_student_frame ,bd=2 , relief = RIDGE , bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)


        #TAKE SAMPLE PHOTO


        take_photosmpl_btn=Button(btn_frame1,text="TAKE A PHOTO SAMPLE",command=self.generate_dataset,width=35, font = ("times new roman" , 13, "bold"),bg="black",fg="white")
        take_photosmpl_btn.grid(row=0,column=0 )

        #UPDATE PHOTO

        update_photo_btn=Button(btn_frame1,text="UPDATE",width=35, font = ("times new roman" , 13, "bold"),bg="black",fg="white")
        update_photo_btn.grid(row=0,column=1 )


        #right lbl frame 

        right_frame = LabelFrame(main_frame ,bg="white", bd = 2 , relief=RIDGE , text = "STUDENT DETAILS" , font = ("times new roman" , 12 ,"bold"))
        right_frame.place(x=750, y=10, width=740, height=580)

        #right lbl img

        img_right = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\hde.jpg")
        img_right = img_right.resize((740,150), Image.Resampling.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)  

        self.first_lbl2 = Label(right_frame, image=self.photoimg_right)  
        self.first_lbl2.place(x=5 , y=0, width=725, height=150)



        #=====search system FRAME =====


        search_sys_frame = LabelFrame(right_frame , bd = 2 , bg="white", relief=RIDGE , text = "SEARCH SYSTEM" , font = ("times new roman" , 12 ,"bold"))
        search_sys_frame.place(x=5,y=135,width=725,height=70)


        #search by 
        search_level = Label(search_sys_frame,text="SEARCH BY:",font = ("times new roman" , 15 ,"bold"),bg="black", fg="white")
        search_level.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        #select combo
        search_combo=ttk.Combobox(search_sys_frame,font = ("times new roman" , 13 ,"bold"),width = 15,state="readonly")
        search_combo["values"]=("SELECT" , "roll_no","phone_no","semester-3","semester-4","semester-5","semester-8")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10 ,sticky=W)



        search_entry=ttk.Entry(search_sys_frame , width=15,font=("times of roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)



        search_btn=Button(search_sys_frame,text="SEARCH",width=12, font = ("times new roman" , 12, "bold"),bg="black",fg="white")
        search_btn.grid(row=0,column=3, padx=4 )

 
        showall_btn=Button(search_sys_frame,text="SHOW ALL",width=12, font = ("times new roman" , 12, "bold"),bg="black",fg="white")
        showall_btn.grid(row=0,column=4 , padx =4 )


        #===tabel frame

        tabel_frame = Frame(right_frame , bd = 2 , bg="white", relief=RIDGE)
        tabel_frame.place(x=5,y=210,width=725,height=350)


        #scroll bar


        scroll_x=ttk.Scrollbar(tabel_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tabel_frame,orient=VERTICAL)

        

        self.student_tabel=ttk.Treeview(tabel_frame,column=("dep","course","year","sem","id","name","div","dob","email","phone","addres","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_tabel.xview)
        scroll_y.config(command=self.student_tabel.yview)


        self.student_tabel.heading("dep",text="DEPARTMENT")
        self.student_tabel.heading("course",text="COURSE")
        self.student_tabel.heading("year",text="YEAR")
        self.student_tabel.heading("sem",text="SEMESTER")
        self.student_tabel.heading("id",text="STUDENT ID")
        self.student_tabel.heading("name",text="NAME")
        self.student_tabel.heading("div",text="DIVISON")
        self.student_tabel.heading("dob",text="DOB")
        self.student_tabel.heading("email",text="EMAIL")
        self.student_tabel.heading("phone",text="PHONE")
        self.student_tabel.heading("addres",text="ADDRES")
        self.student_tabel.heading("teacher",text="TEACHER")
        self.student_tabel.heading("photo",text="PHOTO")
        self.student_tabel["show"]="headings"

        self.student_tabel.column("dep",width=100)
        self.student_tabel.column("course",width=100)
        self.student_tabel.column("year",width=100)
        self.student_tabel.column("sem",width=100)
        self.student_tabel.column("id",width=100)
        self.student_tabel.column("name",width=100)
        self.student_tabel.column("div",width=100)
        self.student_tabel.column("dob",width=100)
        self.student_tabel.column("email",width=100)
        self.student_tabel.column("phone",width=100)
        self.student_tabel.column("addres",width=100)
        self.student_tabel.column("teacher",width=100)
        self.student_tabel.column("photo",width=150)
       



        self.student_tabel.pack(fill=BOTH,expand=1)
        self.student_tabel.bind("<ButtonRelease>",self.get_cursor)
        self.fatch_data()

    #====function declaration

    def add_data(self):
        if self.var_dep.get() == "SELECT DEPARTMENT" or self.var_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="pawantripathi26062005@",
                    database="attandence_sys"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("""
                    INSERT INTO student (
                        dep, course, year, semester, student_id, name, division, dob, email, phone, address, teacher, photosample
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_addres.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)




#=======fatching data from db


    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="pawantripathi26062005@", database=" attandence_sys")
        my_cursor = conn.cursor()
        my_cursor.execute("select*from student")
        data=my_cursor.fetchall()


        if len(data)!=0:
            self.student_tabel.delete(*self.student_tabel.get_children())
            for i in data :
                self.student_tabel.insert("",END,values=i)
            conn.commit()
        conn.close()
        

        #===GETCOURSER


    def get_cursor(self,event=""):
        cursor_focus=self.student_tabel.focus()
        content=self.student_tabel.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_addres.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])



# UPDATE FUNCTION

    def update_data(self):
        if self.var_dep.get() == "SELECT DEPARTMENT" or self.var_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "DO YOU WANT TO UPDATE THIS STUDENT DETAILS", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="pawantripathi26062005@",
                        database="attandence_sys"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("""
                        UPDATE student SET
                            dep=%s, course=%s, year=%s, semester=%s, name=%s, division=%s, dob=%s, email=%s, phone=%s, address=%s, teacher=%s, photosample=%s
                        WHERE student_id=%s
                    """, (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_addres.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                    ))
                    conn.commit()
                    self.fatch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


    #delete function

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student Id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn=mysql.connector.connect(
                        host="localhost",username="root",password="pawantripathi26062005@",database="attandence_sys"
                    )
                    mysql_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    mysql_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #reset data


    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_addres.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #=======generate data set / take photo sample
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_id.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="pawantripathi26062005@", database="attandence_sys")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s", (



                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_name.get(),
                    self.var_div.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_addres.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get() == id + 1
                ))

                conn.commit()
                self.fatch_data()
                self.reset_data()
                conn.close()

                # =========== Load predefined data on face frontals from opencv =========
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                    # scaling factor=1.3
                    # Minimum neighbor = 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    return None
            

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)


                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        cv2.waitKey(1)==13 or int(img_id)==100
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets compled!!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)



        


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()        