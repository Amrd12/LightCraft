#configs
from configs.app_colors import AppColors , appColors
from configs.app_strings import appStrings
#widgets
from presentations.navbar import NavBarWidget
from presentations.main_frame import MainFramWidget

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.appColor.mood(isDarkMood=self.jsonController.data[appStrings.isDarkMood])
        self.TkdndVersion = TkinterDnD._require(self)
        self.config(background = self.appColor.color5)

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
        navbar = NavBarWidget(self )

        navbar.grid(row = 0 ,column = 0 ,sticky = "nsw" , pady=15 ,padx=[15,10])

        navbar2 = MainFramWidget(self  )

        navbar2.grid(row = 0 ,column = 1 ,sticky = "nswe" , pady=15 ,padx=[10,15])

    def get_path(self, event):
        """Handles file drop events."""
        file_path : str =  event.data 
        if file_path.startswith("{"):
            file_path =file_path[1:-1]

        if os.path.isfile(file_path):
            # self.label.configure(text=f"Processing: {file_path}")
            # Example integration with your ImgModel and JsonController
            try:
                # Uncomment these lines if you have these modules available
                img = ImgModel(file_path, os.path.basename(file_path))
                self.jsonController.saveImg(imgModel=img)
                # self.label.configure(text=f"File processed and saved: {file_path}")

            except Exception as e:
                print(file_path , "not file\n" ,e)
                # self.label.configure(text=f"Error: {e}")
                pass
        else:
            pass
            # self.label.configure(text="Invalid file. Please drop a valid file.")

if __name__ == "__main__":

    app = MainApp()
    app.mainloop()
    print("kareem")