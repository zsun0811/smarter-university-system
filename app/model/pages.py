

from datetime import datetime

class Page:
    
    def __init__(self) -> None:
        self.id:str = None
        self.title:str = None
        self.text:str = None
        self.created:datetime = None
        self.updated:datetime = None
            
    def to_json(self) -> any:
        jobj = {}
        jobj['title'] = self.title
        jobj['text'] = self.text
        jobj['created'] = self.created.isoformat()
        jobj['updated'] = self.updated.isoformat()
        jobj['id'] = self.id
        return jobj
        
    @classmethod
    def from_params(cls, title:str, text:str, created:datetime=None, updated:datetime=None, id:str=None):
        obj = cls()
        obj.title = title
        obj.text = text
        obj.created = created
        obj.updated = updated
        obj.id = id
        return obj
    