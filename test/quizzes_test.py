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
        


if __name__ == '__main__':
    unittest.main()