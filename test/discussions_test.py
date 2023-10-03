import unittest

from app.controllers.discussions_controller import DiscussionsController

class DiscussionsTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = DiscussionsController('discussions_test.json')
        
    def test_add_discussion(self):
        self.ctrl.clear_data()
        discussion_id = self.ctrl.add_discussion("Discssion Title", "text", "user_01")
        # Check that we have one discussion in the list
        discussions = self.ctrl.get_discussions()
        self.assertEquals(len(discussions), 1, "There is exactly one discussion.")
        # Check that we can retrieve the added discussion
        discussion = self.ctrl.get_discussion_by_id(discussion_id)
        self.assertIsNotNone(discussion, "The discussion can be retrieved.")
        
    def test_add_response(self):
        self.ctrl.clear_data()
        discussion_id = self.ctrl.add_discussion("Discssion Title", "text", "user_01")
        response_id = self.ctrl.add_response(discussion_id, "response text", "user_01")
        # Check that we can retrieve the added response
        response = self.ctrl.get_response_by_id(response_id)
        self.assertIsNotNone(response, "The response can be retrieved.")
        

if __name__ == '__main__':
    unittest.main()