#!/usr/bin/python

import os

__author__ = 'Preetam'

USE_TOKEN_AUTH = False
USE_RATE_LIMITS = False


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_DB = 'adnota_dev_db'
    #MONGODB_HOST
    #MONGODB_PORT
    #MONGODB_USERNAME
    #MONGODB_PASSWORD

class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
