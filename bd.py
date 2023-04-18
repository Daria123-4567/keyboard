import psycopg2

conn = psycopg2.connect(database="diplom", user="veronika", password="veronika")


def create_table_users():
    with conn.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
                    user_id SERIAL PRIMARY KEY,
                    see_user_id SERIAL);"""
        )


def insert_into_users():
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO user (user_id,see_user_id )"
                       "VALUES('{user_id}','{see_user_id}')"
                       )
        conn.close()

        for row in cursor.execute("SELECT user_id, FROM insert_into_users"):
            user_id = row
            break
        else:
            print("not found")
