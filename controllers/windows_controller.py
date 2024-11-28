from models.img_model import ImgModel
# from presentations.widgets.editing_screen  import EditingScreen

class WindowsController:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
           cls._instance = super(WindowsController, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    imgList : list[ImgModel]
    ActiveWindow : int
    

windowsController : WindowsController = WindowsController()

