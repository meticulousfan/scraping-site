# TwitterScraper
# Copyright 2016-2020 Ahmet Taspinar
# See LICENSE for details.
"""
Twitter Scraper tool
"""

__version__ = '1.5.0'
__author__ = 'Ahmet Taspinar'
__license__ = 'MIT'


from twitterscraper.query import query_tweets
from twitterscraper.query import query_tweets_from_user
from twitterscraper.query import query_user_info
from twitterscraper.tweet import Tweet
from twitterscraper.user import User
from twitterscraper.ts_logger import logger as ts_logger
