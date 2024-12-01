import json
from os import path

from configs.app_strings import appStrings
from models.img_model import ImgModel


class JsonController:
    data: json

    imgsList: list[ImgModel] =  []
    
    def __init__(self):
        self.file_path = path.join(path.dirname(__file__), appStrings.jsonfile)
        self.check()
        self.updateList()
        self.save()
        print(self.imgsList)

    def updateList(self):
        with open(self.file_path, "r") as file:
            self.data = json.loads(file.read())
        self.imgsList =[ImgModel.from_json(i) for i in self.data[appStrings.imgPath] if path.exists(i[appStrings.imgPath])]

    def check(self):
        if not path.exists(self.file_path):
            self.data = {
            appStrings.isfirstTime : True,
            appStrings.isDarkMood : True,
            appStrings.imgPath : []
                    }
            self.save()

    def saveImg(self , imgModel:ImgModel):
        for i in self.imgsList:
            if(i == imgModel):
                return
        self.imgsList.append(imgModel)
        self.save()
    
    def save(self):
        if len(self.imgsList) ==0:
             self.data[appStrings.imgPath]  = [e.to_json() for e in self.imgsList]
        with open(self.file_path, "w") as file:
                file.write(json.dumps(self.data,indent=2))

    def darkMood(self , isdarkMood:bool):
        if( self.data["darkmood"] == isdarkMood):
            return
        self.data["darkmood"] = isdarkMood
        self.save()

    def firstTime(self , firstTime:bool):
        if( self.data["firstTime"] == firstTime):
            return
        self.data["firstTime"] = firstTime
        self.save()

jsonController :JsonController = JsonController()