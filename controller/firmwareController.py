from flask import Blueprint , Flask , render_template , request , redirect , url_for , flash , session
from db import get_db
from werkzeug.utils import secure_filename
import time , os
from config import Config

firmware_bp = Blueprint("firmware", __name__,url_prefix="/firmware")

@firmware_bp.route("/api/firmware/latest", methods=["GET"])
def get_latest_firmware():
    device_type = request.args.get('device', 'esp32')
    
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM firmware WHERE device_type = %s ORDER BY uploaded_at DESC LIMIT 1",
        (device_type,)
    )
    latest = cursor.fetchone()
    cursor.close()
    db.close()
    
    if not latest:
        return jsonify({"error": "No firmware found"}), 404
        
    # Build full URL for the binary
    download_url = request.host_url.rstrip('/') + url_for('static', filename=f"firmware/{latest['filename']}")
    
    return jsonify({
        "version": latest['version'],
        "url": download_url,
        "device_type": latest['device_type']
    })
    
@firmware_bp.route("/upload",methods=["GET","POST"])
def upload():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    if request.method == "POST":
        version = request.form.get("version")
        device_type = request.form.get("device_type","esp-32")
        file = request.files.get("file")
        
        if not version or not file or file.filename == '':
            flash('No .bin file selected or file missing!')
            return redirect(request.url)
        if not file.filename.endwith('.bin'):
            flash('Only .bin file is allowed for firmware')
            return redirect(request.url)
        filename = secure_filename(f"{device_type}_{version}_{int(time.time)}.bin")
        filename = os.path.join(Config.UPLOAD_FOLDER)
        file.save(filepath)
        
        cursor.execute("INSERT INTO firmware(version , filename, device_type) VALUES(%s , %s , %s)", (version,filename,device_type))
        db.commit()
        flash("Firmware has been updated")
        return redirect("/dashboard")
    cursor.execute("SELECT * FROM firmware ORDER BY uploading_at DESC")
    firmwares = cursor.fetchall()
    cursor.close()
    db.close()
    
    return render_template("dashboard.html", firmwares=firmwares)