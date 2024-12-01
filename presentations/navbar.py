from customtkinter import *

#configs
from configs.app_colors import AppColors , appColors
#controller
from controllers.windows_controller import WindowsController , windowsController

from PIL import Image 

class NavBarWidget(CTkFrame):

    windowsController : WindowsController = windowsController
    
    appColor : AppColors  = appColors

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            fg_color=self.appColor.color4,
            bg_color=self.appColor.color5,
            corner_radius=10,
            width=60
        )
        print()
        img= Image.open(r"presentations/icons/lib.png")
        imgp = CTkImage(img , img)
        libbutton = CTkButton(self , width=30 , height=30 ,corner_radius=30 , hover_color= appColors.color3, image=imgp ,fg_color=appColors.color3 ,text="")
        libbutton.pack(pady = 10 , padx=10 , ipady=3 , ipadx=3)
        
    

