import sys              # For parsing arguments
import csv              # For loading CSV file
import requests, json   # For API calls
import os, dotenv       # For loading environment variables from .env file


# Load environment variables
dotenv.load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
OKTA_DOMAIN = os.getenv('OKTA_DOMAIN')

# Set up API endpoints
ADD_USERNAME_TO_GROUP_ENDPOINT = 'https://OKTA_DOMAIN/api/v1/groups/{}/users/{}'.replace("OKTA_DOMAIN", OKTA_DOMAIN)
GET_USER_ID_ENDPOINT = 'https://OKTA_DOMAIN/api/v1/users/{}'.replace("OKTA_DOMAIN", OKTA_DOMAIN)

# Parse arguments
args = sys.argv[1:]

# Check if arguments are correct
if len(args) != 2:
    print("Usage: add_users.py <csv_file_path> <group_id>")
    sys.exit(1)

# Read command line arguments
csv_file_path = args[0]
group_id = args[1]

def getUserIdFromEmail(userMail):
    # Get user ID from email
    response = requests.get(GET_USER_ID_ENDPOINT.format(userMail), headers={'Authorization': 'SSWS {}'.format(API_TOKEN)})
    if response.status_code != 200:
        print("Error: Could not get user ID for {}".format(userMail))
        return None
    return response.json()['id']

# Open CSV File and read the data
with open(csv_file_path, 'r') as csv_file: 
    # Check if file is valid, otherwise quit
    try: 
        csv_reader = csv.reader(csv_file)
    except: 
        print("Error: Could not read CSV file")
        sys.exit(1)

    # Iterate over all users in the CSV file
    # First slot in row should be username
    for row in csv_reader: 
        user_id = getUserIdFromEmail(row[0])
        if user_id is None:
            print(f"User {row[0]} not found")
            continue
        response = requests.put(ADD_USERNAME_TO_GROUP_ENDPOINT.format(group_id, user_id), headers={'Authorization': f'SSWS {API_TOKEN}'})
        if response.status_code != 204: 
            print(f"Could not add user: {row[0]} to group: {group_id}: {response.json()['errorSummary']}")
            continue
        print(f"Added user: {row[0]} to group: {group_id}")



