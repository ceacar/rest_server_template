import os
from flask import Flask
import cache_api
import status

def create_app():
    app = Flask(__name__)

    tasks_api = cache_api.CacheAPI.as_view("TasksAPI")
    stats_api = status.StatusAPI.as_view("stats")

    app.add_url_rule("/get/<key>", view_func=tasks_api, methods=["GET"])
    app.add_url_rule("/save", view_func=tasks_api, methods=["POST"])
    app.add_url_rule("/health", view_func=stats_api, methods=["GET"])

    return app

app = create_app()

@app.route("/")
def root():
    return ("Blazing Potato is up and running!",200)
