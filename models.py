# ----------------------------
# REFERENCE FOR sqlalchemy MAPPINGS...
# https://docs.sqlalchemy.org/en/13/orm/mapping_styles.html
# ----------------------------

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ParseResult(Base):
    __tablename__ = 'parse_result'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column('id', Integer, primary_key=True)
    parent_id = Column('parent_id', Integer)
    org_id = Column('org_id', Integer,  ForeignKey("organization.id"))
    url = Column('url', String)
    level = Column('level', Integer)
    title = Column('title', String)
    keywords = Column('keywords', String)
    description = Column('description', String)
    h1 = Column('h1', String)
    h2 = Column('h2', String)
    h3 = Column('h3', String)
    content = Column('content', String)
    created_date = Column('created_date', DateTime(timezone=True), server_default=func.now())
    scan_date = Column('scan_date', DateTime)

    def __repr__(self):
        return f'ParseResult(id=\'{self.id}\', parent_id=\'{self.parent_id}\', org_id=\'{self.org_id}\', url=\'{self.url}\', level=\'{self.level}\', title=\'{self.title}\', keywords=\'{self.keywords}\', description=\'{self.description}\', h1=\'{self.h1}\', h2=\'{self.h2}\', h3=\'{self.h3}\', content=\'{self.content}\', created_date=\'{self.created_date}\', scan_date=\'{self.scan_date}\')'

    def __str__(self):
        return f'id[{self.id}] parent_id[{self.parent_id}] org_id[{self.org_id}] url[{self.url}] created_date[{self.created_date}]'

class JsonResult():
    url = None
    rank = None

if __name__ == '__main__':
	print('this is not a runable script')
