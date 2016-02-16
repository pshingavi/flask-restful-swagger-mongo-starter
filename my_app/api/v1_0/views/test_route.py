from .. import api

__author__ = 'Preetam'

@api.route('/test')
def test():
    return "<h1>Hello world</h1>"
