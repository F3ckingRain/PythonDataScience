from wwo_hist import retrieve_hist_data
import os

os.chdir(".\\data")
frequency = 24
start_date = '01-JAN-2021'
end_date = '01-JAN-2022'
API_KEY = '5a2702f8940c42c9ad360622221502'
location_list = ['death_valley']
hist_weather_data = retrieve_hist_data(API_KEY,location_list,start_date,end_date,frequency,location_label=False,export_csv=True,store_df=True)