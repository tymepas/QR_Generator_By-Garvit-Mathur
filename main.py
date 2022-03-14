from tkinter import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage


class QR_Generator():
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR_Generator by Garvit Mathur")
        self.root.resizable(False, False)

        title = Label(self.root, text="  QR Generator", font=("times new roman", 40), bg="#053246", fg="white",
                      anchor="w").place(x=0, y=0, relwidth=1)

        # Employee Details Window
        # Variables

        self.var_emp_code = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_department = StringVar()
        self.var_emp_designation = StringVar()

        emp_frame = Frame(self.root, bd=2, relief=RIDGE, bg="White")
        emp_frame.place(x=50, y=100, width=500, height=350)

        emp_title = Label(emp_frame, text="Employee Details", font=("times new roman", 20), bg="#00111a", fg="white",
                          ).place(x=0, y=0, relwidth=1)

        emp_label_Code = Label(emp_frame, text="Employee ID", font=("times new roman", 15, 'bold'), bg="white").place(
            x=20, y=60)
        emp_label_Name = Label(emp_frame, text="Employee Name", font=("times new roman", 15, 'bold'), bg="white").place(
            x=20, y=100)
        emp_label_Dept = Label(emp_frame, text='Department', font=("times new roman", 15, 'bold'), bg="white").place(
            x=20, y=140)
        emp_label_Designation = Label(emp_frame, text="Designation", font=("times new roman", 15, 'bold'),
                                      bg="white").place(x=20, y=180)

        txt_label_Code = Entry(emp_frame, font=("times new roman", 13,), textvariable=self.var_emp_code,
                               bg="lightyellow").place(x=200, y=60, width=200)
        txt_label_Name = Entry(emp_frame, font=("times new roman", 13,), textvariable=self.var_emp_name,
                               bg="lightyellow").place(x=200, y=100, width=200)
        txt_label_Dept = Entry(emp_frame, font=("times new roman", 13,), textvariable=self.var_emp_department,
                               bg="lightyellow").place(x=200, y=140, width=200)
        txt_label_Designation = Entry(emp_frame, font=("times new roman", 13,), textvariable=self.var_emp_designation,
                                      bg="lightyellow").place(x=200, y=180, width=200)

        btn_generate = Button(emp_frame, text="Generate QR", command=self.generate,
                              font=("times new roman", 18, 'bold'),
                              bg='#2196f3', fg='white').place(x=90, y=250, width=180, height=30)
        btn_clear = Button(emp_frame, text="Clear", command=self.clear, font=("times new roman", 15, 'bold'),
                           bg='#607d8b', fg='white').place(x=350, y=250, width=100, height=25)

        self.msg = ""
        self.label_msg = Label(emp_frame, text=self.msg, font=("times new roman", 12, 'bold'),
                               bg='white', fg='green')
        self.label_msg.place(x=0, y=300, relwidth=1)

        # Employee QR Generate Window

        qr_frame = Frame(self.root, bd=2, relief=RIDGE, bg="White")
        qr_frame.place(x=600, y=100, width=260, height=350)

        qr_title = Label(qr_frame, text="Employee QR Code", font=("times new roman", 20), bg="#00111a", fg="white",
                         ).place(x=0, y=0, relwidth=1)
        self.qr_code = Label(qr_frame, text="No QR \nAvailable", font=("times new roman", 15), bg='#99ebff',
                             fg='black', bd=1, relief=RIDGE)
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def clear(self):
        self.var_emp_code.set('')
        self.var_emp_name.set('')
        self.var_emp_department.set('')
        self.var_emp_designation.set('')
        self.msg = ""
        self.label_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_emp_code.get() == '' or self.var_emp_name.get() == '' or self.var_emp_department.get() == '' or self.var_emp_designation.get() == '':
            self.msg = "All Fields are Required!!!"
            self.label_msg.config(text=self.msg, fg='Red')

        else:
            qr_data = (f"Emplyee ID: {self.var_emp_code.get()}\nEmployee Name: {self.var_emp_name.get()}\n"
                       f"Employee Department: {self.var_emp_department.get()}\nEmployee Designation: {self.var_emp_designation.get()}")
            qr_code = qrcode.make(qr_data)
            print(qr_code)
            qr_code = resizeimage.resize_cover(qr_code, [180, 180])
            qr_code.save("Employee_QR/Emp_" + str(self.var_emp_code.get()) + ".png")

            # QR Code Image Update
            self.img = ImageTk.PhotoImage(file="Employee_QR/Emp_" + str(self.var_emp_code.get()) + ".png")
            self.qr_code.config(image=self.img)

            # updating notifications
            self.msg = "QR Generated Successfully!!!"
            self.label_msg.config(text=self.msg, fg='green')


root = Tk()
obj = QR_Generator(root)
root.mainloop()
