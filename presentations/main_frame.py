import customtkinter as ctk
#configs
from configs.app_colors import AppColors , appColors
from configs.app_strings import appStrings
#model
from models.img_model import ImgModel
#controller
from controllers.windows_controller import WindowsController , windowsController


class MainFramWidget(ctk.CTkFrame):

    appColor : AppColors  = appColors

    windowsController : WindowsController = windowsController

    def __init__(self , *args, **kwargs):

        super().__init__(
            *args,
            **kwargs,
            fg_color=self.appColor.color4,
            bg_color=self.appColor.color5,
            corner_radius=10,
        )
    