from tkinter import *
from tkinter import filedialog,messagebox, simpledialog
from PIL import Image,ImageTk
import im

class MyWindow:

    def __init__(self):
        self.win = Tk()
        screen_height = self.win.winfo_screenheight()
        self.win.geometry(f"1000x{screen_height}+300+0")
        self.win.title("Image project")
        self.img = None
        self.selected_shape = ''
        self.processing = ''
        background_image = Image.open("background.jpg")
        background_photo = ImageTk.PhotoImage(background_image)

        #--------הוספת תמונה כרקע ---------
        background_label = Label(self.win, image=background_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #--------הגדרת אייקונים לכפתורים--------
        icon_image = Image.open("picture.png")
        icon_image = icon_image.resize((24,24),Image.LANCZOS)
        self.icon1 = ImageTk.PhotoImage(icon_image)

        icon_image = Image.open("cut.png")
        icon_image = icon_image.resize((24, 24), Image.LANCZOS)
        self.icon2 = ImageTk.PhotoImage(icon_image)

        icon_image = Image.open("text.png")
        icon_image = icon_image.resize((24, 24), Image.LANCZOS)
        self.icon3 = ImageTk.PhotoImage(icon_image)

        icon_image = Image.open("shapes.png")
        icon_image = icon_image.resize((24, 24), Image.LANCZOS)
        self.icon4 = ImageTk.PhotoImage(icon_image)

        icon_image = Image.open("save.png")
        icon_image = icon_image.resize((24, 24), Image.LANCZOS)
        self.icon5 = ImageTk.PhotoImage(icon_image)

        icon_image = Image.open("exit.png")
        icon_image = icon_image.resize((24, 24), Image.LANCZOS)
        self.icon6 = ImageTk.PhotoImage(icon_image)

        #---------הגדרת כפתורים------------

        self.btn1 = Button(self.win,
                           text="add image",
                           relief="raised",
                           bg="white",
                           fg="purple",
                           width=350,
                           height=50,
                           command=self.open_file_dialog,
                           image=self.icon1,
                           compound=LEFT)

        self.btn2 = Button(self.win,
                           text="crop image",
                           relief="raised",
                           bg="white",
                           fg="purple",
                           width=350,
                           height=50,
                           command=self.crop_image,
                           image=self.icon2,
                           compound=LEFT)

        self.btn3 = Button(self.win,
                           text="add text",
                           relief="raised",
                           bg="white",
                           fg="purple",
                           width=350,
                           height=50,
                           command=self.add_text,
                           image=self.icon3,
                           compound=LEFT)

        self.btn4 = Button(self.win,
                           text="add a shape",
                           relief="raised",
                           bg="white",
                           fg="purple",
                           width=350,
                           height=50,
                           command=self.add_a_shape,
                           image=self.icon4,
                           compound=LEFT)

        self.btn5 = Button(self.win,
                           text="save",
                           relief="raised",
                           bg="white",
                           fg="purple",
                           width=350,
                           height=50,
                           command=self.save,
                           image=self.icon5,
                           compound=LEFT)

        self.btn6 = Button(self.win,
                           text="exit",
                           relief="raised",
                           bg="white",
                           fg="purple",
                           width=350,
                           height=50,
                           command=self.exit,
                           image=self.icon6,
                           compound=LEFT)

        #-------הגדרת כפתורי צורות---------

        self.circle_btn = Button(self.win,
                                 text="circle",
                                 bg="orange",
                                 fg="white",
                                 width=20,
                                 height=2,
                                 command=lambda :self.set_shape("circle"))

        self.triangle_btn = Button(self.win,
                                   text="triangle",
                                 bg="orange",
                                 fg="white",
                                 width=20,
                                   height=2,
                                 command=lambda: self.set_shape("triangle"))

        self.rectangle_btn = Button(self.win,
                                 text="rectangle",
                                 bg="orange",
                                 fg="white",
                                 width=20,
                                height=2,
                                 command=lambda: self.set_shape("rectangle"))

        self.line_btn = Button(self.win,
                                 text="line",
                                 bg="orange",
                                 fg="white",
                                 width=20,
                                 height=2,
                                 command=lambda: self.set_shape("line"))

        self.ellipse_btn = Button(self.win,
                                 text="ellipse",
                                 bg="orange",
                                 fg="white",
                                 width=20,
                                 height=2,
                                 command=lambda: self.set_shape("ellipse"))
        #-------הגדרת כפתורי עיבוד----------

        self.adjust_brightness = Button(self.win,
                                       text = "adjust_brightness",
                                        bg="orange",
                                        fg="white",
                                        width=20,
                                        height=2,
                                        command=lambda: self.set_processing("adjust_brightness"))

        self.adjust_contrast = Button(self.win,
                                      text = "adjust_contrast",
                                      bg="orange",
                                      fg="white",
                                      width=20,
                                      height=2,
                                      command=lambda: self.set_processing("adjust_contrast"))

        self.add_tint = Button(self.win,
                               text = "add_tint",
                               bg="orange",
                               fg="white",
                               width=20,
                               height=2,
                               command=lambda: self.set_processing("add_tint"))

        self.blur_image = Button(self.win,
                                 text = "blur_image",
                                 bg="orange",
                                 fg="white",
                                 width=20,
                                 height=2,
                                 command=lambda: self.set_processing("blur_image"))

        self.sharpen_image = Button(self.win,
                                    text = "sharpen_image",
                                    bg="orange",
                                    fg="white",
                                    width=20,
                                    height=2,
                                    command=lambda: self.set_processing("sharpen_image"))

        self.positions()
        self.win.mainloop()

        #---------בחירת צורה--------

    def set_shape(self, shape):
        self.selected_shape = shape
        if self.selected_shape == "circle":
            self.img.draw_circle()
        elif self.selected_shape == "triangle":
            self.img.draw_triangle()
        elif self.selected_shape == "rectangle":
            self.img.draw_rectangle()
        elif self.selected_shape == "line":
            self.img.draw_line()
        elif self.selected_shape == "ellipse":
            self.img.draw_ellipse()
        else:
            print("No shape selected.")

    #------------בחירת עיבוד------------

    def set_processing(self, processing):
        self.processing = processing
        if self.processing == "adjust_brightness":
            self.img.adjust_brightness()
        elif self.processing == "adjust_contrast":
            self.img.adjust_contrast()
        elif self.processing == "add_tint":
            self.img.add_tint()
        elif self.processing == "blur_image":
            self.img.blur_image()
        elif self.processing == "sharpen_image":
            self.img.sharpen_image()
        else:
             print("No shape processing.")

    #------------קביעת מיקומים----------

    def positions(self):

        self.btn1.place(relx=0.5, rely=0.25, anchor=CENTER)
        self.btn2.place(relx=0.5, rely=0.35, anchor=CENTER)
        self.btn3.place(relx=0.5, rely=0.45, anchor=CENTER)
        self.btn4.place(relx=0.5, rely=0.55, anchor=CENTER)
        self.btn5.place(relx=0.5, rely=0.65, anchor=CENTER)
        self.btn5.config(command=self.save)
        self.btn6.place(relx=0.5, rely=0.75, anchor=CENTER)
        self.btn6.config(command=self.exit)

    #-----------העלאת תמונה------------

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename()
        print("selected file", file_path)
        self.img = im.MyImage(file_path, "image")
        self.img.change_random_color()

        self.adjust_brightness.grid(row=2, column=2, padx=21, pady=20)
        self.adjust_contrast.grid(row=2, column=10, padx=21)
        self.add_tint.grid(row=2, column=18, padx=21)
        self.blur_image.grid(row=2, column=26, padx=21)
        self.sharpen_image.grid(row=2, column=32, padx=21)

    #------------הגדרת מיקומי כפתורי צורה------------

    def add_a_shape(self):
        self.circle_btn.grid(row=20, column=2,padx=21, pady=650)
        self.triangle_btn.grid(row=20, column=10,padx=21, pady=650)
        self.line_btn.grid(row=20, column=18,padx=21, pady=650)
        self.rectangle_btn.grid(row=20, column=26,padx=21, pady=650)
        self.ellipse_btn.grid(row=20, column=32, padx=21, pady=650)

    #---------הוספת טקסט---------

    def add_text(self):
        self.img.add_text()

    #-------- חיתוך תמונה ----------

    def crop_image(self):
        self.img.crop_image()

    #-----------שמירת תמונה------------

    def save(self):
        if self.img is not None:
            file_path =filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                self.img.save_image(file_path)
                print("image saved successfully.")
            else:
                print("save operation canceled.")
        else:
            print("no image loaded.")

    #----------סגירת החלונית---------

    def exit(self):
        self.win.destroy()

m=MyWindow()
