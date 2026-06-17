from flask import Blueprint , Flask , render_template , request , redirect , url_for , flash , session
from db import get_db

auth_bp = Blueprint("auth" , __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username,password))
        user_data = cursor.fetchone()
        
        if not user_data:
            flash("Invalid username or password")
            cursor.close()
            db.close()
            return render_template
            
        session["username"] = user_data["username"]
        session["user_id"] = user_data["id"]
        cursor.close()
        db.close()
        flash("Login successful!")
        return render_template("dashboard.html")

    return render_template("login.html")