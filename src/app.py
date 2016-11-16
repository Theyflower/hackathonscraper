#!/usr/bin/env python3	
from flask import Flask, render_template, jsonify
import hackscraper
# from flask_restful import Resource, Api #i should use this
app = Flask('hackathonscraperAPI')

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/api')
def api():
	return render_template('api.html', data=hackscraper.scrape(returnjson=True))
app.add_url_rule('/api', 'api', api)
app.add_url_rule('/', 'index', index)