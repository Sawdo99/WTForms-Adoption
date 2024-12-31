from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Models ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class adopt(db.Model):
    __tablename__ = 'adopt'
        
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String, nullable=False)
    age = db.Column(db.Integar, nullable=False)
    notes = db.Column(db.String, nullable=False)
    available = db.Column(db.Boolean, nullable=False, default=True)


