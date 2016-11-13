#!/usr/bin/python	
from flask import Flask, render_template
# from flask_restful import Resource, Api #i should use this

app = Flask('hackscraperAPI')
# api = Api(app)
def index():
	render_template("index.html")

def api():
	render_template(hackathons.JSON)
app.add_url_rule('/', 'api', api)
app.add_url_rule('/', 'index', index)