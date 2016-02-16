from my_app import create_app
from flask_script  import Manager
import os

__author__ = 'Preetam'

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()