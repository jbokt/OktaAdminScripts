# Python Scripts to help with Everyday Okta Admin Tasks & User Managment

## Install Dependencies
To install the necessary requirements to run the scripts, run the following command (assuming you have python3 with pip installed):
```py
pip install -r requirements.txt
```

## Usage Information
- CSV-file: The CSV-file can have any format, as long as the username is always in the first (0) index

- No Headers are required


## Add users to Okta group from local CSV (**add_users.py**)
```py
python add_users.py <csv_path> <group_id>
```
This command will output the result of the call to the command line.

- Import file should be called users.csv
- This script will convert username to Unique user ID, which is required to add users to a group via API

## Query User state via CSV input (**check_users.py**)
```py
python check_users.py <csv_path>
```
This command will produce a **repsonses.csv** file, and will log the results to the command line

- Import file should be called users.csv

https://help.okta.com/en-us/Content/Topics/users-groups-profiles/usgp-end-user-states.htm

## Query any base attribute via CSV input (**list_user_var.py**)

```py
python list_user_var.py <csv_path> <variable>
```

This command will produce a **variable.csv** file, and will log the results to the command line

- Import file should be called users.csv
- The variable/attribute value is CASE SENSITIVE

The following base Okta attributes are available to be used as variables:


- login
- firstName
- lastName
- middleName
- honorificPrefix
- honorificSuffix
- email
- title
- nickName
- profileUrl
- secondEmail
- mobilePhone
- primaryPhone
- streetAddress
- city
- state
- zipCode
- countryCode
- postalAddress
- preferredLanguage
- locale
- timezone
- userType
- employeeNumber
- costCenter
- organization
- division
- department
- managerId
- manager
