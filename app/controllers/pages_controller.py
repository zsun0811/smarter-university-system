
from typing import List
from datetime import datetime

from app.model.pages import Page
from app.utils import utils
from app.utils.data_loader import load_data, save_data
from app.controllers.controller_interface import IController


class PagesController(IController):
    """
    Controller for managing course pages. A page is a way
    to communicate additional information that does not fit
    into the course slides.
    """
    
    def __init__(self, file_name:str = 'pages.json') -> None:
        super(file_name)
        self.pages:List[Page] = self._load_data()
        
    def _load_data(self):
        pages = []
        for obj in load_data(self.file_name):
            page = Page.from_params(obj['title'],obj['text'],id=obj['id'])
            page.created = datetime.fromisoformat(obj['created'])
            page.updated = datetime.fromisoformat(obj['updated'])
            pages.append(page)
        return pages
    
    def _save_data(self):
        json_data:any = [d.to_json() for d in self.pages]
        save_data(self.file_name,json_data)
        
    def clear_data(self):
        self.pages = []
        self._save_data()
        
    def add_page(self, title:str, text:str) -> str:
        page = Page.from_params(title, text)
        page.created = datetime.now()
        page.updated = datetime.now()
        page.id = utils.generate_id(title + page.created.isoformat())
        self.pages.append(page)
        self._save_data()
        return page.id
    
    def update_page(self, page_id:str, title:str=None, text:str=None) -> str:
        page = self.get_page_by_id(page_id)
        if page is not None:
            if title is not None:
                page.title = title
            if text is not None:
                page.text = text
            page.updated = datetime.now()
            self._save_data()
            return page.id
    
    def get_page_by_id(self, page_id:str) -> Page:
        pages = [d for d in self.pages if d.id == page_id]
        if len(pages) <= 0:
            print(f'Page with id {page_id} does not exists.')
            return None
        else:
            return pages[0]
    