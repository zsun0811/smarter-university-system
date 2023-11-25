import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
    
    def tearDown(self):
        # Clean up after each test
        self.ctrl.clear_data()
        
    def test_expose_failure_01(self):
        """
        None quiz ID, Quiz_controller.py, Line 63
        """
        result = self.ctrl.add_quiz(None,"test",None,None)
        self.assertIsNone(result, 'None quiz ID, Quiz_controller.py, Line 63')

    def test_expose_failure_02(self):
        """
        Invalid Date while adding quiz, Quiz_controller.py, Line 64
        """
        result = self.ctrl.add_quiz("Valid Title","Valid Text","Invalid Date",None)
        self.assertIsNone(result, 'Invalid Date should have raised exception and quiz should not have been saved')
        
    def test_expose_failure_03(self):
        """
        Invalid Boolean while adding answer, Quiz_controller.py, Line 92
        """
        quizId = self.ctrl.add_quiz("Valid Title","Valid Text",None,None)
        questionId = self.ctrl.add_question(quizId, "Question 1", "Text for Question 1")
        answerId = self.ctrl.add_answer(questionId,"Answer Text", "INVALID BOOLEAN")
        self.assertIsNone(answerId, 'Invalid Boolean should have raised exception and answer should not have been saved')
        

if __name__ == '__main__':
    unittest.main()