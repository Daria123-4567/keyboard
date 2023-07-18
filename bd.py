import psycopg2
import sqlalchemy as sq
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base


conn = psycopg2.connect(database="diplom", user="veronika", password="veronika")
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    user_id = sq.Column(sq.Integer, primary_key=True)
    see_user_id = sq.Column(sq.Integer, primary_key=True)

    def insert_into_users(self, user_id, see_user_id):
        with Session(self) as session:
            to_bd = Users(user_id=user_id, see_user_id=see_user_id)
            session.add(to_bd)
            session.commit()

    def check_users(self, user_id, see_user_id):
        with Session(self) as session:
            from_bd = session.query(Users).filter(
                Users.user_id == user_id,
                Users.see_user_id == see_user_id
            ).first()
            return True if from_bd else False

