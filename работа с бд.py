import psycopg2
from config import *
conn = psycopg2.connect(database="diplom", user="postgres", password="veronika")

with conn.cursor() as cur:
    cur.execute(
        """CREATE TABLE IF NOT EXISTS user(
                id SERIAL PRIMARY KEY,
                vk_link varchar,
                age INTEGER,
                gender VARCHAR,
                city VARCHAR,
                family_status VARCHAR);"""
            )

with conn.cursor() as cur:
    cur.execute("INSERT INTO user (vk_link,age, gender, city, family_status)"
                "VALUES('{vk_link}','{age}', '{gender}', '{city}', '{family_status}')");
    conn.close()


with conn.cursor() as cur:
    cur.execute(
        """CREATE TABLE IF NOT EXISTS seen_users(
        id serial,
        vk_id varchar(50) PRIMARY KEY);"""
    );


with conn.cursor() as cur:
    cur.execute("INSERT INTO seen_users (vk_id)"
        "VALUES ('{vk_id}')"
    );

def select(offset):
    with conn.cursor() as cur:
        cur.execute(
            f"""SELECT u.first_name,
                        u.last_name,
                        u.vk_id,
                        u.vk_link,
                        su.vk_id
                        FROM users AS u
                        LEFT JOIN seen_users AS su 
                        ON u.vk_id = su.vk_id
                        WHERE su.vk_id IS NULL
                        OFFSET '{offset}';"""
        )
        return cur.fetchone()

