from sqlalchemy import Column, Integer, String ,ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,backref

engine = create_engine('sqlite:///restaurant.db')

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer(), primary_key=True)
    name = Column(String)
    price = Column(Integer)

    reviews = relationship('Review', back_populates='restaurant')
    restaurant_customers = relationship('RestaurantCustomers', back_populates='restaurant')
     
    def __repr__(self):
        return f'Restaurant(id={self.id}, ' + \
            f'name="{self.name}", ' + \
            f'price="{self.price})"'


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', back_populates='customer')
    restaurant_customers = relationship('RestaurantCustomers', back_populates='customer')