import random
from urllib.robotparser import RobotFileParser


def check_robots(robots_path):
    """
    robots.txtをチェックし、アクセス間隔を取得

    Parameters
    ----------
    robots_path : String
        robots.txtのURL

    Returns
    -------
    int
        記事取得間隔(秒)
    """

    # パス未指定なら適当な間隔を返却
    if robots_path == None or "":
        return random.randint(5,10)

    rp = RobotFileParser()

    rp.set_url(robots_path)
    rp.read()

    delay = None

    try:
        delay = rp.crawl_delay('*')

        if delay == None:
            raise  AttributeError

    except AttributeError:
        delay = random.randint(5,10)

    return delay
