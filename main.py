'''
This is a python program to make a simple image editing software.
'''
# Importing the necessary modules
import tkinter as tk

class App(tk.Tk):   # Creating the class App that inherits tkinter
    COLOR_THEME_COUNTER = True

    def __init__(self):     #initializing some basic properties
        super().__init__()
        #configuring basic information
        self.title("Edituer")

        # configuring the geometry
        self.geometry("1000x600")
        self.resizable(False,False)
        self.attributes("-fullscreen", False)
        # self.configure(bg="#0a52d8")
        self.configure(bg="#001e57")

        #widget methods
        self.create_widgets()

    def create_widgets(self):
        theme_Btn = tk.Button(self,
                            text="Change Theme",bg="orange", 
                            fg="#222c3d", 
                            font=("consolas", 10, "bold"), 
                            command=self.change_mode)
        theme_Btn.pack()

    def change_mode(self):
        if self.COLOR_THEME_COUNTER:
            self.configure(bg="#0a52d8")
        else:
            self.configure(bg="#001e57")
        self.COLOR_THEME_COUNTER = not self.COLOR_THEME_COUNTER
        


if __name__ == "__main__":
    app = App()
    app.mainloop()
