

from typing import List
from datetime import datetime
from enum import Enum

class Flag(Enum):
  INFO = 'INFO'
  IMPORTANT = 'IMPORTANT'
  DUE_SOON = 'DUE_SOON'

class Activity:
    
    def __init__(self) -> None:
        self.id:str = None
        self.text:str = None
        self.directed:bool = False
        self.recipients:List[str] = []
        self.post_time:datetime = None
        self.due_time:datetime = None
        self.flag:Flag = None
        self.lat:float = None
        self.lon:float = None
        
    def to_json(self) -> any:
        jobj = {}
        jobj['id'] = self.id
        jobj['text'] = self.text
        jobj['directed'] = self.directed
        jobj['recipients'] = self.recipients
        jobj['post_time'] = self.post_time.isoformat()
        jobj['due_time'] = self.due_time.isoformat()
        jobj['flag'] = self.flag.value
        jobj['lat'] = self.lat
        jobj['lon'] = self.lon
        return jobj
        
    @classmethod
    def from_params(cls, text:str, directed:bool, recipients:List[str], post_time:datetime, due_time:datetime, flag:Flag, lat:float, lon:float, id:str=None):
        obj = cls()
        obj.text = text
        obj.directed = directed
        obj.recipients = recipients
        obj.post_time = post_time
        obj.due_time = due_time
        obj.flag = flag
        obj.lat = lat
        obj.lon = lon
        obj.id = id
        return obj
    