import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the SHL product catalog
url = "https://www.shl.com/solutions/products/product-catalog/"

def scrape_shl_catalog(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the relevant data on the page
    # This part will depend on the structure of the SHL catalog page
    # For example, you might look for specific HTML tags or classes

    # Example: Find all product entries
    products = soup.find_all('div', class_='product-entry')  # Adjust the class name as needed

    # Extract data and store it in a list
    data = []
    for product in products:
        name_tag = product.find('h2')  # Adjust the tag as needed
        link_tag = product.find('a', href=True)

        if name_tag and link_tag:
            name = name_tag.text.strip()
            link = link_tag['href']
            # Add more fields as necessary
            data.append({
                'name': name,
                'url': link,
                # Add more fields here
            })

    # Convert the list to a DataFrame
    df = pd.DataFrame(data)
    return df

# Scrape the catalog and save it to a CSV file
df = scrape_shl_catalog(url)
if df is not None:
    df.to_csv('shl_assessments.csv', index=False)
    print("Data saved to shl_assessments.csv")
else:
    print("No data was scraped.")