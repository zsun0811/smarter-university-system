
from typing import List
from datetime import datetime

from app.model.reaction import Reaction


class DiscussionReaction:
    
    def __init__(self) -> None:
        self.id:str = None
        self.reaction:Reaction = None
        self.user_id:str = None
        self.timestamp:datetime = None
            
    def to_json(self) -> any:
        jobj = {}
        jobj['reaction'] = self.reaction.value
        jobj['user_id'] = self.user_id
        jobj['timestamp'] = self.timestamp.isoformat()
        jobj['id'] = self.id
        return jobj
        
    @classmethod
    def from_params(cls, reaction:Reaction, user_id:str, timestamp:datetime=None, id:str=None):
        obj = cls()
        obj.reaction = reaction
        obj.user_id = user_id
        obj.timestamp = timestamp
        obj.id = id
        return obj
    
class DiscussionResponse:
    
    def __init__(self) -> None:
        self.id:str = None
        self.text:str = None
        self.author_id:str = None
        self.timestamp:datetime = None
        self.reactions:List[DiscussionReaction] = [] 
        
    def add_reaction(self, reaction:DiscussionReaction):
        self.reactions.append(reaction)
        
    def to_json(self) -> any:
        jobj = {}
        jobj['text'] = self.text
        jobj['author_id'] = self.author_id
        jobj['timestamp'] = self.timestamp.isoformat()
        jobj['id'] = self.id
        jobj['reactions'] = [r.to_json() for r in self.reactions]
        return jobj
        
    @classmethod
    def from_params(cls, text:str, author_id:str, timestamp:datetime=None, id:str=None):
        obj = cls()
        obj.text = text
        obj.author_id = author_id
        obj.timestamp = timestamp
        obj.id = id
        return obj
    

    
    
class DiscussionThread:
    
    def __init__(self) -> None:
        self.id:str = None
        self.title:str = None
        self.text:str = None
        self.author_id:str = None
        self.timestamp:datetime = None
        self.responses:List[DiscussionResponse] = []
        
    def add_response(self, response:DiscussionResponse):
        self.responses.append(response)
            
    def to_json(self) -> any:
        jobj = {}
        jobj['title'] = self.title
        jobj['text'] = self.text
        jobj['author_id'] = self.author_id
        jobj['timestamp'] = self.timestamp.isoformat()
        jobj['id'] = self.id
        jobj['responses'] = [r.to_json() for r in self.responses]
        return jobj
    
    @classmethod
    def from_params(cls, title:str, text:str, author_id:str, timestamp:datetime=None, id:str=None):
        obj = cls()
        obj.title = title
        obj.text = text
        obj.author_id = author_id
        obj.timestamp = timestamp
        obj.id = id
        return obj