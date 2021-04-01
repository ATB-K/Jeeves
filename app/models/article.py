import sys

from app.application import ENGINE, Base
from sqlalchemy import Column, DateTime, Float, Integer, String


class Article(Base):
    """
    記事1件の情報を保持する。

    Attributes
    ----------
    url : String
        記事のURL
    title : String
        記事名
    tag : String
        タグ
    image : String
        アイキャッチ画像のパス
    datetime : DateTime
        記事の公開日時
    site_name : String
        記事のサイト
    """
    
    __tablename__ = 'articles'

    url       = Column('LINK',          String, primary_key = True)
    title     = Column('TITLE',         String)
    tag       = Column('TAG',           String)
    image     = Column('IMAGE_URL',     String)
    datetime  = Column('PUB_DATETIME',  DateTime)
    site_name = Column('SITE_NAME',     String)
