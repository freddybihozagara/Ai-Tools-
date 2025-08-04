from flask import Flask, config, request, jsonify, render_template
import os
import pymysql.cursors
from datetime import datetime
from AiTools.config import init_env

config = init_env()

# Initialize Flask app
app = Flask(__name__)

app.config.update(config)

# Load environment variables
HOST = app.config.get("DB_HOST")
PORT = int(app.config.get("DB_PORT"))
USER = app.config.get("DB_USER")
PWD = app.config.get("DB_PWD")
DB = app.config.get("DB_NAME")



connection = pymysql.connect(

    host=HOST,
    user=USER,
    password=PWD,
    database=DB,
    port=PORT,
    cursorclass=pymysql.cursors.DictCursor)

