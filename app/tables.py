from datetime import datetime
from sqlalchemy import create_engine, desc, CheckConstraint, PrimaryKeyConstraint, UniqueConstraint, Index, Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Review(Base):
    __tablename__ = 'reviews'
    __table_args__ = (
        PrimaryKeyConstraint('id'),
        UniqueConstraint('star_rating')
    )

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    def __repr__(self):
        return f"restaurant {self.id}: {self.name}, price={self.price}"

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return f"customer {self.id}: {self.first_name}, {self.last_name}"

if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
