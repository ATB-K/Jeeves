from app.application import session
from app.models.rss import Rss


def fetch_rss_all():
    """
    記事収集対象のRSSリンクを取得する

    Parameters
    ----------
    None
        なし

    Returns
    -------
    List[Rss]
        記事収集対象リスト
    """
    return session.query(Rss).all()
