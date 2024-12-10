#configs
from configs.app_colors import AppColors , appColors
from configs.app_strings import appStrings

#widgets
from presentations.navbar import NavBarWidget
from presentations.main_frame import MainFramWidget
from presentations.widgets.editing_screen import EditingScreen 

#Controllers
from controllers.json_controller import JsonController

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
        self.geometry("1024x768")
        # ctk.set_appearance_mode("dark")
        # ctk.set_default_color_theme("blue")

        # Register the app window itself as a drag-and-drop target
        self.drop_target_register(DND_ALL)
        self.dnd_bind("<<Drop>>", self.get_path)

        # Add a label to display instructions or messages
        # self.label = ctk.CTkLabel(self, text="Drag and drop a file anywhere in this window!", font=("Arial", 16))
        # self.label.pack(pady=20)

        self.grid()
        self.columnconfigure(0)
        self.columnconfigure(1,weight=1)
        self.rowconfigure(0 ,weight=1)

        # create the nav bar 
        self.navbar = NavBarWidget(master=self ,opendItems=self.opendItems , openImage=self.openImage , mood= self.mood )#call ChangeMainFrame from here

        self.navbar.grid(row = 0 ,column = 0 ,sticky = "nsw" , pady=15 ,padx=[15,10])

        self.mainFramWidget = MainFramWidget(master = self , imagesList= self.jsonController.imgsList)
        self.mainFramWidget.grid(row = 0 ,column = 1 ,sticky = "nswe" , pady=15 ,padx=[10,15])

    def openImage(self, img: ImgModel):
        if img is None:
            # Restore the main frame and remove any EditingScreen
            for widget in self.grid_slaves(row=0, column=1):
                if isinstance(widget, EditingScreen):
                    widget.grid_forget()
            self.mainFramWidget.grid(row=0, column=1, sticky="nswe", pady=15, padx=[10, 15])
        else:
            # Check if an EditingScreen for this image already exists
            for widget in self.grid_slaves(row=0, column=1):
                if isinstance(widget, EditingScreen) and widget.image == img:
                    widget.grid(row=0, column=1, sticky="nswe", pady=15, padx=[10, 15])
                    return

            # Hide the main frame and create a new EditingScreen
            self.mainFramWidget.grid_forget()
            self.addToList(img=img)
            editing_screen = EditingScreen(master = self, image=img)
            editing_screen.grid(row=0, column=1, sticky="nswe", pady=15, padx=[10, 15])


    def addToList(self,img :ImgModel):
        """
        Add A Tab To the nav bar 
        """
        self.navbar.opendItems.append(img)
        
        self.navbar.refresh()

    def removeFromList(self, img:ImgModel):
        """
        remove Tab from the nav bar 
        """
        self.opendItems.remove(img)
        self.navbar.refresh()

    def get_path(self, event  ):
        file_path: str = event if type(event) == str else event.data
        if file_path.startswith("{"):
            file_path = file_path[1:-1]

        if os.path.isfile(file_path):
            try:
                # Create an ImgModel and save it
                img = ImgModel(file_path, os.path.basename(file_path))
                self.jsonController.saveImg(imgModel=img)
                
                # Add the image to the navbar list
                self.openImage(img)
                # self.mainFramWidget.imagesList.append(img)
                # self.mainFramWidget.refresh()
                # Open the image for editing
                # self.openImage(img)
            except Exception as e:  
                print(f"Error processing file {file_path}: {e}")
        else:
            print("Invalid file. Please drop a valid file.")

    def mood(self):
        """
        Toggles the app's mood (dark/light mode) and updates the UI accordingly.

        :param is_dark: Boolean indicating whether the dark mode is active.
        """
        isdark = self.jsonController.darkMood

        self.jsonController.darkMood = not isdark

        ctk.set_appearance_mode(mode_string="dark" if not isdark else "light")
    
            


if __name__ == "__main__":

    app = MainApp()
    app.mainloop()
    print("karem")