import requests #import the requests library

city = input("Enter City Name: ") #driver input

api_key = "671a8dbc1a8a98a6f6663efccee42ba0" #API key 

url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=671a8dbc1a8a98a6f6663efccee42ba0&units=metric".format(city) #required url

response = requests.get(url) #API calling 

if response.status_code == 200: #status code if code pass successfully

    temperature = response.json()  # temp requested from API
    
    temp = temperature["main"]["temp"] #calling for temperature, other can be wind_speed , lat etc...

    print("The Temperature in "+ city +" is--->",temp)  #output

else:
    print('ERROR:',response.status_code) #status code in case of error
