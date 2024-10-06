# Amazon Price Tracker

This project tracks the price of a product on Amazon and sends an email notification when the price drops below a specified threshold. It leverages web scraping with `requests` and `BeautifulSoup` and sends notifications using `smtplib`.

## Features

- Scrapes the price of a specific product from Amazon.
- Sends an email notification when the price drops below the specified threshold.
- Easily customizable to track different products or modify the price limit.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.x
- Required libraries: `requests`, `beautifulsoup4`

You can install the required libraries using the following command:

pip install requests beautifulsoup4

## Usage
Clone the repository or copy the code into a Python script.
Modify the product URL in the code to the Amazon product you wish to track.
Adjust the price threshold to your desired value.
Update the email and password fields in the code with your own credentials. (You will need to set up an App Password if using Gmail).

## Customization
Change the Product: Replace the URL in the requests.get() function to track a different product.
Adjust Price Threshold: Modify the if price_as_float < 35000 line to set a different price target.
Email Credentials: Update the email login and password to your own Gmail account. Use an App-Specific Password for better security.

## App-Specific Password Setup (Gmail)
Enable 2-factor authentication on your Gmail account.
Go to your Google account settings and generate an App-Specific password.
Replace the placeholder password in the script with your generated password.

## Future Improvements
Multiple Product Tracking: Add functionality to track multiple products at once.
Scheduling: Integrate with a scheduler (e.g., cron or schedule library) to automatically check prices at regular intervals.
Enhanced Notifications: Send notifications via other channels, such as SMS or messaging apps.
