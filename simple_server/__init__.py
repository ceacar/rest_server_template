import os
from flask import Flask


def create_app():
    app = Flask(__name__)

    tasks_api = tasks.as_view("TasksAPI")
    app.add_url_rule(
        "/url0/<key>", view_func=tasks_api, methods=["GET"]
    )
    app.add_url_rule("/url1", view_func=tasks_api, methods=["POST"])

    stats_api = StatsAPI.as_view("stats")
    app.add_url_rule("/stats", view_func=stats_api, methods=["GET"])
    return app


app = create_app()


@app.route("/")
def root():
    return "Weather tracker is up and running!"
