from . import db


class Documents(db.Model):
    """Модель документа"""

    __tablename__ = 'documents'
    id = db.Column(db.Integer, primary_key=True)
    rubrics = db.Column(db.JSON)
    text = db.Column(db.String(255))
    created_date = db.Column(db.DateTime)
