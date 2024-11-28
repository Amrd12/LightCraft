from dataclasses import dataclass
import json

@dataclass
class ImgModel:
    
    imgPath:str
    imgName:str

    def __str__(self):
        return json.dumps({"imgName" : self.imgName , "imgPath" : self.imgPath} , indent=2)
    
    def to_json(self):
        return json.loads(str(self) )
    
    @classmethod
    def from_json(cls, json_data):
        if isinstance(json_data, str):
            data = json.loads(json_data)
        else:
            data = json_data
        return cls(**data)