import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from .db import Base
from .db import ENGINE

class Tweet(Base):
    """
    Tweetモデル
    """
    __tablename__ = 'tweet'
    id = Column('id', Integer, primary_key = True)
    tid = Column('tid', String)
    user = Column('user', String)
    screen_name = Column('screen_name', String)
    url = Column('url', String)
    created_date = Column('created_date', DateTime)
    post_status = Column('post_status', String(1))

    def main(self):
        """
        メイン関数
        """
        Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
    main()