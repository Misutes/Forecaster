from flask import render_template
from flask_app.app import application
from Parser import get_val_list
from Predictor import visualization, building_model


@application.route('/')
def index():
    val_list = get_val_list()
    val_list = val_list.items()
    visualization(building_model(171, 255))
    return render_template('index.html', list=val_list)

