import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image,ImageTk
from resizeimage import resizeimage
import qrcode


class QR_Generator:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x550+220+60")
        self.root.config(background="#17202A")
        self.root.title("QR code Generator | Developed by TAHIR HABIB")
        self.root.resizable(False,False)

        label_heading = Label(self.root, text="  QR Code Generator", font=("Roboto", 40, "bold"), bg="#283747", fg="#85929E",
                              anchor="w").place(x=0, y=0, relwidth=1)
        # ___________________________________________Student Detail Frame______________________________________________
        # STUDENT DETAIL FRAME BOX
        std_frame = Frame(self.root, bd=2, bg="#17202A", relief=RIDGE)
        std_frame.place(x=50, y=100, width=500, height=430)

        # variables for student details
        self.var_std_name = StringVar()
        self.var_std_roll = StringVar()
        self.var_std_class = StringVar()
        self.var_std_depart = StringVar()

        # Label of student frame
        std_frame_title = Label(std_frame, text="Student Details", font=("Roboto", 20), bg="#283747", fg="#85929E").place(
            x=0, y=0, relwidth=1)

        # Labels for entries
        name_std_frame_title = Label(std_frame, text="Name:", font=("Roboto", 15), bg="#17202A", fg="#85929E").place(x=20,
                                                                                                                 y=60)
        roll_std_frame_title = Label(std_frame, text="Roll no.:", font=("Roboto", 15), bg="#17202A", fg="#85929E").place(
            x=20, y=100)
        class_std_frame_title = Label(std_frame, text="Class:", font=("Roboto", 15), bg="#17202A", fg="#85929E").place(x=20,
                                                                                                                   y=140)
        department_std_frame_title = Label(std_frame, text="Department:", font=("Roboto", 15), bg="#17202A",
                                           fg="#85929E").place(x=20, y=180)

        # Entry boxes
        name_std_frame_entry = Entry(std_frame, font=("Roboto", 15), textvariable=self.var_std_name, bg="#BFC9CA",
                                     fg="black").place(x=200, y=60)
        roll_std_frame_entry = Entry(std_frame, font=("Roboto", 15), textvariable=self.var_std_roll, bg="#BFC9CA",
                                     fg="black").place(x=200, y=100)
        class_std_frame_entry = Entry(std_frame, font=("Roboto", 15), textvariable=self.var_std_class, bg="#BFC9CA",
                                      fg="black").place(x=200, y=140)
        department_std_frame_entry = Entry(std_frame, font=("Roboto", 15), textvariable=self.var_std_depart, bg="#BFC9CA",
                                           fg="black").place(x=200, y=180)




        # Generate Button
        generate_button = Button(std_frame, text="Generate QR",command=self.generate,fg="black", font=("Roboto", 15, 'bold'), bg="#1F618D",
                                 ).place(x=20, y=280, width=200)
        # Clear Button
        clear_button = Button(std_frame, text="Clear",command=self.clear, font=("Roboto", 15, 'bold')
                              , bg="grey").place(x=20, y=330,width=200)

        # Massege
        self.msg = ""
        self.msg_label_heading = Label(std_frame, text=self.msg, font=("Roboto", 12), fg="#D6DBDF", bg="#17202A")
        self.msg_label_heading.place(x=20, y=380, width=200)

        choice_label = Label(std_frame, text="Choose QR Color", font=("Roboto", 12), bg="#17202A", fg="white").place(
            x=260, y=250, width=200)

        self.choices_background = ["White, Black", "White, Blue", "White, Red", "White, Green", "Black, Blue",
                              "Black, Golden"]
        self.back_ground = ttk.Combobox(std_frame, font=("Comic_Sans_MS", 10, "bold"), values=self.choices_background)
        self.back_ground.place(x=260, y=280,width=200)



        # ___________________________________________Display Frame_______________________________________________________________
        # QR displayer Frame
        QR_displayer_frame = Frame(self.root,bd=2,bg="#17202A",relief=RIDGE)
        QR_displayer_frame.place(x=600,y=100,width=250,height=430)

        # Label of displayer frame
        self.QR_displayer_frame_title = Label(QR_displayer_frame, text="QR Code",font=("Roboto", 20),bg="#283747",fg="#85929E").place(x=0,y=0,relwidth=1)

        # QR pic displayer
        self.qr_code = Label(QR_displayer_frame,text="No QR \n Available",font=("Roboto", 20),bg="#AAB7B8",fg="black",bd=2,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

        # msg under QR displayed
        self.final_msg = ""
        self.final_msg_label_heading = Label(QR_displayer_frame, text=self.msg, font=("Roboto", 12), fg="#D6DBDF", bg="#17202A")
        self.final_msg_label_heading.place(x=20, y=295, width=200)

        Exit_button = Button(QR_displayer_frame, text="Exit", bg="#C50400", fg="white", command=root.quit)
        Exit_button.place(x=24, y=355,width=200)


    def clear(self):
        self.var_std_name.set("")
        self.var_std_roll.set("")
        self.var_std_class.set("")
        self.var_std_depart.set("")
        self.msg = ""
        self.msg_label_heading.config(text=self.msg)
        self.final_msg = ""
        self.final_msg_label_heading.config(text=self.final_msg)
        self.qr_code.config(image="")


    def generate(self):
        if self.var_std_name.get()=="" or self.var_std_roll.get()=="" or self.var_std_class.get()=="" or self.var_std_depart.get()=="":
            self.msg="All Fields are Required!"
            self.msg_label_heading.config(text=self.msg,fg="red")
            self.final_msg = "Failed!"
            self.final_msg_label_heading.config(text=self.final_msg,fg="red")

        else:
            qr_data = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            qr_data.add_data(f"Name: {self.var_std_name.get()}\nRoll no.: {self.var_std_roll.get()}\nClass: {self.var_std_class.get()}\nDepartment: {self.var_std_depart.get()}")
            choice_background = self.back_ground.get()
            qr_data.make()


            if choice_background == self.choices_background[0]:
                img_qr_big = qr_data.make_image(fill_color='RGB(0, 0, 0)', back_color="RGB(255, 255, 255)").convert("RGB")

            elif choice_background == self.choices_background[1]:
                img_qr_big = qr_data.make_image(fill_color='RGB(4, 19, 171)', back_color="RGB(255, 255, 255)").convert("RGB")

            elif choice_background == self.choices_background[2]:
                img_qr_big = qr_data.make_image(fill_color='RGB(202, 0, 0)', back_color="RGB(255, 255, 255)").convert("RGB")

            elif choice_background == self.choices_background[3]:
                img_qr_big = qr_data.make_image(fill_color='RGB(7, 151, 0)', back_color="RGB(255, 255, 255)").convert("RGB")

            elif choice_background == self.choices_background[4]:
                img_qr_big = qr_data.make_image(fill_color='RGB(4, 19, 171)', back_color="RGB(0,0,0)").convert("RGB")

            elif choice_background == self.choices_background[5]:
                img_qr_big = qr_data.make_image(fill_color='RGB(244, 198, 56)', back_color="RGB(0,0,0)").convert("RGB")

            else:
                img_qr_big = qr_data.make_image(fill_color='RGB(0, 0, 0)', back_color="RGB(255, 255, 255)").convert("RGB")



            # img_qr_big = qr_data.make_image(fill_color='RGB(244, 198, 56)', back_color="RGB(0,0,0)").convert("RGB")
            img_qr_big=resizeimage.resize_cover(img_qr_big,[180,180])
            time_stamp = datetime.datetime.now().strftime('%b-%d-%Y_%I-%M-%S')
            img_qr_big.save(f"QR code {self.var_std_name.get()}{time_stamp}.png")

            self.im=ImageTk.PhotoImage(file=f"QR code {self.var_std_name.get()}{time_stamp}.png")
            self.qr_code.config(image=self.im)

            self.msg = "QR Generated Successfully!"
            self.msg_label_heading.config(text=self.msg,fg="#23BD01")

            self.final_msg = f"{self.var_std_name.get()}'s QR code.\n QR also saved in folder."
            self.final_msg_label_heading.config(text=self.final_msg,fg="#23BD01")



root=Tk()
obj = QR_Generator(root)
root.mainloop()