from app import db

class User(db.Model):
    __tablename__ = 'user_data'
  
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(255))
  
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @staticmethod
    def create(username, password):
        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()
