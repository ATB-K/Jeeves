import re
import time

import requests
from bs4 import BeautifulSoup


def search_eyecatch_by_feed(feed):
    """
    記事画像をRss情報内から取得する

    Parameters
    ----------
    feed : FeedParserDict
        RSS情報の辞書データ

    Returns
    -------
    String
        RSS内の画像パス
    """

    # summaryをチェック
    if "summary" in feed:
        image = search_in_feed(feed["summary"])
        if image != "":
            return image

    # contentをチェック
    if "content" in feed:
        image = search_in_feed(feed["content"][0]["value"])
        if image != "":
            return image
    
    # media_contentをチェック
    if "media_content" in feed:
        image = feed["media_content"][0]["url"]
        if image != "":
            return image

    return None

def search_eyecatch_by_article(newes, site, interval):
    """
    記事画像をリンク先から取得する

    Parameters
    ----------
    newes : List[Article]
        記事データリスト
    site : Rss
        サイトの情報

    Returns
    -------
    String
        記事内の画像パス
    """

    # 検索タグが未登録ならスキップ
    if site.eye_catch == "" or None:
        return newes

    for news in newes:
        if news.image == None:
            news.image = search_in_article(news.url, site.eye_catch)
        
        # 記事に連続アクセスは迷惑なので適当に待機
        time.sleep(interval)

    return newes

def search_in_feed(value):
    """
    記事画像をRss情報内から取得する

    Parameters
    ----------
    value : String
        RSS内の文字データ

    Returns
    -------
    String
        RSS内の画像パス
    """

    soup = BeautifulSoup(value, "html.parser")

    img = soup.find('img')
    if img != None:
        return img['src']
    else:
        return None

def search_in_article(url, tag):
    """
    記事画像をリンク先から取得する

    Parameters
    ----------
    url : String
        記事へのリンク
    tag : String
        検索時の目標となるタグ

    Returns
    -------
    String
        記事内の画像パス
    """

    HEADERS = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"}
    PATTERN = "(https?)(:\/\/[-_.!~*\'()a-zA-Z0-9;\/?:\@&=+\$,%#]+)\.(jpg|jpeg|gif|png)"

    # html取得
    html = requests.get(url=url, headers=HEADERS).content
    soup = BeautifulSoup(html, "html.parser")

    # 指定位置までシーク
    html = str(soup)
    point = html.find(tag)

    # 指定位置以降の最初に登場する画像ファイルを特定
    try:
        path = re.search(PATTERN, html[point:]).group()
    except AttributeError:
        path = ""
    
    return path
