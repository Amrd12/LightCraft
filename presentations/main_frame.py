import customtkinter as ctk
#configs
from configs.app_colors import AppColors , appColors
from configs.app_strings import appStrings
#model
from models.img_model import ImgModel
#widgets
from presentations.widgets.img_widget import ImageWidget
from PIL import Image

class MainFramWidget(ctk.CTkFrame):

    appColor : AppColors  = appColors
    imagesList : list[ImgModel]

    num_columns: int = 4

    def __init__(self  ,imagesList : list[ImgModel]  , *args, **kwargs):
        
        super().__init__(
            *args,
            **kwargs,
            fg_color=self.appColor.color4,
            bg_color=self.appColor.color5,
            corner_radius=10,
        )
        self.text = ctk.CTkFont ( family="poppins" ,size= 30 , weight="bold",  )
        self.imagesList = imagesList

        # Create the welcome label
        lbWelcome = ctk.CTkLabel(self , text= "Welcome To Light Craft" ,font=self.text , pady = 10)

        lbWelcome.grid(row=0, column=0, sticky="we", padx=10, pady=10)

        # Create the recent label
        lbrec = ctk.CTkLabel(self , text= "Recent",font=self.text  , pady = 10 )

        lbrec.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        # Create the container for images and make it expand to take remaining space
        self.imagesContainer = ctk.CTkScrollableFrame(self, fg_color=self.appColor.color5
        ,scrollbar_button_color	= self.appColor.color4,
        scrollbar_button_hover_color =  self.appColor.color4,
            bg_color=self.appColor.color5,corner_radius=10)
        
        # Use grid to take remaining space
        self.imagesContainer.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
        self.imagesContainer.bind("<Configure>", self.on_resize)

        # Configure the grid to make row 2 take up the remaining space
        self.grid_rowconfigure(2, weight=1)
        
        self.grid_columnconfigure(0, weight=1)
        self.createIMgsWidget()

    def on_resize(self, event):
    # Refresh the layout when the container is resized
        self.refresh()

    def refresh(self):
        # Clear existing tabs
        for widget in self.imagesContainer.winfo_children():
            widget.destroy()

        # Recreate the navbar with updated items
        self.createIMgsWidget()

    def selectfile(self):
            filename = ctk.filedialog.askopenfilename()
            self.master.get_path(filename)
            print(filename)

    def createIMgsWidget(self):
        container_width = self.master.winfo_width()
        self.imagesList = self.master.jsonController.imgsList
        if len(self.imagesList) == 0:
            for i  in self.imagesContainer.grid_slaves():
                i.grid_forget()
            self.imagesContainer.rowconfigure(0 ,weight=1)
            self.imagesContainer.columnconfigure(0 ,weight=1)

            img = Image.open(appStrings.dadImage)
            imgp= ctk.CTkImage(img,img, size=(200,200))
            self.emptybtn = ctk.CTkButton(self.imagesContainer,fg_color="transparent", image= imgp
           , hover=False,command= lambda: self.selectfile(),
           text="Drag and Drop\nImage Here" ,font=self.text
            ,text_color=(AppColors.color2[0] , AppColors.color2[0])
              ) 

            self.emptybtn.grid(sticky="NSEW" , row=0 , column=0)
            return
        
        for i  in self.imagesContainer.grid_slaves():
            i.grid_forget()
        # Get the width of the imagesContainer

        # Define the width of each image widget (you can adjust this as needed)
        image_width = 200

        # Calculate the number of columns based on the container width
        num_columns = 3#max(container_width // image_width, 3)  # Ensure at least 4 columns
        if self.num_columns == num_columns : return
        row = 0
        print("Number of items per row", num_columns)

        # Clear existing image widgets
        for widget in self.imagesContainer.winfo_children():
            widget.destroy()

        # Create new image widgets based on the updated layout
        row = 0  # Start at the first row
        for index, img in enumerate(self.imagesList):
            newimg = ImageWidget(master=self.imagesContainer, image=img)

            # Calculate the row and column positions
            col = index % num_columns   # Column is determined by the index modulo the number of columns
            if col == 0 and index != 0:  # Increment row when a new row starts (after every num_columns images)
                row += 1
            print( row,col)
            newimg.grid(row=row, column=col, padx=5, pady=5)

