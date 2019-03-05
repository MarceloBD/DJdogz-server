import os, sys
from flask import Flask, jsonify, request, redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from decouple import config
import json 

app = Flask(__name__)

@app.route('/')
def display():
    return 'here'

@app.route('/getMusics')
def musics():
	engine = create_engine(config('URI'))
	db = scoped_session(sessionmaker(bind=engine))
	result = db.execute("SELECT * FROM MUSIC")
	music_list = []
	for rowProxy in result.fetchall():
		music_list += [list(rowProxy)]
	return json.dumps(music_list)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='https://djdogz.herokuapp.com/', port=port)
