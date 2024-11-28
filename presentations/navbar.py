from customtkinter import *

#configs
from configs.app_colors import AppColors , appColors
#controller
from controllers.windows_controller import WindowsController , windowsController

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

