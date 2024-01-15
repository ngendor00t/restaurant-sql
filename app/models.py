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
    
    
    def __repr__(self):
        return f'Customer(id={self.id}, ' + \
            f'first name="{self.first_name}", ' + \
            f'last name="{self.last_name})"'


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))

    restaurant = relationship('Restaurant', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')
    def __repr__(self):
        return f'RestaurantCustomers(restaurant_id={self.restaurant_id}, ' +\
            f'customer_id={self.customer_id})'
  