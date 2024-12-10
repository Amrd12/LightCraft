import os
from models.img_model import ImgModel
import customtkinter as ctk
from PIL import Image
from configs.app_colors import appColors, AppColors

class ImageWidget(ctk.CTkFrame):
    appColor: AppColors = appColors
    image: ImgModel

    def __init__(self, image: ImgModel, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            fg_color=self.appColor.color4,
            bg_color=self.appColor.color5,
            corner_radius=10,
            width=200,
            height=150
        )
        self.text = ctk.CTkFont(family="Poppins", size=12, weight="bold")

        self.image = image
        self.bind("<Button-1>", self.click)

        # Delay image loading until the widget is rendered
        self.after(100, self._load_image)


    def _load_image(self):
        # Load and resize the image
        img = Image.open(self.image.imgPath)
        imgp = ctk.CTkImage(img, img, size=(self.winfo_width(), self.winfo_height()))

        # Add image to the label
        bg_lbl = ctk.CTkLabel(self, text="", image=imgp)
        bg_lbl.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.image_label = bg_lbl
        bg_lbl.bind("<Button-1>", self.click)

        # Delay info loading to ensure width is correctly initialized
        self.after(100, self._load_info)

    def _load_info(self):
        # Create info frame at the bottom
        frame = ctk.CTkFrame(self, height=50, fg_color="transparent" , bg_color="transparent")
        frame.place(relx=0, rely=1.0, anchor="sw", relwidth=1)
        frame.bind("<Button-1>", self.openbtnfun)

        # Add image name label
        lb = ctk.CTkLabel(frame, text=self.image.imgName, font=self.text, text_color=AppColors.color0)
        lb.pack(side="left", padx=10)

        # Add open button
        btn = ctk.CTkButton(frame, text="Open", command=self.openbtnfun, width=50 , font=self.text,
                            hover= False , fg_color= "transparent" , text_color=AppColors.color0)
        btn.pack(side="right", padx=10)
        frame.lift(self.image_label)


    def openbtnfun(self ,*args ):
        # Open the directory containing the image
        path = os.path.dirname(self.image.imgPath)
        os.startfile(path)


    def click(self, event):
        # Handle click event
        # self.master.master.master.addToList(self.image)
        self.master.master.master.openImage(self.image)

