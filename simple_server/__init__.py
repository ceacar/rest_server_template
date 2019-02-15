import os
from flask import Flask
import tasks
import health


def create_app():
    app = Flask(__name__)

    tasks_api = tasks.TasksAPI.as_view("TasksAPI")
    app.add_url_rule(
        "/link1/<key>", view_func=tasks_api, methods=["GET"]
    )
    app.add_url_rule("/link2", view_func=tasks_api, methods=["POST"])

    stats_api = health.StatusAPI.as_view("stats")
    app.add_url_rule("/health", view_func=stats_api, methods=["GET"])
    return app


app = create_app()


@app.route("/")
def root():
    return "Weather tracker is up and running!"
