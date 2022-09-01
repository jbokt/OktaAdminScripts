import sys              # For parsing arguments
import csv              # For loading CSV file
import requests, json   # For API calls
import os, dotenv       # For loading environment variables from .env file


# Load environment variables
dotenv.load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
OKTA_DOMAIN = os.getenv('OKTA_DOMAIN')

# Set up API endpoints
CHECK_USERNAMES_ENDPOINT = f'https://{OKTA_DOMAIN}/api/v1/users/'

# Parse arguments
args = sys.argv[1:]

# Check if arguments are correct
if len(args) != 1:
    print("Usage: check_users.py <csv_file_path>")
    sys.exit(1)

# Read command line arguments
csv_file_path = args[0]

# Open CSV File and read the data
with open(csv_file_path, 'r') as csv_file: 
    # Check if file is valid, otherwise quit
    try: 
        csv_reader = csv.reader(csv_file)
    except: 
        print("Error: Could not read CSV file")
        sys.exit(1)

    usernames = [row[0] for row in csv_reader]

# Iterate over all users in the CSV file
# First slot in row should be username
responses = {}
for username in usernames: 
    response = requests.get(CHECK_USERNAMES_ENDPOINT + username, headers={'Authorization': f'SSWS {API_TOKEN}'})

    try: 
        print(f"User {username} has status: {response.json()['status']}")
        responses[username] = response.json()['status']
    except:
        print(f"Error: Could not get status for user {username}")
        responses[username] = "ERROR"

# Store reponse in CSV
with open('responses.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    for username, status in responses.items():
        csv_writer.writerow([username, status])

