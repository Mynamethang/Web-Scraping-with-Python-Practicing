import psycopg2
from sql_queris import *


def connect_postgres():
    #connect to postgresSQL
    conn = psycopg2.connect("host=localhost dbname=firstdb user=postgres password=12345678")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    return cur, conn

def create_table(cur, conn):
    #drop table if exists
    cur.execute(drop_largest_companies_table)
    conn.commit()
    #create table
    cur.execute(create_largest_companies_table)
    conn.commit()

def main():
    cur, conn = connect_postgres()
    create_table(cur, conn)
    print("create table succesfully!")

    conn.close()
    cur.close()

if __name__ == "__main__":
    main()

    