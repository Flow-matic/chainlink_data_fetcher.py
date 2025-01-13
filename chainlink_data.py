import requests

# Replace with your actual Chainlink API endpoints and parameters
bnbusd_api_url = "https://api.chainlink.io/v2/jobs/your_bnbusd_job_id/runs"  # Replace with actual job ID
cakeusd_api_url = "https://api.chainlink.io/v2/jobs/your_cakeusd_job_id/runs"  # Replace with actual job ID
params = {
    "status": "completed",
    "size": 1,
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
        # Print the params dictionary for debugging
        print(params)

        # Ensure all values in params are strings
        for key, value in params.items():
            if not isinstance(value, str):
                params[key] = str(value)

        # Send the GET request with parameters
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Will raise an error for 4xx/5xx status codes

        # Get the response as JSON
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
    # Fetch data for BNBUSD and CAKEUSD
    bnbusd_price = fetch_chainlink_data(bnbusd_api_url, params)
    cakeusd_price = fetch_chainlink_data(cakeusd_api_url, params)

    # Print the prices if they were successfully retrieved
    if bnbusd_price and cakeusd_price:
        print(f"BNBUSD Price: {bnbusd_price}")
        print(f"CAKEUSD Price: {cakeusd_price}")
    else:
        print("Failed to retrieve one or both prices from Chainlink.")
