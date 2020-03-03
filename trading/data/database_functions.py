import psycopg2
import psycopg2.extras
from trading.data.config import config


def create_table():
    commands = ("""
        CREATE TABLE IF NOT EXISTS stockslist (
            id SERIAL PRIMARY KEY,
            rates TEXT[1] 
        )
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(commands)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def drop_table():
    commands = ("""
        DROP TABLE IF EXISTS stockslist 
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(commands)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_rates(rates):
    sql = """ INSERT INTO stockslist(rates) VALUES (%(rates)s) """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, rates)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_rates():
    sql = """SELECT rates FROM stockslist ORDER BY id DESC LIMIT 1 """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        rates_arr = cur.fetchone()
        cur.close()
        return rates_arr
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
