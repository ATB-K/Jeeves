from app.application import app
from app.services.index_service import get_request, post_request
from flask import Blueprint, render_template, request

POST = "POST"
GET = "GET"

bp_index = Blueprint("index", __name__)

@bp_index.route("/", methods=[GET, POST])
def index():
    """
    Jeevesのメイン画面

    Parameters
    ----------
    request : request
        リクエスト情報

    Returns
    -------
    Text
        htmlの文字列
    """

    app.logger.info("Access from [" + request.remote_addr + "]")

    article = None

    if request.method == POST:
        html, article = post_request(request)
    else:
        html, article = get_request(request)

    return render_template(html, news=article)
