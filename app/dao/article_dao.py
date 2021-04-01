from app.application import session
from app.models.article import Article
from sqlalchemy import desc


def fetch_article_by_date(start, end):
    """
    記事データを日付で取得する

    Parameters
    ----------
    start : String
        開始日時
    end : String
        終了日時

    Returns
    -------
    List[Article]
        記事データリスト
    """
    return session.query(Article).\
        filter(Article.datetime >= start).\
        filter(Article.datetime < end).\
        order_by(desc(Article.datetime)).all()

def fetch_article_by_site(site_name, page):
    """
    記事データをサイト名で取得する

    Parameters
    ----------
    site_name : String
        サイト名
    page : int
        開始地点

    Returns
    -------
    List[Article]
        記事データリスト
    """
    return session.query(Article).\
        filter(Article.site_name == site_name).\
        order_by(desc(Article.datetime)).\
        limit(50).offset(page).all()

def fetch_article_by_tag(tag, page):
    """
    記事データをタグ名で取得する

    Parameters
    ----------
    tag : String
        タグ
    page : int
        開始地点

    Returns
    -------
    List[Article]
        記事データリスト
    """
    return session.query(Article).\
        filter(Article.tag == tag).\
        order_by(desc(Article.datetime)).\
        limit(50).offset(page).all()

def fetch_duplicate(urls):
    """
    記事データの重複データを取得する

    Parameters
    ----------
    urls : List[String]
        URLのList

    Returns
    -------
    List[Article]
        記事データリスト
    """
    return session.query(Article).\
        filter(Article.url.in_(urls)).all()

def insert_article(articles):
    """
    記事データを登録する

    Parameters
    ----------
    articles : List[Article]
        記事データリスト

    Returns
    -------
    None
        なし
    """
    session.add_all(articles)
    session.commit()
