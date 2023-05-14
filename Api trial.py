import requests

# Set the API endpoint URL and parameters
url = "https://newsapi.org/v2/everything?"
url2="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=a08812eb06cb461197c118b8555a3dd0"
params = {
    "country": "in",
    "categories": "health",
    "apiKey": "a08812eb06cb461197c118b8555a3dd0"
}

# Make the API request and get the response
country="in"
category="technology"
furl=url+"?country="+country+"&categories="+category+"&apikey=a08812eb06cb461197c118b8555a3dd0"
response = requests.get(url2)

# Check if the request was successful
if response.status_code == 200:
    # Extract the articles from the response
    articles = response.json()["articles"]
    
    # Print the titles of the first 5 articles
    for article in articles[:5]:
        print(article["title"])
        print("\n")
else:
    print("Error: Could not retrieve news.")
