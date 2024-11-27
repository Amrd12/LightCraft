import json
from os import path

from configs.app_strings import appStrings
from models.img_model import ImgModel


class JsonController:
    data: json

    imgsList: list[ImgModel]

    def __init__(self):
        self.file_path = path.join(path.dirname(__file__), appStrings.jsonfile)
        self.check()
        with open(self.file_path, "r") as file:
            self.data = json.loads(file.read())
        self.imgsList =[ ImgModel.from_json(i) for i in self.data["imgspath"] ]
        print(self.imgsList)

    def check(self):
        if not path.exists(self.file_path):
            self.data = {
            "firstTime" : True,
            "darkmood" : True,
            "imgspath" : []
                    }
            self.save()

    def saveImg(self , imgModel:ImgModel):
        for i in self.imgsList:
            if(i == imgModel):
                return
        self.imgsList.append(imgModel)
        self.data["imgspath"] : list = [e.to_json() for e in self.imgsList]
        self.save()
    
    def save(self):
         with open(self.file_path, "w") as file:
                file.write(json.dumps(self.data,indent=2))

