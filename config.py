import os

class Config:
    SECRET_KEY = 'Hello_WorldIDKWHATTOPUTELSE'
    
    # MySQL settings (Laragon defaults: root, no password, 127.0.0.1:3306)
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DATABASE = 'ota_flask_iot'
    MYSQL_PORT = 3306
    
    # Upload folder for firmware binaries
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'firmware')
    
    # Max upload size (e.g., 16 MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
