import os
from flask import jsonify
from core import app
from database import db, mongodb

@app.route("/")
def home():
  
  try:  
    visits = db.visits.find_one()
    visits['count'] = visits['count'] + 1
    db.visits.update_one({
      '_id': visits['_id']
    }, {
      '$set': {
        'count': visits['count']
      }
    }, upsert=False)
  except:
    db.visits.insert_one({ 'count': 1 })
    visits = db.visits.find_one()

  html = """
    <div><strong>Хэш контейнера с приложением:</strong> {0}</div>
    <div><strong>Кол-во просмотров страницы:</strong> {1}</div>
  """
  
  return html.format(os.environ['HOSTNAME'], visits['count'])

@app.route("/config")
def config():
  return jsonify(dict(os.environ))
