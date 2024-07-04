import os
import pandas as pd
import kaggle
from sqlalchemy.orm import Session
from backend.models import Restaurant, engine
from zipfile import ZipFile

# data = pd.read_csv('C:/Users/N YASWANTH KUMAR/OneDrive/Desktop/Zomato Data/zomato.csv', encoding='ISO-8859-1')
# print(data.head())

os.environ['KAGGLE_USERNAME'] = 'nillayaswanth'
os.environ['KAGGLE_KEY'] = '05309ee629f47c056f5f0a6573c997cc'

dataset = 'shrutimehta/zomato-restaurants-data'
kaggle.api.dataset_download_files(dataset, path='.', unzip=True)

data_file = 'zomato.csv'  
df = pd.read_csv(data_file, encoding='ISO-8859-1')
print(df.head())
os.remove(data_file)



with Session(engine) as session:
    for index, row in df.iterrows():
        restaurant = Restaurant(
            Restaurant_ID = row['Restaurant ID'],
            Restaurant_Name = row['Restaurant Name'],
            Country_Code = row['Country Code'],
            City = row['City'],
            Address = row['Address'],
            Locality = row['Locality'],
            Locality_Verbose = row['Locality Verbose'],
            Longitude = row['Longitude'],
            Latitude = row['Latitude'],
            Cuisines = row['Cuisines'],
            Average_Cost_for_two =  row['Average Cost for two'],
            Currency = row['Currency'],
            Has_Table_booking = row['Has Table booking'],
            Has_Online_delivery = row['Has Online delivery'],
            Is_delivering_now = row['Is delivering now'],
            Switch_to_order_menu = row['Switch to order menu'],
            Price_range = row['Price range'],
            Aggregate_rating = row['Aggregate rating'],
            Rating_color = row['Rating color'],
            Rating_text = row['Rating text'],
            Votes = row['Votes'],
        )
        session.add(restaurant)
    session.commit()
