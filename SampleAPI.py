#import requests module for accessing online APIs data
import requests
import datetime as dt

#API URL for fetching information from web server
Base_url='https://api.open-meteo.com/v1/forecast?latitude=19.07&longitude=72.88&hourly=temperature_2m,apparent_temperature,temperature_80m,temperature_120m&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset&current_weather=true&forecast_days=1&timezone=auto'

#Create object to store response from server
response=requests.get(Base_url).json()

#print the object response for all content recieved in form of dictionary
#make the line 13 as a non comment to view all data:
#print(response)

#print sepcific data using dictionary key for specific values
print("Timezone = ",response.get('timezone'))
temp=response.get('daily')
print("Maximum teperature today = ",temp.get('temperature_2m_max')[0],'°C')