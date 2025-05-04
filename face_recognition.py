from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np


class face_scanner:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face Recognition System")


        title_lbl = Label(self.root, text="FACE SCANNER", font=("times new roman", 35, "bold"), bg="black", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        img_top = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\faceee.jpg")
        img_top = img_top.resize((690, 850), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=650, height=850)

        b1_1 = Button(f_lbl, text="FACE SCANNER", cursor="hand2", command=self.face_scanner, font=("times new roman", 18, "bold"), bg="DARK BLUE", fg="white")
        b1_1.place(x=45, y=340, width=200, height=200)


        img_side = Image.open(r"C:\Users\Lenovo\Desktop\face_recognization\images_for_bg\1_DPNoWJ3Au35Fw58Sn2oj1w.png")
        img_side = img_side.resize((950, 850), Image.Resampling.LANCZOS)
        self.photoimg_side = ImageTk.PhotoImage(img_side)

        f_lbl = Label(self.root, image=self.photoimg_side)
        f_lbl.place(x=650, y=45, width=950, height=850)


    def face_scanner(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))


                print(f"Predicted ID: {id}, Confidence: {confidence}")

                conn = mysql.connector.connect(host="localhost", username="root", password="pawantripathi26062005@", database="attandence_sys")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT roll from student WHERE student_id=%s", (id,))
                r = my_cursor.fetchone()
                r = "+".join(r) if r is not None else "Unknown"

                my_cursor.execute("SELECT name from student WHERE student_id=%s", (id,))
                i = my_cursor.fetchone()
                i = "+".join(i) if i is not None else "Unknown"

                my_cursor.execute("SELECT dep from student WHERE student_id=%s", (id,))
                d = my_cursor.fetchone()
                d = "+".join(d) if d is not None else "Unknown"

                conn.close()

                print(f"Student ID: {id}, Roll: {r}, Name: {i}, Department: {d}")

                if confidence > 40:
                    cv2.putText(img, f"ROLL:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"NAME:{i}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"DEP:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "UNKNOWN FACE", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 225), "face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNITION", img)

            if cv2.waitKey(1) & 0xFF == 27:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = face_scanner(root)
    root.mainloop()
