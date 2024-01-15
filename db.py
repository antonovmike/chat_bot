from sqlalchemy import Column, Integer, String, DateTime, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:123@localhost/test_bot')
Session = sessionmaker(bind=engine)
session = Session()
base = declarative_base()


class User(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    telegram_id = Column(String)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    registration_date = Column(DateTime, default=func.now())


class Report(base):
    __tablename__ = 'report'

    id = Column(Integer, primary_key=True)
    user_message = Column(String)
    gpt_message = Column(String)
    gpt_response_time = Column(String)
    message_date_time = Column(DateTime, default=func.now())


base.metadata.create_all(engine)
