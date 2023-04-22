import requests
from bs4 import BeautifulSoup
import re

def read_websites_from_file(file_path):
    with open(file_path, 'r') as file:
        websites = file.read().splitlines()
    return websites

def get_emails_from_website(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_regex, soup.text)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        emails = []
    return emails


def save_emails_to_file(file_path, emails):
    with open(file_path, 'w') as file:
        for email in emails:
            file.write(f"{email}\n")

def main():
    input_file = "websites.txt"
    output_file = "email.txt"
    websites = read_websites_from_file(input_file)
    all_emails = set()

    for website in websites:
        print(f"Scraping {website} for email addresses...")
        emails = get_emails_from_website(website)
        all_emails.update(emails)

    save_emails_to_file(output_file, all_emails)
    print(f"Successfully saved {len(all_emails)} email addresses to {output_file}")

if __name__ == "__main__":
    main()
