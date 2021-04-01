from app.application import app
from flask_script import Command


@Command
def server():
    """
    サーバ起動
    """

    from app.lib.logger import server_handler

    app.logger.addHandler(server_handler())

    app.run(host=app.config["SERVER_IP"], port=app.config["SERVER_PORT"])

@Command
def batch():
    """
    バッチ起動
    """

    from app.lib.logger import batch_handler
    from app.services.batch_service import collection_news

    app.logger.addHandler(batch_handler())

    collection_news()

@Command
def show():
    """
    設定値参照
    """

    from tabulate import tabulate

    headers = ["NAME", "VALUE"]

    table =  list(map(lambda s: [s, app.config[s]], app.config))

    result = tabulate(table, headers, tablefmt="grid")

    print(result)

@Command
def init():
    """
    初期化処理
    """

    from app.application import ENGINE, Base
    from app.models.article import Article
    from app.models.rss import Rss

    Base.metadata.create_all(bind=ENGINE)

@Command
def learning(input_file_path):
    """
    予測データ生成
    """
    from app.lib.deep_learning import learning

    learning(input_file_path)
