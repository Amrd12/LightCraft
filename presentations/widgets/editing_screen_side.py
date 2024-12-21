import customtkinter as ctk
from configs.app_colors import AppColors, appColors
from configs.app_strings import appStrings
from models.img_model import ImgModel
from presentations.widgets.cutom_slider_field import CustomSliderField
from PIL import ImageEnhance , Image

class EditingScreenSide(ctk.CTkFrame):
    appColor: AppColors = appColors

    def __init__(self, master, *args, **kwargs):
        super().__init__(
            master=master,
            *args,
            **kwargs,
            fg_color=self.appColor.color4,
            corner_radius=10,
            width=200
        )

        self.columnconfigure(0, weight=1)
        self.create_sliders()

    def create_sliders(self):
        """Create a list of CustomSliderField widgets for editing purposes."""
        sliders_data = [
            {"text": "Brightness", "range": {0, 100}, "method": self.adjust_brightness},
            {"text": "Contrast", "range": {0, 100}, "method": self.adjust_contrast},
            {"text": "Saturation", "range": {0, 100}, "method": self.adjust_saturation},
            {"text": "Hue", "range": {-50, 50}, "method": self.adjust_hue}
        ]

        self.sliders = []
        for i, slider_data in enumerate(sliders_data):
            slider = CustomSliderField(
                master=self,
                text=slider_data["text"],
                range=slider_data["range"],
                method=slider_data["method"]
            )
            slider.pack( pady=10, padx=10, ) #row=i, column=0,sticky="n"
            self.sliders.append(slider)

        savebtn = ctk.CTkButton(self , 
                                text= "save" ,
                                
                                 command= lambda: self.master.save() )
        savebtn.pack(pady=10, padx=10,side = "bottom")

    def adjust_brightness(self, value: float):
        enhancer = ImageEnhance.Brightness(self.master.original_img)
        modified_img = enhancer.enhance(value / 50)  # Normalize to 1.0 scale
        self.master.update_canvas_image(modified_img)

    def adjust_contrast(self, value: float):
        enhancer = ImageEnhance.Contrast(self.master.original_img)
        modified_img = enhancer.enhance(value / 50)  # Normalize to 1.0 scale
        self.master.update_canvas_image(modified_img)

    def adjust_saturation(self, value: float):
        enhancer = ImageEnhance.Color(self.master.original_img)
        modified_img = enhancer.enhance(value / 50)  # Normalize to 1.0 scale
        self.master.update_canvas_image(modified_img)

    def adjust_hue(self, value: float):
        hsv_img = self.master.original_img.convert("HSV")
        h, s, v = hsv_img.split()
        h = h.point(lambda p: (p + value) % 256)  # Adjust hue
        modified_img = Image.merge("HSV", (h, s, v)).convert("RGB")
        self.master.update_canvas_image(modified_img)
