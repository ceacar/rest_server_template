
from flask import request, jsonify
from flask.views import MethodView
from werkzeug.exceptions import abort


class StatusAPI(MethodView):
    def get(self):
        return ('healthy', 200)
