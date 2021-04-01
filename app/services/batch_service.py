from datetime import datetime

import feedparser
from app.application import app
from app.dao.article_dao import fetch_duplicate, insert_article
from app.dao.rss_dao import fetch_rss_all
from app.lib.deep_learning import predict
from app.lib.eyecatch import (search_eyecatch_by_article,
                              search_eyecatch_by_feed)
from app.lib.robots import check_robots
from app.models.article import Article


def collection_news():
    """
    ニュースを回収する

    Parameters
    ----------
    None
        なし

    Returns
    -------
    None
        なし
    """

    app.logger.info("----- Start Batch [" + datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "] -----")

    # RSSの一覧を取得
    targets = fetch_rss_all()

    for site in targets:
        try:
            # RSS情報を取得
            news = get_news(site.url)

            # 重複確認
            news = check_duplicate(news)

            # robots.txtを確認
            interval = check_robots(site.robots)

            # アイキャッチ画像取得
            news = search_eyecatch_by_article(news, site, interval)

            # 登録処理
            if len(news):

                # 記事登録
                insert_article(news)

                app.logger.info("Successful collection of (" + site.site_name + ")")
            else:
                app.logger.info("Skip collection of (" + site.site_name + ")")

        except:
            app.logger.error("----- Start Error Log  -----", exc_info=True)
            app.logger.error("(" + site.site_name + ") collection failure.")
    
    app.logger.info("-----  End Batch  [" + datetime.today().strftime("%Y-%m-%d %H:%M:%S") + "] -----")

def get_news(url):
    """
    RSSから記事情報をListで取得

    Parameters
    ----------
    url : String
        RSSのURL

    Returns
    -------
    list[Article]
        記事のList
    """

    # RSS情報を取得
    feeds = feedparser.parse(url)

    ai = predict()

    articles = list()

    for feed in feeds['entries']:
        article = Article()

        # 記事へのURL
        article.url = feed['link']

        # 記事名
        article.title = feed['title']

        # タグ
        if app.config["TAG_JUDGMENT_BY_AI"]:
            article.tag = get_tag(feed) + "," + ai.tag_judgment(article.title)
        else:
            article.tag = get_tag(feed)

        # Rss内の画像取得
        article.image = search_eyecatch_by_feed(feed)

        # 記事更新日 TODO:要改善
        article.datetime = datetime.today().strftime("%Y/%m/%d %H:%M:%S")

        # サイトタイトル
        article.site_name = feeds['feed']['title']

        articles.append(article)
    
    return articles

def get_tag(feed):
    try:
        return feed['tags'][0]['term']
    except (IndexError, KeyError):
        return ""

def check_duplicate(newes):
    """
    重複する記事を削除する

    Parameters
    ----------
    newes : list[Article]
        記事のList(重複削除未)

    Returns
    -------
    list[Article]
        記事のList(重複削除済)
    """

    urls = list(map(lambda s: s.url, newes))

    # 重複した記事を取得
    duplicate = fetch_duplicate(urls)

    articles = list()

    # 重複してない記事を抽出
    for news in newes:
        for item in duplicate:
            if news.url == item.url:
                # breakで中断するとelseに入らない
                break
        else:
            articles.append(news)

    return articles
