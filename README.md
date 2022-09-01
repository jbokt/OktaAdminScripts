# OktaAdminScripts
Python Scripts to help with Everyday Admin Tasks


Install dependencies
To install the necessary requirements to run the scripts you should run the following command (assuming you
got python3 with pip installed):
pip install -r requirements.txt

Usage
CSV-file:
The CSV-file can have any format, as long as the username is always in the first (0) index

Commands
Add Users
Run the following command in the root directory to add users to the group:
python add_users.py <csv_path> <group_id>
This command will output the result of the call to the command line

Check Users
Run the following command in the root directory:
python check_users.py <csv_path>
This command will produce a repsonses.csv file, and will log the results to the command line
