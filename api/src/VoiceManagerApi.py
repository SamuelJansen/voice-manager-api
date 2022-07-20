from flask import send_file

from python_helper import Constant as c
from python_helper import EnvironmentHelper, log
from python_framework import ResourceManager, FlaskUtil, HttpStatus, LogConstant
from queue_manager_api import QueueManager

import ModelAssociation


app = ResourceManager.initialize(__name__, ModelAssociation.MODEL, managerList=[
    QueueManager()
])


@app.route(f'{app.api.baseUrl}/audios/<string:key>')
def getAudio(key=None):
    log.info(getAudio, f'{LogConstant.CONTROLLER_SPACE}{FlaskUtil.safellyGetVerb()}{c.SPACE_DASH_SPACE}{FlaskUtil.safellyGetUrl()}')
    try:
        dto = app.api.resource.service.speak.findAudioByKey(key)
        path = f'''{dto.path.split(f'src{EnvironmentHelper.OS_SEPARATOR}')[-1]}{EnvironmentHelper.OS_SEPARATOR}{dto.name}{c.DOT}{dto.extension}'''
        return send_file(
            path,
            mimetype="audio/mp3",
            as_attachment=False
        ), HttpStatus.OK
    except Exception as exception:
        MESSAGE_KEY = 'message'
        responseDto = {MESSAGE_KEY: 'Audio not found'}
        log.error(getAudio, responseDto.get(MESSAGE_KEY), exception=exception)
    return responseDto, 404 
