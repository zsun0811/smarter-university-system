
from flask import Blueprint, request, send_from_directory
import json


from app.controllers.activities_controller import ActivitiesController
activities = ActivitiesController()
from app.controllers.discussions_controller import DiscussionsController
discussions = DiscussionsController()


controller = Blueprint('config', __name__)

@controller.route('/discussions', methods=['GET'])
def get_discussions():
    return discussions.get_discussions()

@controller.route('/discussion', methods=['POST'])
def add_discussion():
    return discussions.add_discussion_from_payload(request.data.decode(), request.args)

@controller.route('/activity', methods=['POST'])
def add_activity():
    return activities.add_activity_from_payload(request.data.decode(), request.args)
