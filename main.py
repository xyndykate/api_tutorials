import requests  # Import the requests library to make HTTP requests

def get_stock_data():
    # Define the API endpoint URL for fetching IBM stock data
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Get the timestamp of the last refreshed data
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        # Get the opening price for the last refreshed timestamp
        price = data["Time Series (5min)"][last_refreshed]["1. open"]
        return price
    else:
        # Return None if the request failed
        return None

price = get_stock_data()  # Fetch the latest stock price
symbol = "IBM"  # Define the stock symbol
if price is not None:
    # Print the stock symbol and price if data was retrieved
    print(f"{symbol}: {price}")
else:
    # Print an error message if data retrieval failed
    print("Failed to retrieve data.")