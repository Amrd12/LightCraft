import customtkinter as ctk
from configs.app_colors import AppColors, appColors
from configs.app_strings import appStrings
from models.img_model import ImgModel
from PIL import Image ,ImageTk
from tkinter import Canvas

class EditingScreen(ctk.CTkFrame):
    appColor: AppColors = appColors
    image: ImgModel

    def __init__(self, image: ImgModel, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            fg_color=self.appColor.color4,
            corner_radius=10,
        )
        
        self.image = image
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.create_label()
        self.show_image()

    def create_label(self):
            closeLight = Image.open(appStrings.closeLight)
            closeDark = Image.open(appStrings.closeDark)
            close_img_resized = ctk.CTkImage(closeDark ,closeLight, size=(25, 25))
            label = ctk.CTkLabel(self, image=close_img_resized, corner_radius=10, text=self.image.imgName , anchor="w" ,compound="right")
            label.bind("<Button-1>", self.close)
            label.grid(row=0, column=0, sticky="NSEW")

    def close(self, *args):
        self.master.removeFromList(self.image)
        self.master.openImage(None)
        self.destroy()

    def show_image(self):
        try:
            self.img  = Image.open(self.image.imgPath)

            self.imgRachio = self.img.width/self.img.height

            self.imgp :ImageTk.PhotoImage = ImageTk.PhotoImage(self.img)
            color = 0 if self.master.jsonController.darkMood == False else 1
            self.canvas = ctk.CTkCanvas(self , background = appColors.color5[color] ,highlightthickness=0 , bd=0 , relief= "ridge")
            self.canvas.grid(row=1 , column=0 , sticky="nwes"  )
            self.canvas.create_image(0,0 , image = self.imgp , anchor = "nw"  )
            self.canvas.bind("<Configure>" , self.bg_resizer)

        except FileNotFoundError:
            print(f"Image not found: {self.image.imgPath}")
        except Exception as e:
            print(f"Unexpected error in show_image: {e}")

    def bg_resizer(self, event):
        """Resize and update the image when the canvas is resized."""
        # print(event.width , event.height)
        self.canvasRachio = event.width / event.height

        if self.canvasRachio > self.imgRachio : #canvas is wider than the image
            height = int(event.height)
            width = int(height * self.imgRachio)
        else:                       #canvas is narrower than the image
            width = int(event.width)
            height = int(width / self.imgRachio)
            

        img = self.img.resize(size=(width ,height))
        self.imgp  = ImageTk.PhotoImage(img)
        self.canvas.create_image(int( event.width/2 ),int(event.height /2)  , image = self.imgp , anchor = "center"  )

    
    def _set_appearance_mode(self, mode_string):
        # color = 0 
        if mode_string == "Light" : 

            color =0
        else: 
            color =1     

        self.canvas.config(background= appColors.color5[color])
        return super()._set_appearance_mode(mode_string)