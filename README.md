# Python Scripts to help with Everyday Admin Tasks

## Install dependencies
To install the necessary requirements to run the scripts you should run the following command (assuming you got python3 with pip installed):
```py
pip install -r requirements.txt
```

## Usage
CSV-file: The CSV-file can have any format, as long as the username is always in the first (0) index

## Add users to group from CSV
Run the following command in the root directory to add users to the group: 
```py
python add_users.py <csv_path> <group_id>
```
This command will output the result of the call to the command line.

- Import file should be called users.csv
- This script will convert username/email to Unique user ID, which is required to add users to a group via API

## Check user state/status from a CSV

Run the following command in the root directory:
```py
python check_users.py <csv_path>
```
This command will produce a repsonses.csv file, and will log the results to the command line

- Import file should be called users.csv
