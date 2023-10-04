
from flask import Flask, redirect, url_for, render_template, request, flash, Response

import os
import datetime

from database import db, User

app = Flask(__name__)
app.secret_key = "haha"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

        
@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        print(request.form)
        name = request.form["name"]
        number = request.form["number"]
        vehicle_type = request.form["vehicle_type"]
        vehicle_number = request.form["vehicle_number"]
        company_name = request.form["company_name"]
        address = request.form["address"]
        department = request.form["department"]
        who = request.form["who"]
        target = request.form["target"]
        instructions = bool(request.form.get("instructions", False))
        id_card = request.form["id_card"]
        time_in = datetime.datetime.fromisoformat(request.form["time_in"])
        time_out = datetime.datetime.fromisoformat(request.form["time_out"]) if request.form["time_out"] else None
        
        if name and number:
            exists_user = User.query.filter_by(MaTheKhach=id_card).first()
            
            if not exists_user:
                user = User(name,
                            number,
                            vehicle_type,
                            vehicle_number,
                            company_name,
                            address,
                            department,
                            who,
                            target,
                            instructions,
                            id_card,
                            time_in,
                            time_out)
                db.session.add(user)
                db.session.commit()
                print("INSERTED")
            else:
                exists_user.HoTen = name 
                exists_user.SoDienThoai = number 
                exists_user.LoaiXe = vehicle_type 
                exists_user.BienSoXe = vehicle_number 
                exists_user.CongTy = company_name 
                exists_user.DiaChi = address 
                exists_user.BPCanGap = department 
                exists_user.NguoiCanGap = who 
                exists_user.MucDich = target 
                exists_user.HDAnToan = instructions 
                exists_user.MaTheKhach = id_card 
                exists_user.GioVao = time_in 
                exists_user.GioRa = time_out 
                db.session.commit()
                print("UPDATED")
            return redirect(url_for("success_page", name=name))
        
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template("edit_profile.html", current_time=current_time)

@app.route("/success/<name>", methods=["GET", "POST"])
def success_page(name):
    if request.method == "POST":
        print(request.form["back_home_button"])
        if request.form["back_home_button"] == "back":
            return redirect(url_for("home_page"))
        
    return render_template("success.html")

with app.app_context():
    if not os.path.exists("instance/user.db"):
        db.create_all()
        print("CREATED DB")
    app.run(debug=True, port=5001)