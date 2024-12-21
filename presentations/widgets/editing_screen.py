import customtkinter as ctk
from configs.app_colors import AppColors, appColors
from configs.app_strings import appStrings
from models.img_model import ImgModel
from PIL import Image, ImageTk
from tkinter import Canvas
from presentations.widgets.editing_screen_side import EditingScreenSide


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
        self.original_img = None  # Store the original unmodified image
        self.modified_img = None  # Store the modified image

        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.show_image()
        self.create_label()

    def create_label(self):
        closeLight = Image.open(appStrings.closeLight)
        closeDark = Image.open(appStrings.closeDark)
        close_img_resized = ctk.CTkImage(closeDark, closeLight, size=(25, 25))
        label = ctk.CTkLabel(self, image=close_img_resized, corner_radius=10, text=self.image.imgName, anchor="w", compound="right")
        label.bind("<Button-1>", self.close)
        self.after(200, self._load_image)


        label.grid(row=0, column=0, sticky="NSEW")

        side = EditingScreenSide(self)
        side.grid(row=1, column=1, sticky="NSEW")
    def _load_image(self):
        self.bind("<Control-s>" ,self.save)
        for i in self.slaves():
            i.bind("<Control-s>" ,self.save)

    def close(self, *args):
        self.master.removeFromList(self.image)
        self.master.openImage(None)
        self.destroy()

    def show_image(self):
        try:
            self.original_img = Image.open(self.image.imgPath)  # Load the original image
            self.modified_img = self.original_img.copy()  # Create a copy for modification

            self.imgRachio = self.original_img.width / self.original_img.height

            self.imgp: ImageTk.PhotoImage = ImageTk.PhotoImage(self.modified_img)
            color = 0 if not self.master.jsonController.darkMood else 1
            self.canvas = ctk.CTkCanvas(self, background=appColors.color5[color], highlightthickness=0, bd=0, relief="ridge")
            self.canvas.grid(row=1, column=0, sticky="nwes")
            self.canvas.create_image(0, 0, image=self.imgp, anchor="nw")
            self.canvas.bind("<Configure>", self.bg_resizer)
            
        except FileNotFoundError:
            print(f"Image not found: {self.image.imgPath}")
        except Exception as e:
            print(f"Unexpected error in show_image: {e}")

    def bg_resizer(self, event=None):
        """Resize and update the image when the canvas is resized."""
        if not self.modified_img:
            return

        self.canvasRachio = self.canvas.winfo_width() / self.canvas.winfo_height()

        if self.canvasRachio > self.imgRachio:  # Canvas is wider than the image
            height = int(self.canvas.winfo_height())
            width = int(height * self.imgRachio)
        else:  # Canvas is narrower than the image
            width = int(self.canvas.winfo_width())
            height = int(width / self.imgRachio)

        resized_img = self.modified_img.resize(size=(width, height))
        self.imgp = ImageTk.PhotoImage(resized_img)
        self.canvas.create_image(
            int(self.canvas.winfo_width() / 2),
            int(self.canvas.winfo_height() / 2),
            image=self.imgp,
            anchor="center"
        )

    def update_canvas_image(self, modified_img):
        """Update the canvas image with the modified version and call the resizer."""
        self.modified_img = modified_img
        self.bg_resizer()
        
    def save(self , event = None):
        self.original_img = self.modified_img

    def _set_appearance_mode(self, mode_string):
        # color = 0 
        if mode_string == "Light" : 

            color =0
        else: 
            color =1     

        self.canvas.config(background= appColors.color5[color])
        return super()._set_appearance_mode(mode_string)