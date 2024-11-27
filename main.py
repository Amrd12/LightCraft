from controllers.json_controller import JsonController
from models.img_model import ImgModel

if __name__ == "__main__":
    jsoncon = JsonController()
    Img = ImgModel("feaf" , "amr")
    jsoncon.saveImg(imgModel=Img)