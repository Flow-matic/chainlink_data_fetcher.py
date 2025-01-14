import requests

# Replace with your actual API URLs and authentication details
bnbusd_api_url = "https://api.chainlink.io/v2/jobs/actual_bnbusd_job_id/runs"  # Replace with the actual job ID for BNB
api_key = "your_api_key_here"  # Replace with your API key or token

# Request headers for authentication
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Request parameters
params = {
    "status": "completed",
    "size": "1",  # Ensure parameters are strings
}

def fetch_chainlink_data(api_url, params):
    """
    Fetches the latest data point from the specified Chainlink API endpoint.

    Args:
        api_url: The URL of the Chainlink API endpoint.
        params: The parameters to be sent in the request.

    Returns:
        A dictionary containing the extracted data, or None if no data is found.
    """
    try:
        # Send the GET request with parameters and headers
        response = requests.get(api_url, params=params, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP errors (4xx/5xx)

        # Parse the response JSON
        data = response.json()

        # Check if the response contains data
        if "data" in data and data["data"]:
            latest_data_point = data["data"][0]
            # Extract the desired data point (e.g., 'result')
            extracted_data = latest_data_point.get("result", None)
            return extracted_data
        else:
            print(f"No data found in the Chainlink API response for {api_url}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Chainlink API: {e}")
        return None

if __name__ == "__main__":
    # Fetch data for BNBUSD only
    bnbusd_price = fetch_chainlink_data(bnbusd_api_url, params)

    # Print the price if it was successfully retrieved
    if bnbusd_price is not None:
        print(f"BNBUSD Price: {bnbusd_price}")
    else:
        print("Failed to retrieve BNBUSD price.")
