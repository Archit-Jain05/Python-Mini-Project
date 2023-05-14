import requests
from PIL import Image
import io
from io import BytesIO

# Set the API endpoint URL and parameters
url2 = "https://newsapi.org/v2/top-headlines"
url="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=a08812eb06cb461197c118b8555a3dd0"
params = {
    "country": "us",
    "categories":"sports",
    "apiKey": "a08812eb06cb461197c118b8555a3dd0"
}

# Make the API request and get the response
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Extract the articles from the response
    articles = response.json()["articles"]
    
    # Loop through the articles and print the titles and images
    for article in articles:
        title = article["title"]
        image_url = article["urlToImage"]
        
        # Print the title
        print(title)
        
        # Check if the article has an image
        if image_url:
            # Load the image from the URL
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            
            # Display the image
            img.show()
        else:
            print("No image available.")
            
        print("\n")
else:
    print("Error: Could not retrieve news.")
