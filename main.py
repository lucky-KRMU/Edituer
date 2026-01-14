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

        # Creating The Menu bar
        menubar = tk.Menu()

        # This is for the file menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open File", command=self.open_file)
        file_menu.add_command(label="Export File", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_program)
        menubar.add_cascade(label="File", menu=file_menu)

        # This is for the Help Menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About Us", command=self.tell_about_us)
        menubar.add_cascade(label="Help", menu=help_menu)



        self.config(menu=menubar)

        #widget methods
        self.create_widget_theme_change()
        self.display_image()
        self.create_size_change_btn()
        self.make_all_filter_images()

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
                            pady=5,command=self.change_img_size)
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
    
    



    def make_all_filter_images(self,cv_img_cvt="demo.jpg"):
       cv_img = cv.imread(cv_img_cvt)

       #Converting them into various filter photos and then saving them in the ./Photo_DB 
       
       gaussianBlur_img = cv.GaussianBlur(cv_img, (5,5), 0)
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
           message="This is a simple image editing software."
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
