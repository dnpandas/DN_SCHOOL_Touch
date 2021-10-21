# connection_project


import psycopg2
from project_dbconfig import read_db_configuration


def connection():
    """ Connection to PostgreSQL Server """
    conn = None
    try:
        # Reads Parameters connection
        parameter = read_db_configuration()

        # connect to PG SQL Server
        print("Connection to PG SQL")
        conn = psycopg2.connect(**parameter)

        # Create Cursor object
        cur = conn.cursor()

        # Execute statement SELECT
        print("PG DB VER: ")
        cur.execute('SELECT version()')

        # Display PG DB Version.
        versi_db = cur.fetchone()
        print(versi_db)

        # Close connection with PG Server
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is None:
            return
            conn.close()
            print("Connection to PG DB is CLOSED.")


if __name__ == '__main__':
    connection()
