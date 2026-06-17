import mysql.connector
from flask import current_app
from config import Config

def get_db(app_instance=None):
    
    db = mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DATABASE,
        port=Config.MYSQL_PORT
    )
    return db