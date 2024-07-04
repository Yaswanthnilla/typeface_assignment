from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'zomato_data'
    
    Restaurant_ID = Column(Integer, primary_key=True, index=True)
    Restaurant_Name = Column(String, index=True)
    Country_Code = Column(Integer)
    City = Column(String)
    Address = Column(String)
    Locality = Column(String)
    Locality_Verbose = Column(String)
    Longitude = Column(Integer)
    Latitude = Column(Integer)
    Cuisines = Column(String)
    Average_Cost_for_two =  Column(Integer)
    Currency = Column(String)
    Has_Table_booking = Column(String)
    Has_Online_delivery = Column(String)
    Is_delivering_now = Column(String)
    Switch_to_order_menu = Column(String)
    Price_range = Column(Integer)
    Aggregate_rating = Column(Integer)
    Rating_color = Column(String)
    Rating_text = Column(String)
    Votes = Column(Integer)

    def to_dict(self):
        return {
            'id': self.Restaurant_ID,
            'name': self.Restaurant_Name,
            'cuisine': self.Cuisines,
            'address': self.Address,
            'country_code':self.Country_Code,
            'city':self.City,
            'locality':self.Locality,
            'longitude':self.Longitude,
            'latitude':self.Latitude,
            'locality_verbose':self.Locality_Verbose,
            'avg_cost_for_two':self.Average_Cost_for_two,
            'has_online_delivery':self.Has_Online_delivery,
            'has_table_booking':self.Has_Table_booking,
            'currency':self.Currency,
            'is_delivering_now':self.Is_delivering_now,
            'switch_to_order_menu':self.Switch_to_order_menu,
            'price_range':self.Price_range,
            'rating':self.Aggregate_rating,
            'votes':self.Votes,
            'rating_color':self.Rating_color,
            'rating_text':self.Rating_text
        }


DATABASE_URL = "postgresql://postgres:1234567890@localhost:5432/zomato"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
