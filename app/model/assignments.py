


from typing import List
from datetime import datetime

from app.model.reaction import Reaction


class AnswerOption:
    
    def __init__(self) -> None:
        self.id:str = None
        self.text:str = None
        self.is_correct = False
            
    def to_json(self) -> any:
        return self.__dict__
        
    @classmethod
    def from_params(cls, text:str, is_correct:bool=False, id:str=None):
        obj = cls()
        obj.text = text
        obj.is_correct = is_correct
        obj.id = id
        return obj
    
    
class QuizSection:
    
    def __init__(self) -> None:
        self.id:str = None
        self.title:str = None
        self.text:str = None
        self.last_updated:datetime = None
        
    def to_json(self) -> any:
        jobj = {}
        jobj['title'] = self.title
        jobj['text'] = self.text
        jobj['last_updated'] = self.last_updated.isoformat()
        jobj['id'] = self.id
        return jobj
        
    @classmethod
    def from_params(cls, title:str, text:str, last_updated:datetime=None, id:str=None):
        obj = cls()
        obj.title = title
        obj.text = text
        obj.last_updated = last_updated
        obj.id = id
        return obj
    
class Question(QuizSection):
    
    def __init__(self) -> None:
        super().__init__()
        self.answers:List[AnswerOption] = []

    def add_answer_option(self, answer_option:AnswerOption):
        self.answers.append(answer_option)
        
    def to_json(self) -> any:
        jobj = super().to_json()
        jobj['answers'] = [a.to_json() for a in self.answers]
        return jobj
   
    
class Assignment:
    
    def __init__(self) -> None:
        self.id:str = None
        self.title:str = None
        self.text:str = None
        self.last_updated:datetime = None
        self.available_date:datetime = None
        self.due_date:datetime = None
            
    def to_json(self) -> any:
        jobj = {}
        jobj['title'] = self.title
        jobj['text'] = self.text
        jobj['last_updated'] = self.last_updated.isoformat()
        try:
            jobj['available_date'] = self.available_date.isoformat()
        except:
            pass
        try:
            jobj['due_date'] = self.due_date.isoformat()
        except:
            pass
        jobj['id'] = self.id
        return jobj
    
    @classmethod
    def from_params(cls, title:str, text:str, last_updated:datetime=None, available_date:datetime=None, due_date:datetime=None, id:str=None):
        obj = cls()
        obj.title = title
        obj.text = text
        obj.last_updated = last_updated
        obj.available_date = available_date
        obj.due_date = due_date
        obj.id = id
        return obj 
    
    
class Quiz(Assignment):
    
    def __init__(self) -> None:
        self.sections:List[QuizSection] = []
        
    def add_section(self, section:QuizSection):
        self.sections.append(section)
            
    def to_json(self) -> any:
        jobj = super().to_json()
        jobj['sections'] = [s.to_json() for s in self.sections]
        return jobj
    
