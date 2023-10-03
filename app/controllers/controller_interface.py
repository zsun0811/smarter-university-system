

from abc import ABCMeta, abstractmethod

class IController(metaclass=ABCMeta):
    """
    Controller interface specified methods that must
    be implemented by child controllers. That ensures
    that we can call controllers consistently.
    """
    
    def __init__(self, file_name) -> None:
        self.file_name = file_name
        
    @abstractmethod
    def _load_data(self): raise NotImplementedError
    
    @abstractmethod
    def _save_data(self): raise NotImplementedError
    
    @abstractmethod
    def clear_data(self): raise NotImplementedError
        
    