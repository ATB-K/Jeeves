from datetime import datetime, timedelta

from app.application import app
from app.dao.article_dao import fetch_article_by_date, fetch_article_by_site


def post_request(request):
    """
    POSTリクエスト処理

    Parameters
    ----------
    request : request
        リクエスト情報

    Returns
    -------
    String
        応答データに利用するhtmlファイル名
    list[Dict[str, Any]]
        htmlに展開する記事データリスト
    """

    name, value = parse_request(request)

    if name == "DATE":
        start, end = day_range(datetime.strptime(value, '%Y-%m-%d %H:%M:%S'))

        articles = fetch_article_by_date(start, end)
    elif  name == "SITE":
        articles = fetch_article_by_site(value, 0)
    else:
        pass
    
    return "JeevesReload.html", to_list(articles)

def get_request(request):
    """
    GETリクエスト処理

    Parameters
    ----------
    request : request
        リクエスト情報

    Returns
    -------
    String
        応答データに利用するhtmlファイル名
    list[Dict[str, Any]]
        htmlに展開する記事データリスト
    """

    start, end  = day_range(datetime.today())

    articles = fetch_article_by_date(start, end)
    
    return "JeevesBase.html", to_list(articles)

def to_list(article):
    return list(map(lambda s: s.__dict__, article))

def parse_request(request):
    """
    リクエストのデータをパースする

    Parameters
    ----------
    request : request
        リクエスト

    Returns
    -------
    String
        パラメータ名称
    String
        設定値
    """

    param = request.get_data().decode('utf-8').split("=")

    return param[0], param[1]

def day_range(start):
    """
    取得範囲を特定

    Parameters
    ----------
    start : String
        開始日時

    Returns
    -------
    String
        開始日時 (時分秒は0固定)
    String
        終了日時 (時分秒は0固定)
    """

    end = start + timedelta(days=1)

    return start.strftime('%Y-%m-%d 00:00:00'), end.strftime('%Y-%m-%d 00:00:00')
