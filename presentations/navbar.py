import customtkinter as ctk

# configs
from configs.app_colors import AppColors, appColors
from configs.app_strings import appStrings
# model
from models.img_model import ImgModel
from PIL import Image , ImageDraw
from typing import Callable


class NavBarWidget(ctk.CTkFrame):
    appColor: AppColors = appColors

    def __init__(self, opendItems: list[ImgModel], openImage: Callable[[ImgModel], None], mood: Callable[[],None], *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            fg_color=self.appColor.color4,
            # bg_color=self.appColor.color5,
            corner_radius=10,
            width=60
        )

        self.opendItems: list[ImgModel] = opendItems
        self.openImage = openImage

        self.rowconfigure(0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2)

        # Main Screen Button
        imgLib = Image.open(appStrings.LibImgPath)
        imgLibp = ctk.CTkImage(imgLib, imgLib)
        self.libbutton = ctk.CTkButton(
            self,
            command=lambda: self.openImage(None),
            width=30,
            height=30,
            corner_radius=30,
            hover_color=self.appColor.color3,
            image=imgLibp,
            fg_color=self.appColor.color3,
            text=""
        )
        self.libbutton.grid(row=0, column=0, pady=10, padx=10, ipady=3, ipadx=3)

        # Opened Images List Buttons
        self.opendItemsList = ctk.CTkFrame(
            self,
            width=50,
            corner_radius=30,
            fg_color="transparent"
        )
        self.opendItemsList.grid(row=1, column=0 , sticky = "NS", pady=10, padx=10, ipady=3, ipadx=3)  # Fixed typo here
        self.createOpendItemsList()

        lightMood = Image.open(appStrings.lightMoodImgPath)
        darkMood =  Image.open(appStrings.darkMoodImgPath)
        imgMoodp = ctk.CTkImage(light_image=lightMood , dark_image=darkMood)

        # App Mood Button
        self.mood = ctk.CTkButton(
            self,
            width=30,
            height=30,
            command=lambda: mood(),
            hover_color=self.appColor.color3,
            fg_color=self.appColor.color3,
            text="",
            image = imgMoodp

        )
        self.mood.grid(row=2, column=0, pady=10, padx=10, ipady=3, ipadx=3)

    def createOpendItemsList(self):
        for btn in self.opendItems:
            img = Image.open(btn.imgPath)
            imgp = ctk.CTkImage(img, img)
            btncon = ctk.CTkButton(
                self.opendItemsList,
                command=lambda btn=btn: self.openImage(btn),
                width=30,
                height=30,
                corner_radius=30,
                hover_color=self.appColor.color3,
                image=imgp,
                fg_color=self.appColor.color3,
                text="",
               
            )
            btncon.pack( pady = 5)
            
    
    def refresh(self):
        # Clear existing tabs
        for widget in self.opendItemsList.winfo_children():
            widget.destroy()

        # Recreate the navbar with updated items
        self.createOpendItemsList()
