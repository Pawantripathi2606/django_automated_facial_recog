from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np

class train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")



        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\Dark-background-free-download.jpg") 
        img_top = img_top.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)

        b1_1 = Button(self.root, text="TRAIN DATA",  cursor="hand2", font=("times new roman", 30, "bold"), bg="black", fg="white")    
        b1_1.place(x=0, y=380, width=1530, height=60)


        img_down = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\Dark-background-free-download.jpg") 
        img_down = img_down.resize((1530, 325), Image.Resampling.LANCZOS)
        self.photoimg_down = ImageTk.PhotoImage(img_down)

        f_lbl = Label(self.root, image=self.photoimg_down)
        f_lbl.place(x=0, y=440, width=1530, height=325)   

        b1_1 = Button(f_lbl, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="black", fg="white")
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("times new roman", 30, "bold"), bg="black", fg="white")
        b1_1.place(x=0, y=380, width=1530, height=60)

        img_down = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\Dark-background-free-download.jpg")
        img_down = img_down.resize((1530,325),Image.Resampling.LANCZOS)
        self.photoimg_down = ImageTk.PhotoImage(img_down)
        f_lbl = Label(self.root, image=self.photoimg_down)
        f_lbl.place(x=0, y=440, width=1530, height=325)


    #lbph algorithm 

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # convert to grayscale
            image_np = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

           
            
            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training", image_np)
            cv2.waitKey(1) == 13
        ids = np.array(ids)


        #====training of classifier
        #===and save


        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!!!")
 
       

        

if __name__ == "__main__":
    root = Tk()
    obj = train(root)
    root.mainloop()               