import os

from flask import Flask
from flask_script import Manager
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *

# Flask
app = Flask(__name__, instance_relative_config=True)


# Command
manager = Manager(app)


# 標準設定ファイル読み込み
app.config.from_object("setting")


# 非公開設定ファイル読み込み
if app.config["ENV"] == "development":
    app.config.from_pyfile(os.path.join("config", "development.py"), silent=True)
else:
    app.config.from_pyfile(os.path.join("config", "production.py"), silent=True)


# DB情報
DATABASE = '%s://%s:%s@%s:%s/%s' % (
    app.config["DB_TYPE"], # DBの種類
    app.config["DB_USER"], # ユーザ名
    app.config["DB_PW"],   # パスワード
    app.config["DB_IP"],   # IPアドレス
    app.config["DB_PORT"], # ポート番号
    app.config["DB_NAME"]  # データベース名
)


# エンジン定義
ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo = app.config["DEBUG"] # Trueだと実行のたびにSQLが出力される
)


# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するなど。
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)


# modelsで使用する
Base = declarative_base()
Base.query = session.query_property()
