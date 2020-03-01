from flask import Blueprint, Response, make_response
from loguru import logger

from ..main import app

app_bp = Blueprint("version_blueprint", __name__)


@app_bp.route("/ping")
def ping() -> Response:
    logger.info("Got ping request!")
    return make_response("pong")


app.register_blueprint(app_bp, url_prefix="/v0/")
