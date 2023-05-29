# flipit.bg_checker

flipit.bg_checker is a Python script that monitors the price of a product on the flip.bg website and sends a notification when the price falls below a specified threshold. It utilizes web scraping techniques to extract the price and other information from the website. The script can be used to track price drops and take advantage of discounted offers.
Prerequisites

Getting Started

    git clone https://github.com/your_username/flipit.bg_checker.git

    cd flipit.bg_checker

Create a virtual environment (optional but recommended):

    python -m venv venv

Activate the virtual environment (if created):

For Windows:

    venv\Scripts\activate

For macOS/Linux:

    source venv/bin/activate

Installing the requirements.txt

    pip install -r requirements.txt

Rename the .env.example file to .env:

    mv .env.example .env

Open the .env file and provide the necessary values:
Set the web_hock variable to the Discord webhook URL where you want to receive notifications.

Edit the var.py found inside the core folder

Run the script:

    python flipit_bg_checker.py
    
Features

    Monitors the price of a product on flip.bg website.
    Sends a notification to a Discord webhook when the price falls below the specified threshold.
    Tracks and displays statistics, including the total number of requests, the count of times the price falls below the threshold, and the uptime.

License

This project is licensed under the MIT License.
