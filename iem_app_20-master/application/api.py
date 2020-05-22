from datetime import date
from flask import Flask, render_template, request, current_app, g
from . import app
from .db import add_measurement

@app.route('/api/post_data', methods=('POST',))
def api_post_data():

    data = request.json
    add_measurement(
        data['unit_id'],
        data['registered'],
        data['bmp280_temperature'],
        data['bmp280_pressure'],
        data['si7021_temperature'],
        data['si7021_humidity'],
        data['ccs811_tvoc'],
        data['sds011_dust']
    )
    print('Data i Flask App:', data)
    #else:
        # Hvis ikke rikitg nøkkel, så returnere vi en 401 kode: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401
    #    abort(401)
    return 'Data received!'

@app.route('/api/test', methods=('POST',))
def api_test():
    """
    Start på api for å motta data fra ESP
    Data sendes som json
    """
    data = request.json
 
    print('Data i Flask App:', data)
    return 'Data received!'






