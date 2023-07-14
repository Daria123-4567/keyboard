import psycopg2
from sqlalchemy.orm import Session

conn = psycopg2.connect(database="diplom", user="veronika", password="veronika")


def users():
    with conn.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
                    user_id SERIAL PRIMARY KEY,
                    see_user_id SERIAL);"""
        )


def insert_into_users(engine, user_id, see_user_id):
    with Session(engine) as session:
        to_bd = users(user_id=user_id, see_user_id=see_user_id)
        session.add(to_bd)
        session.commit()


def check_users(engine, user_id, see_user_id):
    with Session(engine) as session:
        from_bd = session.query(users).filter(
            users.user_id == user_id,
            users.see_user_id == see_user_id
        ).first()
        return True if from_bd else False

