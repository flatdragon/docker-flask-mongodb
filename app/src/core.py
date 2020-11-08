import os
from flask import Flask as _create_app
from database import db as _db

app = _create_app(__name__)

_host = os.environ['HOSTNAME']

def serve():
  app.run(_host, 80)
