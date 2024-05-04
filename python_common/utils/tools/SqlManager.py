from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import scoped_session, sessionmaker


class SqlManager:
    def __init__(self, mysql_host, mysql_user, mysql_password, mysql_database):
        self.mysql_host = mysql_host
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_database = mysql_database
        self.engine = None

    class Base(DeclarativeBase):
        pass

    def create_engine(self):
        self.engine = create_engine(
            f"mysql+pymysql://{self.mysql_user}:{self.mysql_password}@{self.mysql_host}/{self.mysql_database}",
            echo=True
        )
        return self

    # 在原数据库中新建映射类对应的表
    def create_table(self):
        self.Base.metadata.create_all(self.engine)

    def drop_table(self):
        self.Base.metadata.drop_all(self.engine)

    def get_session(self):
        return scoped_session(sessionmaker(bind=self.engine, autocommit=False, autoflush=True))
