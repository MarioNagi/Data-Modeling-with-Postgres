import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
from sql_queries import create_table_queries, drop_table_queries

host = os.environ.get("host")
database = os.environ.get("database")
user = os.environ.get("user")
password = os.environ.get("password")

def create_database():
    """
    - Creates and connects to the aws sparkifydb
    - Returns the connection and cursor to aws sparkifydb
    """
    
    # connect to default database
    conn = psycopg2.connect(f"host={host} dbname=postgres user={user} password={password}")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect(f"host={host} dbname={database} user={user} password={password}")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()