import psycopg2
from sqlalchemy import Column, String, Integer
from base import Base
from base import Session


class TestLog2(Base):
    __tablename__ = 'test_log2'
    message_id = Column(Integer, primary_key=True)
    message1 = Column(String(20))
    message2 = Column(String(40))

    def __init__(self, message_id, message1, message2):
        self.message_id = message_id
        self.message1 = message1
        self.message2 = message2


def connect():

    try:



    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        print('goodbye.')


if __name__ == '__main__':
    connect()
