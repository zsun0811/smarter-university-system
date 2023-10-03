from typing import List, Dict
from datetime import datetime

from app.utils.data_loader import load_data,save_data
from app.utils import utils
from app.model.discussion import DiscussionResponse, DiscussionThread, DiscussionReaction
from app.model.reaction import Reaction
from app.controllers.controller_interface import IController

class DiscussionsController(IController):
    """
    This controller handles all activities related to
    discussion items.
    """
    
    def __init__(self, file_name='discussions.json') -> None:
        super().__init__(file_name)
        self.discussions:List[DiscussionThread] = self._load_data()
        
    def _load_data(self):
        discussions = []
        for obj in load_data(self.file_name):
            thread = DiscussionThread.from_params(obj['title'],obj['text'],obj['author_id'],id=obj['id'])
            thread.timestamp = datetime.fromisoformat(obj['timestamp'])
            for robj in obj['responses']:
                response = DiscussionResponse.from_params(robj['text'],robj['author_id'],id=robj['id'])
                response.timestamp = datetime.fromisoformat(robj['timestamp'])
                for react_obj in robj['reactions']:
                    reaction = DiscussionReaction.from_params(Reaction[react_obj['reaction']],react_obj['user_id'],id=react_obj['id'])
                    reaction.timestamp = datetime.fromisoformat(react_obj['timestamp'])
                    response.add_reaction(reaction)
                thread.add_response(response)
            discussions.append(thread)
        return discussions
    
    def _save_data(self):
        json_data:any = [d.to_json() for d in self.discussions]
        save_data(self.file_name,json_data)
        
    def clear_data(self):
        self.discussions = []
        self._save_data()
        
    def add_discussion_from_payload(self, text:str, args:Dict[str,str]) -> str:
        """
        Reads the POST payload from the body and URL, and adds a new
        discussion.
        """
        
        # The title and user_id must be specified
        if 'title' not in args or 'user_id' not in args:
            return None
            
        return self.add_discussion(args['title'], text, args['user_id'])
        
    def add_discussion(self, title:str, text:str, user_id:str) -> str:
        """
        Add a new discussion to the list and saves it.
        """
        thread = DiscussionThread.from_params(title, text, user_id)
        thread.timestamp = datetime.now()
        thread.id = utils.generate_id(user_id + thread.timestamp.isoformat())
        self.discussions.append(thread)
        self._save_data()
        return thread.id
        
    def add_response(self, discussion_id:str, text:str, user_id:str) -> str:
        """
        Adds a response to a discussion.
        """
        discussion = self.get_discussion_by_id(discussion_id)
        if discussion is not None:
            response = DiscussionResponse.from_params(text, user_id, timestamp=datetime.now())
            response.id = utils.generate_id(f'{user_id}{response.timestamp.isoformat()}')
            discussion.add_response(response)
            self._save_data()
            return response.id
    
    def add_reaction(self, response_id:str, reaction:str, user_id:str) -> str:
        """
        Adds a reaction to a response.
        """
        response = self.get_response_by_id(response_id)
        if response is not None:
            reaction = DiscussionReaction.from_params(Reaction[reaction],user_id,timestamp=datetime.now())
            reaction.id = utils.generate_id(f'{user_id}{reaction.timestamp.isoformat()}')
            response.add_reaction(reaction)
            self._save_data()
            return reaction.id
    

    def get_discussions(self) -> List[DiscussionThread]:
        return self.discussions
    
    
    def remove_discusssion(self, discussion_id:str):
        self.discussions = [d for d in self.discussions if d.id != discussion_id]
    
    
    def get_discussion_by_id(self, discussion_id:str) -> DiscussionThread:
        discussions = [d for d in self.discussions if d.id == discussion_id]
        if len(discussions) <= 0:
            print(f'Discussion with id {discussion_id} does not exists.')
            return None
        else:
            return discussions[0]
        
    def get_response_by_id(self, response_id:str) -> DiscussionResponse:
        responses = [r for rs in self.discussions for r in rs.responses if r.id == response_id]
        if len(responses) <= 0:
            print(f'Response with id {response_id} does not exists.')
            return None
        else:
            return responses[0]
        
    def print_discussion_board(self):
        """
        Prints the content of the discussion board to
        console. This can be convenient for debugging.
        """
        for d_idx, disc in enumerate(self.discussions):
            print(f'\n({d_idx+1}) [{disc.timestamp.strftime("%Y-%m-%d %H:%M:%S")}] {disc.title}\n{disc.text}')
            for r_idx, resp in enumerate(disc.responses):
                react_vals:List[str] = [r.reaction.value for r in resp.reactions]
                reactions_str:str = ", ".join([f"{x} ({react_vals.count(x)})" for x in set(react_vals)])
                print(f'\t({r_idx+1}) [{resp.timestamp.strftime("%Y-%m-%d %H:%M:%S")}] {reactions_str}\n\t{resp.text}')
    