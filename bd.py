import psycopg2
from token import *
conn = psycopg2.connect(database="diplom", user="user", password="password")

with conn.cursor() as cur:
    cur.execute(
        """CREATE TABLE IF NOT EXISTS user(
                user_id SERIAL PRIMARY KEY,
                see_user_id SERIAL);"""
            )

with conn.cursor() as cur:
    cur.execute("INSERT INTO user (user_id,see_user_id )"
                "VALUES('{user_id}','{see_user_id}')");
    conn.close()




