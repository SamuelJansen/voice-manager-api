from python_helper import Constant as c
from python_helper import EnvironmentHelper
from python_framework import ResourceManager, FlaskUtil, HttpStatus
from queue_manager_api import QueueManager

import ModelAssociation


app = ResourceManager.initialize(__name__, ModelAssociation.MODEL, managerList=[
    QueueManager()
])

from flask import send_file

@app.route(f'{app.api.baseUrl}/audios/<string:key>')
def getAudio(key=None):
    try:
        dto = app.api.resource.service.speak.findAudioByKey(key)
        path = f'''{dto.path.split(f'src{EnvironmentHelper.OS_SEPARATOR}')[-1]}{EnvironmentHelper.OS_SEPARATOR}{dto.name}{c.DOT}{dto.extension}'''
        return send_file(
            path,
            mimetype="audio/mp3",
            as_attachment=False
        ), HttpStatus.OK
    except Exception as exception:
        print(exception)
    return {'message': 'Audio not found'}, 400
