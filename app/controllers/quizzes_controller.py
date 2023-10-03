from typing import List
from datetime import datetime

from app.utils.data_loader import load_data,save_data
from app.utils import utils
from app.model.assignments import Quiz, Question, AnswerOption
from app.controllers.controller_interface import IController


class QuizzesController(IController):
    """
    This controller manages all CRUD activities related
    to quizzes. That includes adding, retrieving, and 
    removing quizzes and other items in its hierarchy.
    """
    
    def __init__(self, file_name = 'assignments.json') -> None:
        super().__init__(file_name)
        self.quizzes:List[Quiz] = self._load_data()
        
    def _load_data(self) -> List[Quiz]:
        """
        Loads the already stored data from a JSON file. Every
        items in the JSON file is converted into a runtime object.
        """
        quizzes = []
        for qobj in load_data(self.file_name):
            last_updated = datetime.fromisoformat(qobj['last_updated'])
            try:
                available_date = datetime.fromisoformat(qobj['available_date'])
            except:
                available_date = None
            try:
                due_date = datetime.fromisoformat(qobj['due_date'])
            except:
                due_date = None
            quiz = Quiz.from_params(qobj['title'],qobj['text'],last_updated,available_date,due_date,id=qobj['id'])
            for sobj in qobj['sections']:
                qst_last_updated = datetime.fromisoformat(sobj['last_updated'])
                question = Question.from_params(sobj['title'], sobj['text'],qst_last_updated,id=sobj['id'])
                for aobj in sobj['answers']:
                    # text:str, is_correct:bool=False, id:str=None):
                    answer = AnswerOption.from_params(aobj['text'],aobj['is_correct'],id=aobj['id'])
                    question.add_answer_option(answer)
                quiz.add_section(question)
            quizzes.append(quiz)
        return quizzes
    
    def _save_data(self):
        """
        Saves the objects that are in the current list
        to the JSON file for permanent storage.
        """
        json_data:any = [q.to_json() for q in self.quizzes]
        save_data(self.file_name,json_data)
        
    def add_quiz(self, title:str, text:str, available_date:datetime, due_date:datetime) -> str:
        """
        Add a new quiz. This is called when the user 
        creates a new quiz from the user interface.
        """
        updated_date = datetime.now()
        quiz_id = utils.generate_id(title + updated_date.isoformat())
        quiz = Quiz.from_params(title, text, updated_date,available_date,due_date, quiz_id)
        self.quizzes.append(quiz)
        self._save_data()
        return quiz.id
        
    def add_question(self, quiz_id:str, title:str, text:str) -> str:
        """
        Add a new question to the quiz that is specified
        in quiz_id. Note that the parent quiz must already
        exist.
        """
        quiz = self.get_quiz_by_id(quiz_id)
        if quiz is not None:
            last_updated = datetime.now()
            question_id = utils.generate_id(f'{title}{last_updated.isoformat()}')
            question = Question.from_params(title, text, last_updated,question_id)
            quiz.add_section(question)
            self._save_data()
            return question.id
    
    def add_answer(self, question_id:str, text:str, is_correct:bool) -> str:
        """
        Add answer to an already existing quiz.
        """
        question = self.get_question_by_id(question_id)
        if question is not None:
            last_updated = datetime.now()
            answer_id = utils.generate_id(f'{text}{last_updated.isoformat()}')
            answer = AnswerOption.from_params(text,is_correct,answer_id)
            question.add_answer_option(answer)
            self._save_data()
            return answer.id
    

    def get_quizzes(self) -> List[Quiz]:
        """
        Simply returns all quizzes.
        """
        return self.quizzes
    
    
    def remove_quiz(self, quiz_id:str):
        """
        Finds the quiz with the specified ID
        and takes it out of the list.
        """
        self.quizzes = [q for q in self.quizzes if q.id != quiz_id]
    
    def get_quiz_by_id(self, quiz_id:str) -> Quiz:
        """
        Utility function to get a specific quiz. This will be called
        when the user select a quiz and views the detail page.
        """
        quizzes = [q for q in self.quizzes if q.id == quiz_id]
        if len(quizzes) <= 0:
            print(f'Quiz with id {quiz_id} does not exists.')
            return None
        else:
            return quizzes[0]
        
    def get_question_by_id(self, question_id:str) -> Question:
        """
        Returns the question specified by the ID. It'll find
        it without knowing what quiz it belongs to.
        """
        questions = [question for quiz in self.quizzes for question in quiz.sections if question.id == question_id]
        if len(questions) <= 0:
            print(f'Question with id {question_id} does not exists.')
            return None
        else:
            return questions[0]
        
    def clear_data(self):
        """
        Delete all stored data.
        """
        self.quizzes = []
        self._save_data()
        
        
    def print_quiz(self, quiz_id:str):
        """
        Prints the content of a quiz to the console.
        That can be used for debugging.
        """
        quiz:Quiz = self.get_quiz_by_id(quiz_id)
        if quiz is not None:
            print(f'\n[{quiz.last_updated.strftime("%Y-%m-%d %H:%M:%S")}] {quiz.title}\n{quiz.text}')
            for s_idx, section in enumerate(quiz.sections):
                print(f'\t({s_idx+1}) [{section.last_updated.strftime("%Y-%m-%d %H:%M:%S")}] {section.title}\n\t{section.text}')
                for a_idx, answer in enumerate(section.answers):
                    print(f'\t\t({a_idx+1}) [{answer.is_correct}] {answer.text}')
    
