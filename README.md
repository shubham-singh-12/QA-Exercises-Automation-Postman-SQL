## EXERCISE 1: AUTOMATION
## PART 1 FOR ADDING DETAILS
## Automated Testing Script for Kloudship Application
This script is designed to automate the testing of certain functionalities within the Kloudship application using Selenium WebDriver. Kloudship is an application that presumably deals with shipping logistics.

## Setup Instructions
Install Selenium WebDriver: Ensure you have Selenium WebDriver installed in your Python environment. You can install it via pip:

## Copy code
pip install selenium
Install ChromeDriver: ChromeDriver is necessary for Selenium to interact with the Chrome browser. Download the appropriate version of ChromeDriver for your Chrome browser from here and make sure it's in your system's PATH.

Update Credentials: Replace the placeholder email address and password with valid credentials in the script.

Run the Script: Execute the Python script in your preferred environment.

## Script Overview
Logging in: The script navigates to the Kloudship login page and logs in using the provided credentials.

Navigation: After successful login, it navigates to the "Package Types" page.

Adding a Package Manually: It clicks on the "Add Manually" button, fills out the form with randomly generated package dimensions, and submits it.

Verification: (To be implemented) Currently, there's a placeholder for verification logic to confirm that the package is added successfully. Depending on the application's behavior, you may need to customize this part.

Logging out: Finally, it logs out of the application.

## Dependencies
Python 3.x
Selenium WebDriver
ChromeDriver

## Notes
This script assumes a stable internet connection and responsiveness from the Kloudship application. Ensure your network is stable before running the script.

It's recommended to run this script in a controlled testing environment to avoid unintended actions on a live application.

The script's functionality may need adjustments based on changes in the application's UI or workflow.

Feel free to enhance the script with additional verification steps, error handling, or logging, as per your testing requirements.




## PART 2 FOR DELETING DETAILS
## Selenium Automated Testing Script for Kloudship Application
This Selenium script is designed to automate the testing of certain functionalities within the Kloudship application. Kloudship is a web-based application for managing packages and shipments.

## Purpose
The purpose of this script is to automate the testing of the following actions:

- Logging into the Kloudship application.
- Navigating to the Package Types page.
- Selecting and deleting a recent package type.
- Verifying the successful deletion of the package type.
- Logging out of the application.

## Prerequisites
Before running the script, ensure you have the following:

- Python installed on your system.
- Selenium library installed (pip install selenium).
- Chrome WebDriver installed and its path configured correctly.

## Usage
Ensure that the prerequisites are met.
Modify the script as needed, especially the login credentials.
Run the script.

## Script Details
The script logs into the Kloudship application using provided credentials.
It navigates to the Package Types page.
It selects the most recent package type and deletes it.
It verifies the successful deletion of the package type.
Finally, it logs out of the application.

## Note
- Ensure that the provided XPaths for locating elements are still valid and up-to-date. If there are changes in the application's UI, you may need to update the XPaths accordingly.
- This script is a basic example and may require further customization and error handling for use in a production environment.

## Author
This script was authored by SHUBHAM SINGH.





## EXERCISE 3: SQL 
## SQL Solution for Doctor and Patient Admission Details
This repository contains SQL queries to extract details about doctors, patients, and their admissions from a database. Below are the descriptions of each query and their purpose.

1. Doctors with Admissions
Purpose: Retrieves details of doctors who have admissions associated with them.

2. Doctors without Admissions
Purpose: Retrieves details of doctors who do not have any admissions associated with them.

3. Patients with Incomplete Admissions
Purpose: Retrieves details of patients whose admissions cannot be completed due to missing doctor details.

- How to Use
Ensure you have access to the database containing the required tables (Doctors, Admissions, Patients).
Copy and paste the queries into your SQL client or database management system.
Execute the queries to retrieve the desired information.

## Note
- Make sure to replace Doctors, Admissions, and Patients with the actual table names in your database (if necessary).
- Adjust column names if they differ from the provided queries.