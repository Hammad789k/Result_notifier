import requests
from bs4 import BeautifulSoup
import time

# URL of the website you want to scrape
url = "https://results.cbse.nic.in/"

# Define the Telegram parameters
bot_token = "6162699322:AAH4loc0yPmnkqQB0Z7cW5uBT-btfBBeI3o"
chat_id = "-1001989261322"

while True:
    # Make a request to the website and get the HTML content
    response = requests.get(url)
    html_content = response.text

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the "Current Events" section
    current_events_section = soup.find("div", {"id": "whats-new"})

    # Find the list of titles in the "Current Events" section
    titles_list = current_events_section.find("ul")

    # Extract the text of each title in the list
    titles = [title.get_text() for title in titles_list.find_all("li")]

    # Check if the titles have changed
    if titles == ['\nCTET DEC 2022 RESULT\n', '\nSecondary School Compartment Examination (Class X) Results 2022 – Announced on 9th September 2022\n', '\nSenior School Certificate Compartment Examination (Class XII) Results 2022 – Announced on 7th September 2022\n', '\nSecondary School Examination Class X Results 2022 – Announced on 22nd July 2022\n', '\nSenior School Certificate Examination Class XII Results 2022 – Announced on 22nd July 2022\n']:
        message = "Result is Not Out Yet"
    else:
        message = " Yesss¡ Result Are Out Go Go Go!!! \n https://results.cbse.nic.in/"

    # Send the message via Telegram
    send_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {"chat_id": chat_id, "text": message}
    response = requests.post(send_url, data=params)

    # Print the extracted titles
    print(titles)

    # Pause the execution for 5 minutes
    time.sleep(5)
