from db import db


class JokeModel(db.Model):
    __tablename__ = "Jokes"

    id = db.Column(db.Integer, primary_key=True)
    joke = db.Column(db.String, unique=False, nullable=False)

    def json(self):
        return {
            "id": self.id,
            "joke": self.joke,
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
