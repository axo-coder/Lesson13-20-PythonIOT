from flask import Flask , request , render_template , Blueprint
from controller.auth_controller import auth_bp
from config import Config
from controller.firmwareController import firmware_bp

app = Flask(__name__)
app.register_blueprint(auth_bp)
app.register_blueprint(firmware_bp)
app.secret_key = Config.SECRET_KEY

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True,port=5500, host="0.0.0.0")