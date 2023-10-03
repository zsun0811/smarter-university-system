

from flask import Flask
from api import controller

import logging
logger = logging.getLogger(__name__)



app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.register_blueprint(controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9083)