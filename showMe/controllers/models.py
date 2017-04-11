from showMe import db


class logs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    icon = db.Column(db.String(120), unique=False)
    path = db.Column(db.String(120), unique=True)

    def __init__(self, name, logo, path):
        self.name = name
        self.logo = logo
        self.path = path

    def __repr__(self):
        return '<logs %r>' % self.name