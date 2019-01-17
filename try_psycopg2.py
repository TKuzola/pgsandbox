import psycopg2


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="777999Pg")

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()




        cur1 = conn.cursor()
        id = '4'
        mes1 = 'Forth entry'
        mes2 = 'SQLAlchemy test message'
        sql1 = f"INSERT INTO test.test_log2(message_id, message1, message2) VALUES({id},'{mes1}','{mes2}')"
        cur1.execute(sql1)

        conn.commit()
        cur1.close()


        cur2 = conn.cursor()
        cur2.execute("SELECT message_id, message1, message2 FROM test.test_log2")
        print("The number of log entries: ", cur2.rowcount)
        row = cur2.fetchone()

        while row is not None:
            print(row)
            row = cur2.fetchone()

        cur2.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
