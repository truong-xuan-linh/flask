from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    # https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
    id = db.Column(db.Integer, primary_key=True)
    HoTen = db.Column(db.String(255))
    SoDienThoai = db.Column(db.String(255))
    LoaiXe = db.Column(db.String(255))
    BienSoXe = db.Column(db.String(255))
    CongTy = db.Column(db.String(255))
    DiaChi = db.Column(db.String(255))
    BPCanGap = db.Column(db.String(255))
    NguoiCanGap = db.Column(db.String(255))
    MucDich = db.Column(db.String(255))
    HDAnToan = db.Column(db.Boolean)
    MaTheKhach = db.Column(db.String(255))
    GioVao = db.Column(db.DateTime)
    GioRa = db.Column(db.DateTime)
    
    def __init__(self, 
                HoTen,
                SoDienThoai,
                LoaiXe,
                BienSoXe,
                CongTy,
                DiaChi,
                BPCanGap,
                NguoiCanGap,
                MucDich,
                HDAnToan,
                MaTheKhach,
                GioVao,
                GioRa,
                ) -> None:
        super().__init__()
        
        self.HoTen = HoTen
        self.SoDienThoai = SoDienThoai
        self.LoaiXe = LoaiXe
        self.BienSoXe = BienSoXe
        self.CongTy = CongTy
        self.DiaChi = DiaChi
        self.BPCanGap = BPCanGap
        self.NguoiCanGap = NguoiCanGap
        self.MucDich = MucDich
        self.HDAnToan = HDAnToan
        self.MaTheKhach = MaTheKhach
        self.GioVao = GioVao
        self.GioRa = GioRa