import os
from cachelib.file import FileSystemCache
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    ROOT_PATH = basedir
    STATIC_FOLDER = os.path.join(basedir, 'app/view/static')
    TEMPLATE_FOLDER = os.path.join(basedir, 'app/view/templates')
    SESSION_TYPE = 'cachelib'
    SESSION_SERIALIZATION_FORMAT = 'json'
    SESSION_CACHELIB = FileSystemCache(cache_dir='flask_session', threshold=500)
    HOSTNAME = os.environ.get('HOSTNAME') or 'localhost'
    PORT = 3000