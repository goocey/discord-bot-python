import yaml
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from ..settings import settings

"""
sqlalchemyのでDB接続周りを行うメソッド実行用ソース
"""

setting = settings.get_setting()
ENGINE = create_engine(
    setting['DATABASE'],
    encoding = setting['DATABASE_ENCODING'],
    echo=True # Trueだと実行のたびにSQLが出力される
)

# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するなど。
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()