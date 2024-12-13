#configs
from configs.app_colors import AppColors , appColors
from configs.app_strings import appStrings

#widgets
from presentations.navbar import NavBarWidget

from presentations.main_frame import MainFramWidget

from presentations.widgets.editing_screen import EditingScreen 

#Controllers
from controllers.json_controller import JsonController

from controllers.page_controller import PageController

#models
from models.img_model import ImgModel

#imports
import os
import customtkinter as ctk
from tkinterdnd2 import TkinterDnD, DND_ALL


class MainApp(ctk.CTk, TkinterDnD.DnDWrapper):
    jsonController : JsonController = JsonController()

    
    appColor : AppColors  = appColors

    opendItems : list[ImgModel] =[]

    mainFramWidget : MainFramWidget

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs ,fg_color = self.appColor.color5)
        ctk.set_appearance_mode(  "dark" if self.jsonController.darkMood == True else "light")
        self.TkdndVersion = TkinterDnD._require(self)


        # Set up the main window
        self.title("Light Craft")
        self.geometry("1096x616")

        # Register the app window itself as a drag-and-drop target
        self.drop_target_register(DND_ALL)
        self.dnd_bind("<<Drop>>", self.get_path)
        self.grid()
        self.columnconfigure(0)
        self.columnconfigure(1,weight=1)
        self.rowconfigure(0 ,weight=1)

        # create the nav bar 
        self.navbar = NavBarWidget(master=self ,opendItems=self.opendItems , openImage=self.openImage , mood= self.mood )#call ChangeMainFrame from here

        self.navbar.grid(row = 0 ,column = 0 ,sticky = "nsw" , pady=15 ,padx=[15,10])

        self.mainFramWidget = MainFramWidget(master = self , imagesList= self.jsonController.imgsList)
        self.mainFramWidget.grid(row = 0 ,column = 1 ,sticky = "nswe" , pady=15 ,padx=[10,15])
        self.pageController: PageController = PageController(mainApp=self , navbar=self.navbar , mainFrameWidget=self.mainFramWidget)



if __name__ == "__main__":
    app = MainApp()

    app.mainloop()