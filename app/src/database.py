import os
from pymongo import MongoClient as _client

mongodb = _client('mongodb://mongodb:27017/')

db = mongodb.visits
