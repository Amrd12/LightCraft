#model
from models.img_model import ImgModel

#controlles
from controllers.json_controller import JsonController

#views
from presentations.navbar import NavBarWidget
from presentations.main_frame import MainFramWidget
from presentations.widgets.img_widget import ImageWidget
from presentations.widgets.editing_screen import EditingScreen

import main.MainApp as MainApp

class PageController:
        
    openedPages: list[ImgModel] #  images Opened In the Nave bar

    Images :  list[ImgModel] # images in the recent tab

    def __init__(self, mainApp :MainApp,  navbar:NavBarWidget , mainFrameWidget : MainFramWidget ):


        self.mainApp: main.MainApp =mainApp
        self.navbar:NavBarWidget  = navbar
        self. mainFrameWidget : MainFramWidget = mainFrameWidget


    def openImage(self, img: ImgModel):
        if img is None:
            # Restore the main frame and remove any EditingScreen
            for widget in self.grid_slaves(row=0, column=1):
                if isinstance(widget, EditingScreen):
                    widget.grid_forget()
            
            self.mainFramWidget.refresh()
            self.mainFramWidget.grid(row=0, column=1, sticky="nswe", pady=15, padx=[10, 15])
        else:
            self.mainFramWidget.grid_forget()
            self.addToList(img=img)
            editing_screen = EditingScreen(master = self, image=img)
            editing_screen.grid(row=0, column=1, sticky="nswe", pady=15, padx=[10, 15])


    def addToList(self,img :ImgModel):
        """
        Add A Tab To the nav bar 
        """
        for imgs in self.opendItems:
                if img.imgPath == imgs.imgPath : return
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
                self.mainFramWidget.imagesList.append(img)
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
    
