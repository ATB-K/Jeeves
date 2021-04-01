import logging
import logging.handlers


# サーバログ定義
def server_handler():
    server = logging.handlers.RotatingFileHandler("log/Jeeves.log", "a+", maxBytes=50000, backupCount=5)
    server.setLevel(logging.DEBUG) 
    server.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] [%(module)s.py]: %(message)s'))
    return server


# バッチログ定義
def batch_handler():
    batch = logging.handlers.RotatingFileHandler("log/JeevesBatch.log", "a+", maxBytes=50000, backupCount=5)
    batch.setLevel(logging.INFO) 
    batch.setFormatter(logging.Formatter('[%(asctime)s] [%(levelname)s] [%(module)s.py]: %(message)s'))
    return batch
