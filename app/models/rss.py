import sys

from app.application import ENGINE, Base
from sqlalchemy import Column, DateTime, Float, Integer, String


class Rss(Base):
    """
    RSS1件の情報を保持する。

    Attributes
    ----------
    url : String
        RSSのURL
    site_name : String
        記事のサイト
    eye_catch : String
        アイキャッチ検索用のタグ
    option
        アイキャッチ検索時のオプション情報
    robots
        robots.txtのURL
    """
    
    __tablename__ = 'rss'

    url       = Column('LINK',      String, primary_key = True)
    site_name = Column('SITE_NAME', String)
    eye_catch = Column('EYE_CATCH', String)
    option    = Column('OPTION',    String)
    robots    = Column('ROBOTS',    String)
