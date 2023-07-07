import psycopg2
from PostgreSQL15.orm import Session

conn = psycopg2.connect(database="diplom", user="veronika", password="veronika")


def create_table_users():
    with conn.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
                    user_id SERIAL PRIMARY KEY,
                    see_user_id SERIAL);"""
        )


def insert_into_users(engine, user_id, see_user_id):
    with Session(engine) as session:
        to_bd = Users(user_id=user_id, see_user_id=see_user_id)
        session.add(to_bd)
        session.commit()


def check_users(engine, user_id, see_user_id):
    with Session(engine) as session:
        from_bd = session.query(Users).filter(
            Users.user_id == user_id,
            Users.see_user_id == see_user_id
        ).first()
        return True if from_bd else False

