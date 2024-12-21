import customtkinter as ctk
from configs.app_colors import appColors ,AppColors

class CustomSliderField(ctk.CTkFrame):
    appColor: AppColors = appColors
    def __init__(self, master, text, range, method, *args, **kwargs):
        super().__init__(
            master=master,
            *args,
            **kwargs,
            fg_color="transparent"
        )

        self.method = method
        self.range = range
        self.current_value = (min(range) +max(range))/2 # Default value is the midpoint of the range

        self.columnconfigure(1, weight=1)
        
        # Label above the slider for the text
        self.text_label = ctk.CTkLabel(self, text=text, font=("Arial", 12, "bold"))
        self.text_label.grid(row=0, column=0, columnspan=3, pady=(0, 5), sticky="n")

        # Min value label
        self.min_label = ctk.CTkLabel(self, text=f"{min(range)}", font=("Arial", 10))
        self.min_label.grid(row=1, column=0, padx=(5, 0), sticky="w")

        # Slider
        self.slider = ctk.CTkSlider(
            self,
            from_=min(range),
            to=max(range),
            number_of_steps=100,
            command=self.on_value_change,
            button_color=self.appColor.color3,
            hover=False,
            fg_color= self.appColor.color5[0],
            progress_color=self.appColor.color5[1]#[self.appColor.color5[1] , self.appColor.color5[0]]
        )
        self.slider.set(self.current_value)  # Set slider to the default value
        self.slider.grid(row=1, column=1, padx=5, sticky="ew")

        # Max value label
        self.max_label = ctk.CTkLabel(self, text=f"{max(range)}", font=("Arial", 10))
        self.max_label.grid(row=1, column=2, padx=(0, 5), sticky="e")

        # Current value label below the slider
        self.value_label = ctk.CTkLabel(self, text=f"{self.current_value:.2f}", font=("Arial", 10))
        self.value_label.grid(row=2, column=0, columnspan=3, pady=(5, 0), sticky="n")

    def on_value_change(self, value):
        """Handle slider value changes."""
        self.current_value = float(value)
        self.value_label.configure(text=f"{self.current_value:.2f}")  # Update current value label
        self.method(self.current_value)  # Call the provided method with the current value
