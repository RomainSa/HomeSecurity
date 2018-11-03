from shutil import copyfile
import os
import glob
import configparser
from functools import wraps

from flask import Flask, Response, request, render_template, url_for
app = Flask(__name__)
config = configparser.ConfigParser()
config.read('conf.cfg')
login = os.environ['FLASK_LOGIN']
password = os.environ['FLASK_PASSWORD']
url = os.environ['FLASK_APP_URL']


def check_auth(login_, password_):
    """This function is called to check if a username /
    password combination is valid.
    """
    return login_ == login and password_ == password


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response('Could not verify your access level for that URL.\n'
                    'You have to login with proper credentials', 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@app.route('/', methods=['GET'])
@requires_auth
def index():
    """Home page"""
    snapshots_folder = config['server']['snapshots_folder']
    files = [f for f in glob.glob(snapshots_folder + '*') if '.jpg' in f]
    if len(files) > 0:
        # last screenshot
        latest_snapshot_path = max(files, key=os.path.getctime)
        # copy in static folder
        copyfile(latest_snapshot_path, 'static/home.jpg')
    return render_template('index.html',
                           url=url,
                           img=url_for('static', filename='home.jpg'))
