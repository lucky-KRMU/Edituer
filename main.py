'''
This is a python program to make a simple image editing software.
'''
# Importing the necessary modules
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk
import cv2 as cv

class App(tk.Tk):   # Creating the class App that inherits tkinter
    COLOR_THEME_COUNTER = False

    WIDTH_IMG = 300
    HEIGHT_IMG = 300

    MAIN_IMG_CV = "demo.jpg" # Default image
    HEAD = MAIN_IMG_CV
    EXPORT_IMG_PATH = ""

    def __init__(self):     #initializing some basic properties
        super().__init__()
        #configuring basic information
        self.title("Edituer")

        # configuring the geometry
        self.geometry("1000x600")
        self.resizable(False,False)
        self.attributes("-fullscreen", False)
        self.configure(bg="#383838")
        self.iconbitmap("icon.ico")

        # Creating The Menu bar
        menubar = tk.Menu()

        # This is for the file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Image", command=self.open_file)
        file_menu.add_command(label="Export Image", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_program)
        menubar.add_cascade(label="File", menu=file_menu)

        # This is for the Help Menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About Us", command=self.tell_about_us)
        menubar.add_cascade(label="Help", menu=help_menu)



        self.config(menu=menubar)



        # Making filter buttons grid




        #widget methods
        self.create_widget_theme_change()
        self.add_label_text()
        self.display_image()
        self.create_size_change_btn()
        self.make_all_filter_images()
        self.btns_grid()

    def create_widget_theme_change(self):
        theme_Btn = tk.Button(self,
                            text="Change Theme",bg="#1F51FF", 
                            fg="white", 
                            font=("helvetica", 10, "bold"),
                            relief="flat", 
                            bd=5,
                            cursor="star",
                            padx=5, 
                            pady=5,
                            command=self.change_mode)
        theme_Btn.pack()
        theme_Btn.place(x=10,y=10)
    
    def create_size_change_btn(self):
        size_change_btn = tk.Button(self, 
                            text="Change size",
                            bg="#1F51FF", 
                            fg="white", 
                            font=("helvetica", 10, "bold"),
                            relief="flat", 
                            bd=5,
                            cursor="star",
                            padx=5, 
                            pady=5,
                            height=1,
                            width=10,
                            command=self.change_img_size)
        size_change_btn.pack()
        size_change_btn.place(x=700,y=280)

    def display_image(self,corX=150, corY=50, sizeX=WIDTH_IMG, sizeY=HEIGHT_IMG, img_to_dis="demo.jpg"):
       #Reading the basic image and displaying it.
       cv_img = cv.imread(str(img_to_dis))
       cv_img_resized = cv.resize(cv_img, (sizeX,sizeY), interpolation=cv.INTER_AREA)
       image_cvt = cv.cvtColor(cv_img_resized, cv.COLOR_BGR2RGB)
       image = Image.fromarray(image_cvt)
       tk_image = ImageTk.PhotoImage(image=image)
       


       img_label = tk.Label(self, image=tk_image)
       img_label.image = tk_image
       img_label.pack()
       img_label.place(x=corX,y=corY)
    
    def btns_grid(self):
       canny_Btn = tk.Button(self,
                            text="Sketch",bg="#1F51FF", 
                            fg="white", 
                            font=("helvetica", 10, "bold"),
                            relief="flat", 
                            bd=5,
                            cursor="star",
                            padx=5, 
                            pady=5,
                            width=10,
                            command=self.to_canny
       ) 
       dialated_Btn = tk.Button(self,
                            text="Dialate",bg="#1F51FF", 
                            fg="white", 
                            font=("helvetica", 10, "bold"),
                            relief="flat", 
                            bd=5,
                            cursor="star",
                            padx=5, 
                            pady=5,
                            width=10,
                            command=self.to_dialated
       ) 
       gaussianBlur_Btn = tk.Button(self,
                            text="Blur",bg="#1F51FF", 
                            fg="white", 
                            font=("helvetica", 10, "bold"),
                            relief="flat", 
                            bd=5,
                            cursor="star",
                            padx=5, 
                            pady=5,
                            width=10,
                            command=self.to_blur
       ) 
       hsv_Btn = tk.Button(self,
                            text="Funky",bg="#1F51FF", 
                            fg="white", 
                            font=("helvetica", 10, "bold"),
                            relief="flat", 
                            bd=5,
                            cursor="star",
                            padx=5, 
                            pady=5,
                            width=10,
                            command=self.to_hsv
       ) 
       lab_Btn = tk.Button(self,
                            text="Ghost",bg="#1F51FF", 
                            fg="white", 
                            font=("helvetica", 10, "bold"),
                            relief="flat", 
                            bd=5,
                            cursor="star",
                            padx=5, 
                            pady=5,
                            width=10,
                            command=self.to_lab
       ) 
       monochrome_Btn = tk.Button(self,
                            text="Monochrome",bg="#1F51FF", 
                            fg="white", 
                            font=("helvetica", 10, "bold"),
                            relief="flat", 
                            bd=5,
                            cursor="star",
                            padx=5, 
                            pady=5,
                            width=10,
                            command=self.to_monochrome
       ) 
       normal_Btn = tk.Button(self,
                            text="Normal",bg="#1F51FF", 
                            fg="white", 
                            font=("helvetica", 10, "bold"),
                            relief="flat", 
                            bd=5,
                            cursor="star",
                            padx=5, 
                            pady=5,
                            width=10,
                            command=self.to_normal
       ) 
       export_Btn = tk.Button(self,
                            text="Export",bg="#1F51FF", 
                            fg="white", 
                            font=("helvetica", 10, "bold"),
                            relief="flat", 
                            bd=5,
                            cursor="star",
                            padx=5, 
                            pady=5,
                            width=10,
                            command=self.export_img           
       )

       canny_Btn.pack()
       dialated_Btn.pack()
       gaussianBlur_Btn.pack()
       hsv_Btn.pack()
       lab_Btn.pack()
       monochrome_Btn.pack()
       normal_Btn.pack()
       export_Btn.pack()

       canny_Btn.place(x=100, y=450)
       dialated_Btn.place(x=300, y=450)
       gaussianBlur_Btn.place(x=500, y=450)
       hsv_Btn.place(x=700, y=450)
       lab_Btn.place(x=100, y=520)
       monochrome_Btn.place(x=300, y=520)
       normal_Btn.place(x=500, y=520)
       export_Btn.place(x=700, y=520) 



    def make_all_filter_images(self,cv_img_cvt="demo.jpg"):
       cv_img = cv.imread(cv_img_cvt)

       #Converting them into various filter photos and then saving them in the ./Photo_DB 
       
       gaussianBlur_img = cv.GaussianBlur(cv_img, (7,7), 0)
       cv.imwrite("./Photo_DB/gaussianBlur.jpg", gaussianBlur_img)

       canny_img = cv.Canny(cv_img, 100,100)
       cv.imwrite("./Photo_DB/canny.jpg", canny_img)

       monochrome_img = cv.cvtColor(cv_img, cv.COLOR_RGB2GRAY)
       cv.imwrite("./Photo_DB/monochrome.jpg", monochrome_img)

       hsv_img = cv.cvtColor(cv_img, cv.COLOR_BGR2HSV)
       cv.imwrite("./Photo_DB/hsv.jpg", hsv_img)

       lab_img = cv.cvtColor(cv_img, cv.COLOR_BGR2LAB) 
       cv.imwrite("./Photo_DB/lab.jpg", lab_img)
       
       dialated_img = cv.dilate(cv_img, (7,7), iterations=1)
       cv.imwrite("./Photo_DB/dialated.jpg", dialated_img)

       normal = cv_img
       cv.imwrite("./Photo_DB/normal.jpg", normal)

    def add_label_text(self):
        img_preview = tk.Label(self,
                               text="Preview (Image not to size)",
                               font=("helvetica", 15, "bold"),
                               fg="white",
                               bg="#1F51FF")
        img_preview.pack()
        img_preview.place(x=180, y=10)

        filter_options = tk.Label(self,
                                  text="Filter options: ",
                                  fg="white",
                                  bg="#00229E",
                                  font=("helvetica", 15, "bold"))
        filter_options.pack()

    def change_mode(self):
        if self.COLOR_THEME_COUNTER:
            self.configure(bg="#383838")
        else:
            self.configure(bg="#c9c9c9")
        self.COLOR_THEME_COUNTER = not self.COLOR_THEME_COUNTER

    def change_img_size(self):
        self.WIDTH_IMG = 90
        self.HEIGHT_IMG = 160
        print("size changed.")

    def open_file(self):
       self.HEAD = askopenfilename(
           title="Choose your image to be edited",
           filetypes=[
               ("Image file (JPG/JPEG)","*.jpg"),
               ("Image File Types (PNG)", "*.png")
           ]
       )
       self.display_image(img_to_dis=self.HEAD)
       self.make_all_filter_images(cv_img_cvt=self.HEAD)

    def save_file(self):
       print("File Opened.")
    
    def exit_program(self):
       self.destroy()

    def tell_about_us(self):
        messagebox.showinfo(
           title="About Us",
           message="This is a simple image editing software.",
           icon="info"
        )

    def to_canny(self):
        self.display_image(img_to_dis="./Photo_DB/canny.jpg")

    def to_dialated(self):
        self.display_image(img_to_dis="./Photo_DB/dialated.jpg")

    def to_blur(self):
        self.display_image(img_to_dis="./Photo_DB/gaussianBlur.jpg")

    def to_hsv(self):
        self.display_image(img_to_dis="./Photo_DB/hsv.jpg")

    def to_lab(self):
        self.display_image(img_to_dis="./Photo_DB/lab.jpg")

    def to_monochrome(self):
        self.display_image(img_to_dis="./Photo_DB/monochrome.jpg")

    def to_normal(self):
        self.display_image(img_to_dis="./Photo_DB/normal.jpg")

    def export_img(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
