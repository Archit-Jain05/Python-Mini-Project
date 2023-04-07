import requests
import datetime as dt


Base_url='http://api.openweathermap.org/data/5/weather?appid=834ec3873c248ede6f80b9bfc00a6533&q=Mumbai'
API_key='834ec3873c248ede6f80b9bfc00a6533'
City='Mumbai'

#final_url=Base_url+"appid="+API_key+"&q="+City

response=requests.get(Base_url).json()

print(response)