
from typing import List
from datetime import datetime

from app.utils import utils
from app.utils.data_loader import load_data, save_data
from app.controllers.controller_interface import IController
from app.model.activities import Activity


class ActivitiesController(IController):
    """
    Controller for managing the activity stream.
    """
    
    def __init__(self, file_name:str = 'activities.json') -> None:
        super().__init__(file_name)
        self.activities:List[Activity] = self._load_data()
        
    def _load_data(self):
        activities = []
        for obj in load_data(self.file_name):
            try:
                post_time = datetime.fromisoformat(obj['created'])
            except:
                post_time = None
            try:
                due_time = datetime.fromisoformat(obj['updated'])
            except:
                due_time = None
            activity = Activity.from_params(obj['text'],obj['directed'],obj['recipients'],post_time,due_time,obj['flag'],obj['lat'],obj['lon'],id=obj['id'])
            activities.append(activity)
        return activities
    
    def _save_data(self):
        json_data:any = [a.to_json() for a in self.activities]
        save_data(self.file_name,json_data)
        
    def clear_data(self):
        self.activities = []
        self._save_data()
        
    def add_activity_from_payload(self, payload:any) -> None:
        """
        This parses the parameters that were passed in via
        the API endpoint and creates a new Activity object.
        It also handles any invalid data that may have been
        specified by the API consumer.
        """
        pass