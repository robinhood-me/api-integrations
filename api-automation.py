import requests

# Example: API endpoints of two applications
API_APP1 = "https://jsonplaceholder.typicode.com/posts"
API_APP2 = "https://jsonplaceholder.typicode.com/comments"

def fetch_data_from_app1():
    """Fetch data from the first application (mocked API)."""
    response = requests.get(API_APP1)
    if response.status_code == 200:
        print("Data fetched successfully from App1:")
        return response.json()[:3]  # Get first 3 results for brevity
    else:
        print("Failed to fetch data from App1")
        return []

def send_data_to_app2(data):
    """Send data to the second application (mocked API)."""
    for item in data:
        response = requests.post(API_APP2, json=item)
        if response.status_code == 201:
            print(f"Data sent to App2 successfully: {item}")
        else:
            print(f"Failed to send data to App2: {item}")

if __name__ == "__main__":
    print("Starting API Automation...")
    data = fetch_data_from_app1()
    if data:
        send_data_to_app2(data)
    print("API Automation completed!")

