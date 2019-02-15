from flask import request, jsonify
from flask.views import MethodView
from werkzeug.exceptions import abort
from simple_server import cache


class TasksAPI(MethodView):

    def post(self):
        req_data = request.get_json()
        try:
            need_data = req_data.get("field1", "")

            return (str(need_data), 400)
        except Exception:
            abort("Unknown Error", 501)

    def get(self, key: str):

        try:
            res = cache.get_cacher().get(key)
            return (str(res), 200)
        except Exception:
            abort(501)
