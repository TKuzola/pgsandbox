import psycopg2
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker


def connect():
    
    try:
        engine = db.create_engine("postgresql://postgres:777999Pg@localhost:5432/postgres")
        engine.echo = True  # We want to see the SQL we're creating
        connection = engine.connect()
        metadata = db.MetaData()
        log2 = db.Table('test_log2', metadata, autoload=True, autoload_with=engine, schema='test')

        # Print the column names
        # print(log2.columns.keys())

        # Print full table metadata
        # print(repr(metadata.tables['log2']))

        Session = sessionmaker(bind=engine)
        # Equivalent to 'SELECT * FROM log2'
        work_session = Session()
        for instance in work_session.query(log2):
             print(instance.message_id, instance.message1, instance.message2)


    except Exception as e:
        # handle exception "e", or re-raise appropriately.
        print(e)
    finally:
        print('goodbye.')


if __name__ == '__main__':
    connect()
