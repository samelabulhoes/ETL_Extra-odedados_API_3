import requests
import pandas as pd

# URL of the API
url = "https://example.com/api/produtos"

# Make a GET request to fetch the data from the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data from the response
    json_data = response.json()
    
    # Convert JSON data to a DataFrame
    df = pd.DataFrame(json_data)
    
    # Save the DataFrame to a CSV file
    df.to_csv('produtos.csv', index=False)
    
    print("Data saved to produtos.csv")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
