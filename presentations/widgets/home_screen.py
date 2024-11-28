import customtkinter as ctk
from controllers.json_controller import JsonController , jsonController
from models.img_model import ImgModel

class HomeScreen(ctk.CTkFrame):
    imgList : list[ImgModel] = jsonController.imgsList

    def pack(self, **kwargs):
        jsonController.updateList()
        self.imgList = jsonController.imgsList
        return super().pack(**kwargs)
    