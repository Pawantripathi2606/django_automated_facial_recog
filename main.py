from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import train
from face_recognition import face_scanner

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")


        #self.main_frame = Frame(self.root, bg="white")
        #self.main_frame.place(x=0, y=0, width=1530, height=900)


    #0 img
        img = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\img.jpeg")
        img = img.resize((500,130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        self.first_lbl = Label(self.root, image=self.photoimg)
        self.first_lbl.place(x=0, y=0, width=500, height=130)

    #1  img    
        img1 = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\face.jpeg")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)  

        self.first_lbl1 = Label(self.root, image=self.photoimg1)  
        self.first_lbl1.place(x=500, y=0, width=500, height=130)

    #2 image     
        img2 = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\img2.jpeg")
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




        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTANDANCE SYSTEM SOFTWARE" , font=("times new roman",35,"bold"),bg="white",fg="dark blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)



# buttons 

        img4 = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\bro.png")
        img4 = img4.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)  

        #bg_img = Label(self.root, image=self.photoimg3)  
        #bg_img.place(x=0, y=130, width=1530, height=710)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100 , width=220,height=220)


        b1_1=Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=300 , width=220,height=40)


#2nd button 
        img5 = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\hh.jpg")
        img5 = img5.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)  

        

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100 , width=220,height=220)


        b1_1=Button(bg_img,text="FACE TRACKER ",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=300 , width=220,height=40)




        #3rd button 
        img6 = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\th.jpeg")
        img6 = img6.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)  

        

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100 , width=220,height=220)


        b1_1=Button(bg_img,text="ATTENDENCE",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=300 , width=220,height=40)




         #4th button 
        img7 = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\AV.jpeg")
        img7 = img7.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)  

        

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100 , width=220,height=220)


        b1_1=Button(bg_img,text="HELP CENTER",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=300 , width=220,height=40)



        #5th button 
        img8 = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\ml.jpeg")
        img8 = img8.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)  

        

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=400 , width=220,height=220)


        b1_1=Button(bg_img,text="DATA TRAINER",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=600 , width=220,height=40)




        #6th button 
        img9 = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\ph.jpeg")
        img9 = img9.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)  

        

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img,)
        b1.place(x=500,y=400 , width=220,height=220)


        b1_1=Button(bg_img,text="PHOTOS ",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=600 , width=220,height=40)




         #7th button 
        img10 = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\dev.jpeg")
        img10 = img10.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)  

        

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=400 , width=220,height=220)


        b1_1=Button(bg_img,text="DEVELOPER ",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=600 , width=220,height=40)




         #8th button 
        img11 = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\ex.jpeg")
        img11 = img11.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)  

        

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=400 , width=220,height=220)


        b1_1=Button(bg_img,text="EXIT ",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=600 , width=220,height=40)

    def open_img(self):
        os.startfile("data")


        #===function buttons
        

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.new_window.geometry("1530x900+0+0") 
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_scanner(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
